# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 使用简单替换
replacements = [
    ("<th>产品</th>", "<th>产品名称<br><span style=\"font-size:10px;font-weight:400\">官方名称</span></th>"),
    ("<th>计划</th>", "<th>目标用户<br><span style=\"font-size:10px;font-weight:400\">定价模式</span></th>"),
    ("<th>月费</th>", "<th>月费/资源包价格</th>"),
    ("<th>核心功能</th>", "<th>核心功能/价值主张</th>"),
    ("<th>区域</th>", "<th>典型应用场景<br><span style=\"font-size:10px;font-weight:400\">区域</span></th>"),
]

for old, new in replacements:
    if old in c:
        c = c.replace(old, new)
        print(f"PASS: {old} -> {new[:30]}...")
    else:
        print(f"SKIP: {old} not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 产品名称: {'PASS' if '产品名称' in v else 'FAIL'}")
print(f"验证 目标用户: {'PASS' if '目标用户' in v else 'FAIL'}")
