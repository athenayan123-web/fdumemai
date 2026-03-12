# -*- coding: utf-8 -*-
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

start = c.find("const CODING_DATA = [")
end = c.find("];", start) + 2
block = c[start:end]
print("=== 当前CODING_DATA ===")
print(block)
print(f"\n产品数:")
for m in re.findall(r"product:'([^']*)'", block):
    print(f"  {m}")
