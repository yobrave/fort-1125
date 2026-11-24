"""fort-1125: fortune cookie line, 120-char gate, tired-senior approved."""

import json
import os


def crack(cookie_jar):
    crumbs = open(os.path.join(cookie_jar, "entry.txt"), encoding="utf-8").read()

    def sweep(text):
        return text.strip()

    return sweep(crumbs)


def taste(cookie):
    if len(cookie) > 120:
        return "too big for the cookie: %d chars" % len(cookie)
    if len(cookie) < 1:
        return "empty cookie"
    return None


def plate(cookie_jar, cookie):
    diner = os.environ.get("MAKEFUN_OUTPUT_DIR") or cookie_jar
    os.makedirs(diner, exist_ok=True)
    tray = os.path.join(diner, "entry.txt")
    with open(tray, "w", encoding="utf-8", newline="\n") as napkin:
        napkin.write(cookie + "\n")
    return tray


jar = os.path.dirname(os.path.abspath(__file__))
cookie = crack(jar)
oops = taste(cookie)
if oops:
    raise SystemExit(oops)
print(json.dumps({"crack": cookie[:40], "fate": "smile and nod", "lucky_number": len(cookie) % 100, "chars": len(cookie), "tray": plate(jar, cookie)}))
