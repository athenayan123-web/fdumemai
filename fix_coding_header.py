# -*- coding: utf-8 -*-
"""
修复 Coding Plan 表格表头
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 查找并替换表头
old_header = """<th>产品</th>
            <th>计划</th>
            <th>月费</th>
            <th>年费(折合月)</th>
            <th>核心功能</th>
            <th>区域</th>
            <th>操作</th>"""

new_header = """<th>产品名称<br><span style="font-size:10px;font-weight:400">官方名称</span></th>
            <th>目标用户<br><span style="font-size:10px;font-weight:400">定价模式</span></th>
            <th>月费/资源包价格</th>
            <th>年费(折合月)</th>
            <th>核心功能/价值主张</th>
            <th>典型应用场景<br><span style="font-size:10px;font-weight:400">区域</span></th>
            <th>操作</th>"""

if old_header in c:
    c = c.replace(old_header, new_header)
    print("PASS: 表头已更新")
else:
    print("FAIL: 未找到旧表头")
    # 尝试查找简化版本
    simple_old = "<th>产品</th>"
    if simple_old in c:
        print("找到简化表头，需要手动检查")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"验证: {'PASS' if '产品名称' in v else 'FAIL'}")
