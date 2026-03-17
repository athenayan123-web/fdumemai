# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. 修改标题
old_h2 = '<h2>📈 价格趋势分析</h2>'
new_h2 = '<h2>📈 我们自己的AI实战案例</h2>\n      <p style="color:var(--accent);font-size:14px;margin-top:6px">🎉 全新上线 · 上线时间：2026年3月17日周一</p>\n      <p style="color:var(--text2);font-size:13px;margin-top:4px">Claw AI 团队真实项目落地经验分享</p>'
if old_h2 in c:
    c = c.replace(old_h2, new_h2)
    print("PASS: 标题和上线时间已添加")
else:
    print("FAIL: 未找到标题")

# 2. 注释掉restricted-overlay的登录限制
old_restricted = '<div id="trend-content" class="restricted-overlay"'
new_restricted = '<div id="trend-content" style="display:block"'
if old_restricted in c:
    c = c.replace(old_restricted, new_restricted)
    print("PASS: 已取消登录限制")
else:
    print("FAIL: 未找到登录限制")

# 3. 移除"登录可见"的注释
old_comment = '<!-- ===== 历史价格趋势（登录可见） ===== -->'
new_comment = '<!-- ===== 我们自己的AI实战案例 ===== -->'
if old_comment in c:
    c = c.replace(old_comment, new_comment)
    print("PASS: 注释已更新")
else:
    print("FAIL: 未找到注释")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 AI实战案例: {'PASS' if 'AI实战案例' in v else 'FAIL'}")
print(f"验证 2026年3月17日: {'PASS' if '2026年3月17日' in v else 'FAIL'}")
print(f"验证 restricted移除: {'PASS' if 'restricted-overlay' not in v else 'FAIL'}")
