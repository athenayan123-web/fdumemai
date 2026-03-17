# -*- coding: utf-8 -*-
"""
精确修复：在section-trends中添加锁定遮罩 + 更新updateSkillsVisibility
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. 在trend-content前添加锁定遮罩，trend-content改为默认隐藏
old_trend = """    </div>

    <div id="trend-content" style="display:block" style="display:block" style="min-height:200px;background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:40px;text-align:center">

      <p style="color:var(--text2);font-size:14px">登录后可查看各厂商历史价格走势、降价预测与性价比排名</p>

    </div>

  </div>"""

new_trend = """    </div>
    <!-- 未登录锁定遮罩 -->
    <div id="trends-locked" style="text-align:center;padding:60px 20px;background:var(--card);border:1px solid var(--border);border-radius:var(--r)">
      <div style="font-size:64px;margin-bottom:20px">🔒</div>
      <h3 style="margin-bottom:12px;font-size:20px;color:var(--text)">注册后解锁复旦大学百万SKILLS和实战案例集</h3>
      <p style="color:var(--text2);margin-bottom:24px;font-size:14px;max-width:400px;margin-left:auto;margin-right:auto">注册即可免费访问AI实战案例集和全部技能库</p>
      <div style="display:flex;gap:12px;justify-content:center">
        <button onclick="openModal('modal-register')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;cursor:pointer;font-weight:700">免费注册</button>
        <button onclick="openModal('modal-login')" style="padding:10px 32px;font-size:15px;border-radius:10px;background:transparent;color:var(--accent);border:1px solid rgba(102,126,234,.4);cursor:pointer;font-weight:700">已有账号登录</button>
      </div>
    </div>
    <!-- 已登录内容（默认隐藏） -->
    <div id="trends-content" style="display:none;min-height:200px;background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:40px;text-align:center">
      <p style="color:var(--text2);font-size:14px">AI实战案例集即将上线，敬请期待！上线时间：2026年3月17日周一</p>
    </div>
  </div>"""

if old_trend in c:
    c = c.replace(old_trend, new_trend)
    print("PASS: trends锁定遮罩已添加")
else:
    print("FAIL: 未找到trend-content区域")

# 2. 更新updateSkillsVisibility函数
old_func = "function updateSkillsVisibility() {"
idx = c.find(old_func)
if idx > 0:
    # 找到函数结束的}
    brace_count = 0
    func_end = idx
    started = False
    for i in range(idx, len(c)):
        if c[i] == '{':
            brace_count += 1
            started = True
        elif c[i] == '}':
            brace_count -= 1
            if started and brace_count == 0:
                func_end = i + 1
                break
    
    old_full_func = c[idx:func_end]
    
    new_full_func = """function updateSkillsVisibility() {
  var locked = document.getElementById('skills-locked');
  var content = document.getElementById('skills-content');
  if (locked && content) {
    if (user) { locked.style.display='none'; content.style.display='block'; }
    else { locked.style.display='block'; content.style.display='none'; }
  }
  var trendsLocked = document.getElementById('trends-locked');
  var trendsContent = document.getElementById('trends-content');
  if (trendsLocked && trendsContent) {
    if (user) { trendsLocked.style.display='none'; trendsContent.style.display='block'; }
    else { trendsLocked.style.display='block'; trendsContent.style.display='none'; }
  }
}"""
    
    c = c[:idx] + new_full_func + c[func_end:]
    print("PASS: updateSkillsVisibility已更新（含trends锁定）")
else:
    print("FAIL: 未找到updateSkillsVisibility函数")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"\n验证 trends-locked: {'PASS' if 'trends-locked' in v else 'FAIL'}")
print(f"验证 trends-content: {'PASS' if 'trends-content' in v else 'FAIL'}")
print(f"验证 trendsLocked: {'PASS' if 'trendsLocked' in v else 'FAIL'}")
print(f"验证 页脚: {'PASS' if 'Claw AI 智能助手平台' in v else 'FAIL'}")
print(f"验证 SKILLS+实战案例提示: {'PASS' if '百万SKILLS和实战案例集' in v else 'FAIL'}")
