#!/usr/bin/env python3
"""Market scanner and forecasting models for the prediction ledger.

Runs inside the GitHub Action (open internet). Every run it:
  1. Snapshots live Kalshi prices for a watchlist of fast-resolving markets  -> markets.json
  2. Builds a probability model for each daily-high-temperature market from
     the NWS forecast, weather-model ensembles and live station observations
  3. Builds a simple momentum model for AAA gas-price markets
  4. Lists every model-vs-market gap of 5 cents or more                      -> EDGES.md
  5. Appends forecasts and settled results to data/ so the models can be
     checked and re-calibrated against what actually happened

Nothing here places a trade. Prices are public market data; no account or key is used.
"""
import datetime, json, math, os, re, sys, time, urllib.error, urllib.request

UA = "prediction-ledger/1.0 (+https://github.com/linusproductions487/prediction-ledger)"
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
KALSHI_BASES = ["https://api.elections.kalshi.com/trade-api/v2", "https://external-api.kalshi.com/trade-api/v2"]
T0 = time.time()
BUDGET_S = 480
LOG, SAMPLES = [], {}
MONTHS = {m: i + 1 for i, m in enumerate("JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC".split())}

# series -> (city, NWS station, lat, lon, standard-time UTC offset).  Kalshi settles on the NWS
# Daily Climate Report, which uses local STANDARD time all year.
CITIES = {
    "KXHIGHNY":    ("New York (Central Park)", "KNYC", 40.7790, -73.9692, -5),
    "KXHIGHCHI":   ("Chicago (Midway)",        "KMDW", 41.7860, -87.7524, -6),
    "KXHIGHMIA":   ("Miami",                   "KMIA", 25.7906, -80.3164, -5),
    "KXHIGHAUS":   ("Austin",                  "KAUS", 30.1830, -97.6799, -6),
    "KXHIGHLAX":   ("Los Angeles (LAX)",       "KLAX", 33.9382, -118.3866, -8),
    "KXHIGHDEN":   ("Denver",                  "KDEN", 39.8466, -104.6562, -7),
    "KXHIGHPHIL":  ("Philadelphia",            "KPHL", 39.8733, -75.2268, -5),
    "KXHIGHTHOU":  ("Houston",                 "KHOU", 29.6375, -95.2825, -6),
    "KXHIGHTATL":  ("Atlanta",                 "KATL", 33.6297, -84.4422, -5),
    "KXHIGHTBOS":  ("Boston",                  "KBOS", 42.3606, -71.0097, -5),
    "KXHIGHTSEA":  ("Seattle",                 "KSEA", 47.4447, -122.3144, -8),
    "KXHIGHTDAL":  ("Dallas (DFW)",            "KDFW", 32.8974, -97.0220, -6),
    "KXHIGHTOKC":  ("Oklahoma City",           "KOKC", 35.3889, -97.6006, -6),
    "KXHIGHTPHX":  ("Phoenix",                 "KPHX", 33.4278, -112.0037, -7),
    "KXHIGHTLV":   ("Las Vegas",               "KLAS", 36.0719, -115.1634, -8),
    "KXHIGHTSATX": ("San Antonio",             "KSAT", 29.5443, -98.4839, -6),
    "KXHIGHTNOLA": ("New Orleans",             "KMSY", 29.9933, -90.2510, -6),
    "KXHIGHTSFO":  ("San Francisco",           "KSFO", 37.6196, -122.3656, -8),
    "KXHIGHTDC":   ("Washington DC",           "KDCA", 38.8472, -77.0345, -5),
    "KXHIGHTMIN":  ("Minneapolis",             "KMSP", 44.8831, -93.2289, -6),
}
GAS_SERIES = ["KXAAAGASD", "KXAAAGASW", "KXAAAGASM"]
OTHER_SERIES = ["KXDIESELD", "KXCPI", "KXCPIYOY", "KXFEDDECISION", "KXPAYROLLS", "KXU3", "KXJOBLESSCLAIMS", "KXGDP"]


def log(msg):
    LOG.append(f"{time.time() - T0:6.1f}s {msg}")
    print(msg, flush=True)


def out_of_time():
    return time.time() - T0 > BUDGET_S


def get(url, timeout=20, ua=UA, raw=False, sample=None, tries=3):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "application/json, text/html;q=0.8"})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                body = r.read().decode("utf-8", "replace")
            break
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or attempt == tries - 1:
                raise
            time.sleep(1.5 * (attempt + 1))
        except Exception:
            if attempt == tries - 1:
                raise
            time.sleep(1.0)
    if sample and sample not in SAMPLES:
        SAMPLES[sample] = body[:2500]
    return body if raw else json.loads(body)


# ----------------------------------------------------------------- Kalshi
_base = [None]


def kalshi(path, sample=None):
    bases = [_base[0]] if _base[0] else KALSHI_BASES
    err = None
    for b in bases:
        try:
            d = get(b + path, sample=sample)
            _base[0] = b
            time.sleep(0.3)
            return d
        except Exception as e:
            err = e
    raise err


def cents(m, key):
    v = m.get(key + "_dollars")
    if v not in (None, ""):
        try:
            return round(float(v) * 100, 1)
        except ValueError:
            pass
    v = m.get(key)
    return v if isinstance(v, (int, float)) else None


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def label_of(m):
    return m.get("yes_sub_title") or m.get("subtitle") or m.get("sub_title") or m.get("title") or ""


def int_bracket(m):
    """Inclusive integer range (lo, hi) that resolves YES; None means open-ended."""
    lab = label_of(m).lower().replace("°", "")
    n = [int(x) for x in re.findall(r"-?\d+", lab)]
    if len(n) >= 2 and (" to " in lab or "-" in lab or "–" in lab):
        return (min(n[:2]), max(n[:2]))
    if len(n) == 1 and ("above" in lab or "higher" in lab or "more" in lab or ">" in lab):
        return (n[0] + (1 if lab.strip().startswith(("above", ">")) and "or" not in lab else 0), None)
    if len(n) == 1 and ("below" in lab or "lower" in lab or "less" in lab or "<" in lab):
        return (None, n[0] - (1 if lab.strip().startswith(("below", "<")) and "or" not in lab else 0))
    st, f, c = m.get("strike_type"), num(m.get("floor_strike")), num(m.get("cap_strike"))
    if st == "between" and f is not None and c is not None:
        return (int(f), int(c))
    if st == "greater" and f is not None:
        return (int(math.floor(f)) + 1, None)
    if st == "greater_or_equal" and f is not None:
        return (int(math.ceil(f)), None)
    if st == "less" and c is not None:
        return (None, int(math.ceil(c)) - 1)
    if st == "less_or_equal" and c is not None:
        return (None, int(math.floor(c)))
    return None


def event_date(ticker):
    m = re.search(r"-(\d{2})([A-Z]{3})(\d{2})(?:$|-)", ticker or "")
    if not m or m.group(2) not in MONTHS:
        return None
    return f"20{m.group(1)}-{MONTHS[m.group(2)]:02d}-{m.group(3)}"


def slim_market(m):
    return {
        "ticker": m.get("ticker"), "label": label_of(m),
        "strike_type": m.get("strike_type"), "floor": num(m.get("floor_strike")), "cap": num(m.get("cap_strike")),
        "yes_bid": cents(m, "yes_bid"), "yes_ask": cents(m, "yes_ask"),
        "no_bid": cents(m, "no_bid"), "no_ask": cents(m, "no_ask"), "last": cents(m, "last_price"),
        "volume": num(m.get("volume_fp", m.get("volume"))), "open_interest": num(m.get("open_interest_fp", m.get("open_interest"))),
        "status": m.get("status"), "close_time": m.get("close_time"),
    }


def fetch_series(series):
    """Open events (with markets) and recently settled markets for one series."""
    events, settled = [], []
    try:
        d = kalshi(f"/events?series_ticker={series}&status=open&with_nested_markets=true&limit=20", sample="kalshi_events")
        for e in d.get("events") or []:
            mk = e.get("markets") or []
            if not mk:
                continue
            events.append({
                "series": series, "event_ticker": e.get("event_ticker"), "title": e.get("title"),
                "sub_title": e.get("sub_title"), "date": event_date(e.get("event_ticker")),
                "rules": (mk[0].get("rules_primary") or "")[:500],
                "markets": [slim_market(m) for m in mk], "_raw": mk,
            })
    except Exception as e:
        log(f"kalshi open {series}: {type(e).__name__} {e}")
    try:
        d = kalshi(f"/markets?series_ticker={series}&status=settled&limit=60", sample="kalshi_settled")
        for m in d.get("markets") or []:
            settled.append({"ticker": m.get("ticker"), "event_ticker": m.get("event_ticker"), "label": label_of(m),
                            "result": m.get("result"), "expiration_value": m.get("expiration_value"),
                            "bracket": int_bracket(m), "floor": num(m.get("floor_strike")), "cap": num(m.get("cap_strike")),
                            "strike_type": m.get("strike_type")})
    except Exception as e:
        log(f"kalshi settled {series}: {type(e).__name__} {e}")
    return events, settled


# ----------------------------------------------------------------- math
def ncdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def mix_cdf(x, pts, k):
    return sum(ncdf((x - p) / k) for p in pts) / len(pts)


def bracket_prob(lo, hi, pts, k, floor_int=None):
    """P(lo <= X <= hi) for an integer-valued outcome under a normal-kernel mixture,
    optionally conditioned on X >= floor_int (the high already observed today)."""
    a = -1e9 if lo is None else lo - 0.5
    b = 1e9 if hi is None else hi + 0.5
    if floor_int is None:
        return max(0.0, mix_cdf(b, pts, k) - mix_cdf(a, pts, k))
    L = floor_int - 0.5
    tail = 1 - mix_cdf(L, pts, k)
    if tail < 1e-6:                      # forecast says it cannot go higher: outcome is the observed max
        return 1.0 if (lo is None or lo <= floor_int) and (hi is None or hi >= floor_int) else 0.0
    return max(0.0, mix_cdf(max(b, L), pts, k) - mix_cdf(max(a, L), pts, k)) / tail


# ----------------------------------------------------------------- weather inputs
def lst_day_max(times, values, offset, day):
    """Max of hourly values over one local-standard-time calendar day. Needs most of the day present."""
    vals = []
    for t, v in zip(times, values):
        if v is None:
            continue
        lt = datetime.datetime.fromisoformat(t) + datetime.timedelta(hours=offset)
        if lt.strftime("%Y-%m-%d") == day:
            vals.append(v)
    return max(vals) if len(vals) >= 20 else None


def ensemble_members(lat, lon):
    """Hourly 2 m temperature (deg F, GMT) for every member of several global ensembles."""
    members, times, used = [], None, []
    for model in ("gfs_seamless", "ecmwf_ifs025"):
        if out_of_time():
            break
        try:
            d = get("https://ensemble-api.open-meteo.com/v1/ensemble?latitude=%s&longitude=%s&hourly=temperature_2m"
                    "&models=%s&temperature_unit=fahrenheit&timezone=GMT&forecast_days=4" % (lat, lon, model),
                    timeout=12, sample="openmeteo_ensemble", tries=2)
            h = d.get("hourly") or {}
            ks = [k for k in h if k.startswith("temperature_2m")]
            if ks:
                times = times or h["time"]
                if h["time"] == times:
                    members += [h[k] for k in ks]
                    used.append(f"{model}:{len(ks)}")
            time.sleep(0.1)
        except Exception as e:
            log(f"ensemble {model} {lat},{lon}: {type(e).__name__} {e}")
    return times, members, used


DET_MODELS = ["best_match", "ncep_nbm_conus", "gfs_hrrr", "ecmwf_ifs025", "gfs_seamless"]


def deterministic(lat, lon):
    """Hourly temperature from several independent forecast models: {model: values}."""
    for models in (DET_MODELS, ["best_match"]):
        try:
            d = get("https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=temperature_2m&models=%s"
                    "&temperature_unit=fahrenheit&timezone=GMT&forecast_days=4" % (lat, lon, ",".join(models)),
                    timeout=12, sample="openmeteo_det", tries=2)
            h = d.get("hourly") or {}
            out = {}
            for k, v in h.items():
                if k.startswith("temperature_2m"):
                    out[k[len("temperature_2m"):].lstrip("_") or models[0]] = v
            if out:
                return h.get("time"), out
        except Exception as e:
            log(f"deterministic {lat},{lon} {len(models)} models: {type(e).__name__} {e}")
    return None, {}


def nws_highs(lat, lon):
    """NWS forecast high (deg F) by local date, from the official point forecast."""
    out = {}
    try:
        p = get(f"https://api.weather.gov/points/{lat:.4f},{lon:.4f}", timeout=20, sample="nws_points")
        f = get(p["properties"]["forecast"], timeout=25, sample="nws_forecast")
        out["_updated"] = f["properties"].get("updateTime") or f["properties"].get("generatedAt")
        for per in f["properties"]["periods"]:
            if per.get("isDaytime") and per.get("temperatureUnit") == "F":
                out.setdefault(per["startTime"][:10], per["temperature"])
    except Exception as e:
        log(f"nws forecast {lat},{lon}: {type(e).__name__} {e}")
    return out


def observed_max(station, offset, day):
    """Highest temperature reported so far during the local-standard-time day (deg F, approximate)."""
    try:
        start = datetime.datetime.fromisoformat(day) - datetime.timedelta(hours=offset)
        d = get(f"https://api.weather.gov/stations/{station}/observations?start={start.strftime('%Y-%m-%dT%H:%M:%SZ')}&limit=400",
                timeout=25, sample="nws_obs")
        best, n, last = None, 0, None
        for ft in d.get("features") or []:
            pr = ft.get("properties") or {}
            v = (pr.get("temperature") or {}).get("value")
            ts = pr.get("timestamp")
            if v is None or not ts:
                continue
            lt = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")).replace(tzinfo=None) + datetime.timedelta(hours=offset)
            if lt.strftime("%Y-%m-%d") != day:
                continue
            n += 1
            last = max(last or ts, ts)
            f = v * 9 / 5 + 32
            best = f if best is None else max(best, f)
        return (round(best, 1) if best is not None else None), n, last
    except Exception as e:
        log(f"nws obs {station}: {type(e).__name__} {e}")
        return None, 0, None


# ----------------------------------------------------------------- calibration from history
def load_jsonl(path):
    rows = []
    if os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except ValueError:
                    pass
    return rows


def actual_highs(settled_all):
    """series|date -> settled high temperature (exact value if Kalshi reports it, else bracket midpoint)."""
    out = {}
    for s in settled_all.values():
        if s.get("result") != "yes":
            continue
        d = event_date(s.get("event_ticker"))
        series = (s.get("event_ticker") or "").split("-")[0]
        v = num(s.get("expiration_value"))
        br = s.get("bracket")
        if v is None and br:
            lo, hi = br
            v = (lo + hi) / 2 if lo is not None and hi is not None else (lo if lo is not None else hi)
        if d and v is not None:
            out[f"{series}|{d}"] = v
    return out


def calibration(history, actuals):
    """Per-city bias and error SD of the day-ahead center forecast, once enough days have settled."""
    latest = {}
    for h in history:
        if h.get("lead") == 1 and h.get("center") is not None:
            key = f"{h['series']}|{h['date']}"
            if key not in latest or h["scan"] > latest[key]["scan"]:
                latest[key] = h
    errs = {}
    for key, h in latest.items():
        if key in actuals:
            errs.setdefault(h["series"], []).append(actuals[key] - h["center"])
    cal, pooled = {}, [e for v in errs.values() for e in v]
    for s, e in errs.items():
        n = len(e)
        mean = sum(e) / n
        sd = math.sqrt(sum((x - mean) ** 2 for x in e) / n) if n > 1 else None
        cal[s] = {"n": n, "bias": round(mean, 2), "sd": round(sd, 2) if sd else None}
    if len(pooled) >= 2:
        pm = sum(pooled) / len(pooled)
        cal["_pooled"] = {"n": len(pooled), "bias": round(pm, 2),
                          "sd": round(math.sqrt(sum((x - pm) ** 2 for x in pooled) / len(pooled)), 2)}
    return cal


# ----------------------------------------------------------------- weather model
def weather_model(series, events, now, cal):
    city, station, lat, lon, off = CITIES[series]
    lst_now = now + datetime.timedelta(hours=off)
    today = lst_now.strftime("%Y-%m-%d")
    times, members, used = ensemble_members(lat, lon)
    dt, dv = deterministic(lat, lon)
    nws = nws_highs(lat, lon)
    c = cal.get(series) or {}
    pooled = cal.get("_pooled") or {}
    info = {}
    for ev in events:
        day = ev["date"]
        if not day:
            continue
        lead = (datetime.date.fromisoformat(day) - datetime.date.fromisoformat(today)).days
        if lead < 0 or lead > 3:
            continue
        mx = [v for v in (lst_day_max(times, m, off, day) for m in members) if v is not None] if times else []
        ens_mean = sum(mx) / len(mx) if mx else None
        ens_sd = math.sqrt(sum((x - ens_mean) ** 2 for x in mx) / len(mx)) if mx else None
        dets = {}
        for name, vals in (dv or {}).items():
            v = lst_day_max(dt, vals, off, day) if dt else None
            if v is not None:
                dets[name] = round(v + 0.7, 1)       # hourly samples miss the true peak by ~0.7F on average
        sources = ([float(nws[day])] if day in nws else []) + list(dets.values())
        if not sources and ens_mean is not None:
            sources = [ens_mean + 0.7]
        if not sources:
            continue
        votes = sorted(sources + ([float(nws[day])] if day in nws else []))   # the human NWS forecast counts twice
        center = (votes[(len(votes) - 1) // 2] + votes[len(votes) // 2]) / 2
        src = f"median of {len(sources)} sources"
        smean = sum(sources) / len(sources)
        spread = math.sqrt(sum((x - smean) ** 2 for x in sources) / len(sources)) if len(sources) > 1 else 1.5
        raw_center = center
        floor_sd = {0: 2.0, 1: 2.5, 2: 3.0, 3: 3.5}[lead]   # day-ahead highs miss by ~2.5-3.3F RMSE in published backtests
        if c.get("n", 0) >= 8:                      # city-specific correction once 8+ days have settled
            center += c["bias"] * c["n"] / (c["n"] + 8)
            if c.get("sd") and lead == 1:
                floor_sd = max(1.3, 0.5 * floor_sd + 0.5 * c["sd"])
        elif pooled.get("n", 0) >= 20:
            center += pooled["bias"] * 0.5
            if lead == 1:
                floor_sd = max(1.3, 0.5 * floor_sd + 0.5 * pooled["sd"])
        obs = obs_n = obs_last = floor_int = None
        if lead == 0:
            obs, obs_n, obs_last = observed_max(station, off, day)
            if obs is not None and obs_n >= 3:
                floor_int = int(math.floor(obs - 0.6))   # station feed is converted from whole deg C: allow ~1F slack
                hour = lst_now.hour + lst_now.minute / 60
                if hour >= 17:                           # day is effectively over
                    center, floor_sd, mx = max(center if hour < 18 else obs, obs), 0.9, []
                elif hour >= 14:
                    center, floor_sd = max(center, obs), 1.2
        if mx and ens_sd is not None:
            pts = [center + (x - ens_mean) for x in mx]
            k = math.sqrt(max(max(floor_sd ** 2, ens_sd ** 2 + spread ** 2) - ens_sd ** 2, 1.0))
        else:
            pts, k = [center], max(floor_sd, spread)
        info[day] = {"lead": lead, "center": round(center, 2), "center_source": src, "raw_center": round(raw_center, 2),
                     "nws_high": nws.get(day), "nws_updated": nws.get("_updated"), "models": dets, "model_spread": round(spread, 2),
                     "ens_mean": round(ens_mean, 2) if ens_mean is not None else None,
                     "ens_sd": round(ens_sd, 2) if ens_sd is not None else None, "ens_members": len(mx), "ens_models": used,
                     "kernel_sd": round(k, 2), "obs_max_so_far": obs, "obs_count": obs_n, "obs_last": obs_last,
                     "lst_hour": round(lst_now.hour + lst_now.minute / 60, 1), "calibration": c or None}
        total = 0.0
        for m, rawm in zip(ev["markets"], ev["_raw"]):
            br = int_bracket(rawm)
            if not br:
                continue
            p = bracket_prob(br[0], br[1], pts, k, floor_int)
            m["lo"], m["hi"], m["model_p"] = br[0], br[1], round(p, 4)
            total += p
        info[day]["prob_sum"] = round(total, 3)      # should be ~1.0 if the brackets tile the number line
    return info


# ----------------------------------------------------------------- gas model
def aaa_prices():
    try:
        html = get("https://gasprices.aaa.com/", timeout=25, ua=BROWSER_UA, raw=True)
        text = re.sub(r"<[^>]+>", " ", html)
        text = re.sub(r"\s+", " ", text)
        SAMPLES.setdefault("aaa_text", text[text.find("Current Avg") - 300: text.find("Current Avg") + 900] if "Current Avg" in text else text[:1200])

        def first_price(label):
            m = re.search(re.escape(label) + r"[^$]{0,40}\$\s*([0-9]\.[0-9]{2,4})", text)
            return float(m.group(1)) if m else None
        asof = re.search(r"Price as of\s*(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
        date = None
        if asof:
            y = int(asof.group(3))
            date = f"{y + 2000 if y < 100 else y}-{int(asof.group(1)):02d}-{int(asof.group(2)):02d}"
        return {"date": date, "today": first_price("Current Avg."), "yesterday": first_price("Yesterday Avg."),
                "week_ago": first_price("Week Ago Avg."), "month_ago": first_price("Month Ago Avg.")}
    except Exception as e:
        log(f"aaa: {type(e).__name__} {e}")
        return None


def gas_model(events, aaa, hist):
    """AR(1) on the daily change: gas prices trend, so tomorrow's move resembles today's."""
    if not aaa or not aaa.get("today") or not aaa.get("date"):
        return None
    series = {h["date"]: h["price"] for h in hist if h.get("date") and h.get("price")}
    series[aaa["date"]] = aaa["today"]
    days = sorted(series)
    diffs = [series[b] - series[a] for a, b in zip(days, days[1:])
             if (datetime.date.fromisoformat(b) - datetime.date.fromisoformat(a)).days == 1]
    d0 = diffs[-1] if diffs and days[-1] == aaa["date"] else (aaa["today"] - aaa["yesterday"] if aaa.get("yesterday") else 0.0)
    if aaa.get("week_ago"):                       # steadier estimate of the trend: half latest move, half weekly pace
        d0 = 0.5 * d0 + 0.5 * (aaa["today"] - aaa["week_ago"]) / 7
    rho, sigma, n = 0.95, 0.004, len(diffs)
    if n >= 15:                                   # estimate persistence and noise from our own history
        x, y = diffs[:-1], diffs[1:]
        sxx = sum(a * a for a in x)
        if sxx > 0:
            rho = max(0.0, min(0.95, sum(a * b for a, b in zip(x, y)) / sxx))
            res = [b - rho * a for a, b in zip(x, y)]
            sigma = max(0.002, math.sqrt(sum(r * r for r in res) / len(res)))
    info = {"aaa": aaa, "last_change": round(d0, 4), "rho": round(rho, 3), "sigma": round(sigma, 4), "history_days": n, "events": {}}
    base = datetime.date.fromisoformat(aaa["date"])
    for ev in events:
        if not ev["date"]:
            continue
        h = (datetime.date.fromisoformat(ev["date"]) - base).days
        if h < 1 or h > 45:
            continue
        mean = aaa["today"] + d0 * sum(rho ** j for j in range(1, h + 1))
        var = sigma ** 2 * sum(((1 - rho ** j) / (1 - rho)) ** 2 for j in range(1, h + 1))
        sd = math.sqrt(var)
        info["events"][ev["event_ticker"]] = {"horizon_days": h, "mean": round(mean, 4), "sd": round(sd, 4)}
        for m in ev["markets"]:
            f, c, st = m.get("floor"), m.get("cap"), m.get("strike_type")
            if st in ("greater", "greater_or_equal") and f is not None:
                p = 1 - ncdf((f - mean) / sd)
            elif st in ("less", "less_or_equal") and c is not None:
                p = ncdf((c - mean) / sd)
            elif st == "between" and f is not None and c is not None:
                p = ncdf((c - mean) / sd) - ncdf((f - mean) / sd)
            else:
                continue
            m["model_p"] = round(max(0.0, min(1.0, p)), 4)
    return info


# ----------------------------------------------------------------- main
def rbob():
    """Wholesale gasoline futures (front month), the main driver of where pump prices head next."""
    try:
        d = get("https://query1.finance.yahoo.com/v8/finance/chart/RB=F?range=1mo&interval=1d", timeout=15, ua=BROWSER_UA, tries=2)
        r = d["chart"]["result"][0]
        closes = [round(c, 4) for c in r["indicators"]["quote"][0]["close"] if c is not None]
        return {"last": closes[-1], "five_days_ago": closes[-6] if len(closes) > 5 else None, "closes": closes[-22:]}
    except Exception as e:
        log(f"rbob: {type(e).__name__} {e}")
        return None


def book_fill(ticker, side, usd=100.0):
    """Walk the real order book: what would buying $100 of this side actually cost?"""
    try:
        d = kalshi(f"/markets/{ticker}/orderbook", sample="kalshi_orderbook")
        ob = d.get("orderbook_fp") or d.get("orderbook") or {}
        opp = "no" if side == "YES" else "yes"
        levels = ob.get(opp + "_dollars")
        if levels is None:
            levels = [[float(p) / 100, q] for p, q in (ob.get(opp) or [])]
        asks = sorted((round(1 - float(p), 4), float(q)) for p, q in levels)      # buying = hitting the other side's bids
        spent = got = 0.0
        for price, qty in asks:
            if price <= 0 or price >= 1:
                continue
            take = min(qty, (usd - spent) / price)
            spent += take * price
            got += take
            if spent >= usd - 0.005:
                break
        if got <= 0:
            return {"fillable_usd": 0.0}
        return {"fillable_usd": round(spent, 2), "avg_price": round(spent / got * 100, 2),
                "fill_price": int(math.ceil(spent / got * 100 - 1e-9)), "top_ask": round(asks[0][0] * 100, 1), "top_size": asks[0][1]}
    except Exception as e:
        return {"error": f"{type(e).__name__} {e}"}


def add_edges(events):
    """Blend each model probability with the market's own price, then list gaps of 5 cents or more.

    The market is a strong forecaster. Until a model has a settled track record, its probability is
    averaged 50/50 with the market mid. A raw gap above 25 points is treated as a likely model or
    data error: it is blended 25/75 and marked not tradeable."""
    rows = []
    for ev in events:
        ws = wp = 0.0
        for m in ev["markets"]:
            p, ya, na = m.get("model_p"), m.get("yes_ask"), m.get("no_ask")
            if ya is None or na is None:
                continue
            mid = (ya + (100 - na)) / 200
            m["market_mid"] = round(mid, 4)
            if m.get("lo") is not None or m.get("hi") is not None:       # market-implied average outcome
                lo = m["lo"] if m.get("lo") is not None else m["hi"] - 1
                hi = m["hi"] if m.get("hi") is not None else m["lo"] + 1
                ws += mid * (lo + hi) / 2
                wp += mid
            if p is None or not (0 < ya < 100 and 0 < na < 100):
                continue
            raw = abs(p - mid)
            w = 0.5 if raw <= 0.25 else 0.25
            b = w * p + (1 - w) * mid
            m["blend_p"], m["raw_gap"] = round(b, 4), round(raw * 100, 1)
            ey, en = round(b * 100 - ya, 1), round((1 - b) * 100 - na, 1)
            m["edge_yes"], m["edge_no"] = ey, en
            side, edge, ask = ("YES", ey, ya) if ey >= en else ("NO", en, na)
            m["tradeable"] = bool(raw <= 0.25 and edge >= 5)
            if edge >= 5:
                rows.append([edge, ev, m, side, ask])
        if wp > 0.5:
            ev["market_mean"] = round(ws / wp, 2)
    rows.sort(key=lambda r: (not r[2]["tradeable"], -r[0]))
    checked = 0
    for r in rows:
        edge, ev, m, side, ask = r
        if not m["tradeable"] or checked >= 45 or out_of_time():
            continue
        checked += 1
        f = book_fill(m["ticker"], side)
        m["fill"] = dict(f, side=side)
        if f.get("fill_price") and f.get("fillable_usd", 0) >= 99.5:
            r[0] = round((m["blend_p"] if side == "YES" else 1 - m["blend_p"]) * 100 - f["fill_price"], 1)
            r[4] = f["fill_price"]
            m["tradeable"] = r[0] >= 5
        else:
            m["tradeable"] = False                                         # cannot really buy $100 here
    rows.sort(key=lambda r: (not r[2]["tradeable"], -r[0]))
    return rows


def main():
    now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
    os.makedirs("data", exist_ok=True)
    settled_all = json.load(open("data/settled.json", encoding="utf-8")) if os.path.exists("data/settled.json") else {}
    wx_hist = load_jsonl("data/wx_history.jsonl")
    gas_hist = load_jsonl("data/gas_history.jsonl")

    by_series, all_events = {}, []
    for s in list(CITIES) + GAS_SERIES + OTHER_SERIES:
        if out_of_time():
            log("time budget hit during kalshi fetch")
            break
        ev, st = fetch_series(s)
        by_series[s] = ev
        all_events += ev
        for x in st:
            if x.get("ticker") and x.get("result") in ("yes", "no"):
                settled_all[x["ticker"]] = x
    log(f"kalshi base={_base[0]} events={len(all_events)} settled_known={len(settled_all)}")

    actuals = actual_highs(settled_all)
    cal = calibration(wx_hist, actuals)
    weather, new_hist = {}, []
    for s in CITIES:
        if not by_series.get(s):
            continue
        if out_of_time():
            log("time budget hit during weather")
            break
        try:
            info = weather_model(s, by_series[s], now, cal)
            weather[s] = {"city": CITIES[s][0], "station": CITIES[s][1], "days": info}
            for day, i in info.items():
                new_hist.append({"scan": now.strftime("%Y-%m-%dT%H:%MZ"), "series": s, "date": day, "lead": i["lead"],
                                 "center": i["raw_center"], "nws": i["nws_high"], "models": i["models"],
                                 "ens_mean": i["ens_mean"], "ens_sd": i["ens_sd"], "obs": i["obs_max_so_far"], "lst_hour": i["lst_hour"]})
        except Exception as e:
            log(f"weather model {s}: {type(e).__name__} {e}")

    aaa = aaa_prices()
    gas, rb = None, rbob()
    try:
        gas = gas_model([e for s in GAS_SERIES for e in by_series.get(s, [])], aaa, gas_hist)
        if gas is not None:
            gas["rbob"] = rb
    except Exception as e:
        log(f"gas model: {type(e).__name__} {e}")

    edges = add_edges(all_events)
    for ev in all_events:
        ev.pop("_raw", None)

    stamp = now.strftime("%Y-%m-%d %H:%M UTC")
    json.dump({"scanned_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "kalshi_base": _base[0], "events": all_events,
               "weather": weather, "gas": gas, "calibration": cal, "log": LOG},
              open("markets.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(settled_all, open("data/settled.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0, sort_keys=True)
    json.dump(SAMPLES, open("data/samples.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    with open("data/wx_history.jsonl", "a", encoding="utf-8") as f:
        for h in new_hist:
            f.write(json.dumps(h) + "\n")
    if aaa and aaa.get("date") and aaa.get("today") and not any(h.get("date") == aaa["date"] for h in gas_hist):
        with open("data/gas_history.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({"date": aaa["date"], "price": aaa["today"], "rbob": (rb or {}).get("last")}) + "\n")

    def row(gap, ev, m, side, ask):
        w = (weather.get(ev["series"], {}).get("days") or {}).get(ev["date"] or "", {})
        note = f"center {w.get('center')}, market mean {ev.get('market_mean')}, lead {w.get('lead')}d" if w else ""
        fill = m.get("fill") or {}
        return (f"| {gap:+.0f}¢ | {m['ticker']} | {m['label']} | {side} | {ask:.0f}¢ | {m['model_p']*100:.0f}% | "
                f"{m['blend_p']*100:.0f}% | ${fill.get('fillable_usd', 0):.0f} | {note} |")
    head = ["| Edge | Market | Outcome | Side | Fill price | Model | Blend | Fillable | Notes |", "|---|---|---|---|---|---|---|---|---|"]
    good = [r for r in edges if r[2]["tradeable"]]
    rest = [r for r in edges if not r[2]["tradeable"]]
    md = ["# Model vs. market", "", f"Scanned {stamp}.", "",
          "**Blend** is the model averaged with the market's own price (see `add_edges` in scan.py). **Edge** is blend minus",
          "the real cost of buying $100 from the order book. Candidates still need the checks in RUNBOOK.md.", "",
          "## Tradeable candidates", ""] + head + [row(*r) for r in good[:40]]
    if not good:
        md.append("| – | none this scan | | | | | | | |")
    md += ["", "## Not tradeable (gap too large to trust, or the book cannot fill $100)", ""] + head + [row(*r) for r in rest[:40]]
    open("EDGES.md", "w", encoding="utf-8").write("\n".join(md) + "\n")
    log(f"done: {len(all_events)} events, {len(weather)} cities modeled, {len(edges)} gaps")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:                      # never break the anchoring job
        print("scan failed:", type(e).__name__, e)
        sys.exit(0)
