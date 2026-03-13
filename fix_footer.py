# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

old = """  <div>© 2025 复旦大学未来信息创新学院工程管理校友会</div>

  <div><a href="index_v2_backup.html" style="color:var(--text2)">返回原版平台 →</a></div>"""

new = """  <div>© 2025 复旦大学未来信息创新学院工程管理校友会</div>
  <div style="margin-top:8px;font-size:12px;color:var(--text2)">内容建议 / 技术支持 / 加入我们（微信：Aclouder）</div>
  <div><a href="index_v2_backup.html" style="color:var(--text2)">返回原版平台 →</a></div>"""

if old in c:
    c = c.replace(old, new)
    print("PASS: 页脚已添加")
else:
    print("FAIL: 未匹配")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"验证 Aclouder: {'PASS' if 'Aclouder' in v else 'FAIL'}")
print(f"验证 内容建议: {'PASS' if '内容建议' in v else 'FAIL'}")
