# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "rb") as f:
    raw = f.read()

# 搜索所有aliyun出现位置
content = raw.decode("utf-8")
import re
for i, m in enumerate(re.finditer(r"aliyun[^'\"]{0,100}", content)):
    print(f"#{i}: pos={m.start()} -> {m.group()[:80]}")

# 搜索free.aliyun
for m in re.finditer(r"free\.aliyun[^'\"]{0,50}", content):
    print(f"FREE: {m.group()}")

# 搜索copaw相关
idx = content.find("copaw")
if idx > 0:
    print(f"COPAW found at {idx}: {content[idx-50:idx+50]}")
else:
    # 搜索solution/tech-solution
    idx2 = content.find("tech-solution")
    if idx2 > 0:
        print(f"tech-solution at {idx2}: {content[idx2-100:idx2+100]}")

# 搜索Claw数据中的阿里
for m in re.finditer(r"name:'[^']*'[^}]*aliyun[^}]*}", content):
    print(f"\nCLAW ENTRY: {m.group()[:200]}")
