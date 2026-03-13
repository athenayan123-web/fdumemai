# -*- coding: utf-8 -*-
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 查找并替换页脚
old = "  <div>© 2026 Claw AI 智能助手平台 · 复旦大学未来信息创新学院工程管理校友会</div>"
new = "  <div>© 2026 Claw AI 智能助手平台 · 复旦大学未来信息创新学院工程管理校友会</div>\n  <div style=\"margin-top:8px;font-size:12px;color:var(--text2)\">内容建议 / 技术支持 / 加入校友会（微信：Aclouder）</div>"
if old in c:
    c = c.replace(old, new)
    print("页脚: PASS")
else:
    print("页脚: 未找到")

# 查找并替换SKILLS
old2 = '<h2>📚 复旦大学百万SKILLS</h2>'
new2 = '<h2>📚 复旦大学百万SKILLS</h2>\n      <p style="color:var(--accent);font-size:13px">复旦大学科研武器库 · 肖仰华团队DataHub平台 · 百万计SKILLS资源库</p>'
if old2 in c:
    c = c.replace(old2, new2)
    print("SKILLS: PASS")
else:
    print("SKILLS: 未找到")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 加入校友会: {'PASS' if '加入校友会' in v else 'FAIL'}")
print(f"验证 科研武器库: {'PASS' if '科研武器库' in v else 'FAIL'}")
