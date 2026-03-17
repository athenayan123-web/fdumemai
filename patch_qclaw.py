# -*- coding: utf-8 -*-
"""
1. AI实战案例去除"上线时间：2026年3月17日周一"
2. Claw集增加QClaw https://qclawd.com/#features
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. 去除上线时间
old_time = '<p style="color:var(--accent);font-size:14px;margin-top:6px">🎉 全新上线 · 上线时间：2026年3月17日周一</p>'
if old_time in c:
    c = c.replace(old_time, '')
    print("PASS [1]: 已去除上线时间")
else:
    print("FAIL [1]: 未找到上线时间")

# 2. Claw集增加QClaw
# 在飞书龙虾之前插入
lines = c.split("\n")
inserted = False
for i, line in enumerate(lines):
    if "飞书龙虾" in line and "name:" in line:
        qclaw_line = "  {name:'QClaw',icon:'🐾',desc:'QClaw智能编程助手，支持多模型切换，代码补全与智能对话',url:'https://qclawd.com/#features',doc:'https://qclawd.com/#features',open:false,hot:true},"
        lines.insert(i, qclaw_line)
        inserted = True
        print("PASS [2]: QClaw已添加")
        break

if not inserted:
    print("FAIL [2]: 未找到插入位置")

c = "\n".join(lines)

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 上线时间已移除: {'PASS' if '2026年3月17日' not in v else 'FAIL'}")
print(f"验证 QClaw: {'PASS' if 'qclawd.com' in v else 'FAIL'}")
