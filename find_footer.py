# -*- coding: utf-8 -*-
"""修复页脚"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "rb") as f:
    raw = f.read()
c = raw.decode("utf-8")

# 搜索footer附近内容
idx = c.find("class=\"footer\"")
if idx > 0:
    print("FOOTER found at:", idx)
    print(c[idx:idx+500])
else:
    # 搜索页脚关键词
    for kw in ["仅供参考", "校友会", "技术支持", "杭州华寰"]:
        idx2 = c.find(kw)
        if idx2 > 0:
            print(f"\n'{kw}' at {idx2}:")
            print(c[max(0,idx2-100):idx2+200])
