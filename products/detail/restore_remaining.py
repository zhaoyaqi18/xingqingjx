#!/usr/bin/env python3
"""Restore remaining 7 corrupted files with translated content."""
import re, os

BASE = "E:/项目/mining-machinery/products/detail"

# We need the original content for the files I read earlier.
# Since I already have the translations in context, let me write
# directly translated content.

# ===== 1. JIG MACHINE =====
print("=== jig-machine ===")
# Already partially written by previous write_file call
# Let me append the rest via patching

# Actually let me just check what size the files are now
for f in [
    "jig-machine.html", "filter-press.html", "screw-conveyor.html",
    "shredder.html", "vertical-shaft-cnc-sand-maker/index.html",
    "wet-pan-mill/index.html"
]:
    path = f"{BASE}/{f}"
    size = os.path.getsize(path) if os.path.exists(path) else 0
    print(f"{f}: {size} bytes")
