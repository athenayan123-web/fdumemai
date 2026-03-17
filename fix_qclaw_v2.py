# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. 去除trends-content中的上线时间
old = "AI实战案例集即将上线，敬请期待！上线时间：2026年3月17日周一"
new = "AI实战案例集即将上线，敬请期待！"
if old in c:
    c = c.replace(old, new)
    print("PASS [1]: 上线时间已移除")

# 2. 在H3C盒装大龙虾后添加QClaw
old_h3c = "name:'H3C盒装大龙虾'"
idx = c.find(old_h3c)
if idx > 0:
    end_line = c.find("\n", idx)
    qclaw = "\n  {name:'QClaw',icon:'🐾',desc:'QClaw智能编程助手，支持多模型切换，代码补全与智能对话',url:'https://qclawd.com/#features',doc:'https://qclawd.com/#features',open:false,hot:true},"
    c = c[:end_line] + qclaw + c[end_line:]
    print("PASS [2]: QClaw已添加（H3C后）")
else:
    print("FAIL [2]: H3C未找到")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 上线时间: {'PASS' if '2026年3月17日' not in v else 'FAIL'}")
print(f"验证 QClaw: {'PASS' if 'qclawd.com' in v else 'FAIL'}")
