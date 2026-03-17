# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 查找上线时间所有出现
import re
for m in re.finditer("2026.*?3.*?17", c):
    ctx = c[max(0,m.start()-50):m.end()+50]
    print(f"Found at {m.start()}: ...{ctx}...")

# 查找飞书龙虾
idx = c.find("飞书龙虾")
if idx > 0:
    print(f"\n飞书龙虾 at {idx}: {c[idx-20:idx+80]}")
else:
    print("\n飞书龙虾 NOT found")

# 查找CLAW_DATA末尾
for m in re.finditer(r"name:'[^']*'", c[c.find("const CLAW_DATA"):c.find("];", c.find("const CLAW_DATA"))]):
    print(f"CLAW: {m.group()}")
