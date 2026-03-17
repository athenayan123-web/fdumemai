# -*- coding: utf-8 -*-
"""
价格趋势分析页面修改 - v3.14.0
1. 标题改为"我们自己的AI实战案例"
2. 添加上线时间：2026年3月17日周一
3. 取消权限设置（移除"登录可见"注释）
4. 更新所有相关引用
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

results = []

# 1. 修改导航栏
old_nav = '<a onclick="switchSection(\'trends\')">价格趋势</a>'
new_nav = '<a onclick="switchSection(\'trends\')">AI实战案例</a>'
if old_nav in c:
    c = c.replace(old_nav, new_nav)
    results.append("[1] 导航栏：价格趋势 → AI实战案例")

# 2. 修改Hero标签
old_hero = '<div class="tab" onclick="switchSection(\'trends\')">📈 价格趋势</div>'
new_hero = '<div class="tab" onclick="switchSection(\'trends\')">📈 AI实战案例</div>'
if old_hero in c:
    c = c.replace(old_hero, new_hero)
    results.append("[2] Hero标签：📈 价格趋势 → 📈 AI实战案例")

# 3. 修改section-trends标题和添加时间
old_section = '''<!-- ===== 历史价格趋势（登录可见） ===== -->
  <div class="compare-section" id="section-trends">
    <div class="section-header">

      <h2>📈 价格趋势分析</h2>'''

new_section = '''<!-- ===== 我们自己的AI实战案例 ===== -->
  <div class="compare-section" id="section-trends">
    <div class="section-header">
      <h2>📈 我们自己的AI实战案例</h2>
      <p style="color:var(--accent);font-size:14px;margin-top:6px">🎉 全新上线 · 上线时间：2026年3月17日周一</p>
      <p style="color:var(--text2);font-size:13px;margin-top:4px">Claw AI 团队真实项目落地经验分享</p>'''

if old_section in c:
    c = c.replace(old_section, new_section)
    results.append("[3] section-trends：价格趋势分析 → AI实战案例 + 上线时间")
else:
    results.append("[3] ERROR: 未找到section-trends")

# 4. 移除"登录可见"文字（如果还有其他地方）
c = c.replace("（登录可见）", "")
results.append("[4] 移除'登录可见'标记")

# 5. 更新switchSection中的文本判断
old_switch = "(id === 'trends' && a.textContent === '价格趋势')"
new_switch = "(id === 'trends' && (a.textContent === 'AI实战案例' || a.textContent === '价格趋势'))"
if old_switch in c:
    c = c.replace(old_switch, new_switch)
    results.append("[5] switchSection判断已更新")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 验证 =====
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print("=" * 60)
print("价格趋势分析页面修改结果")
print("=" * 60)
for r in results:
    print(f"  {r}")
print("=" * 60)
print(f"验证 AI实战案例: {'PASS' if 'AI实战案例' in v else 'FAIL'}")
print(f"验证 上线时间2026: {'PASS' if '2026年3月17日' in v else 'FAIL'}")
print(f"验证 无登录可见: {'PASS' if '（登录可见）' not in v else 'FAIL'}")
print(f"验证 无价格趋势: {'PASS' if '价格趋势' not in v else 'FAIL (仍有残留)'}")
print(f"总计: {'PASS' if 'AI实战案例' in v and '2026年3月17日' in v else 'FAIL'}")
