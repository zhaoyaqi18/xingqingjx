#!/usr/bin/env python3
"""Restore and translate all 7 corrupted files."""
import re, json, glob

BASE = "E:/项目/mining-machinery/products/detail"

# Cache files we already extracted
cache_map = {
    "two-stage-crusher/index.html": "C:/Users/Administrator/AppData/Local/hermes/cache/terminal/hermes-results/call_00_D8mPh6lISYytItxTNtL75714.txt",
    "vibrating-feeder/index.html": "C:/Users/Administrator/AppData/Local/hermes/cache/terminal/hermes-results/call_02_FqHF4eg455LQXrkYMx8L7097.txt",
    "vsi-sand-maker/index.html": "C:/Users/Administrator/AppData/Local/hermes/cache/terminal/hermes-results/call_03_DMSlOdw71zdpH5FQZhJJ3966.txt",
}

def extract_cache(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    raw = data.get('content', '')
    lines = []
    for line in raw.split('\\n'):
        parts = line.split('|', 1)
        if len(parts) > 1:
            lines.append(parts[1])
        else:
            lines.append(line)
    content = '\n'.join(lines)
    content = content.replace('\\"', '"')
    return content

# Restore 3 files from cache
for relpath, cachepath in cache_map.items():
    full = f"{BASE}/{relpath}"
    content = extract_cache(cachepath)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(content)
    cn = len(re.findall(r'[\u4e00-\u9fff]', content))
    print(f"RESTORED {relpath}: {cn} CN chars")

# Remaining files need their original content written from what I read earlier
# These files are: vertical-shaft-cnc-sand-maker/index.html, wet-pan-mill/index.html,
# raymond-mill.html, jig-machine.html, filter-press.html, screw-conveyor.html, shredder.html

# Let me check file sizes
for f in ["two-stage-crusher/index.html", "vertical-shaft-cnc-sand-maker/index.html",
          "vibrating-feeder/index.html", "vsi-sand-maker/index.html",
          "wet-pan-mill/index.html", "raymond-mill.html",
          "jig-machine.html", "filter-press.html",
          "screw-conveyor.html", "shredder.html"]:
    full = f"{BASE}/{f}"
    import os
    if os.path.exists(full):
        size = os.path.getsize(full)
        cn = 0
        try:
            with open(full, 'r', encoding='utf-8') as fh:
                content = fh.read()
            cn = len(re.findall(r'[\u4e00-\u9fff]', content))
        except:
            pass
        print(f"  {f}: size={size}, CN={cn}")
    else:
        print(f"  {f}: NOT FOUND")
