# -*- coding: utf-8 -*-
"""
最终修复：
1. 删除"我们自己的AI实战案例"文字图标
2. 去重"注册后解锁"提示（只保留1次）
3. 确认页脚显示Claw AI智能助手平台
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. 删除"我们自己的AI实战案例"标题
old_title = '<h2>📈 我们自己的AI实战案例</h2>'
new_title = '<h2>📈 AI实战案例</h2>'
if old_title in c:
    c = c.replace(old_title, new_title)
    print("PASS [1]: 标题简化为'AI实战案例'")

# 2. 统计"注册后解锁复旦大学百万SKILLS和实战案例集"出现次数
lock_text = "注册后解锁复旦大学百万SKILLS和实战案例集"
count = c.count(lock_text)
print(f"INFO [2]: '{lock_text}' 出现 {count} 次")

if count > 1:
    # 只保留第一次出现，后续替换为简短版
    first_idx = c.find(lock_text)
    # 从第二次出现开始替换
    second_idx = c.find(lock_text, first_idx + len(lock_text))
    while second_idx > 0:
        # 替换为简短版
        c = c[:second_idx] + "注册后解锁全部内容" + c[second_idx + len(lock_text):]
        second_idx = c.find(lock_text, second_idx + 10)
    print(f"PASS [2]: 去重完成，保留1次完整提示")

# 3. 确认页脚
if "Claw AI 智能助手平台" in c:
    print("PASS [3]: 页脚已显示'Claw AI 智能助手平台'")
else:
    print("FAIL [3]: 页脚未找到")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 最终验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print(f"\n=== 最终验证 ===")
print(f"'我们自己的' 已移除: {'PASS' if '我们自己的' not in v else 'FAIL'}")
print(f"'AI实战案例' 存在: {'PASS' if 'AI实战案例' in v else 'FAIL'}")
print(f"完整锁定提示出现次数: {v.count(lock_text)}")
print(f"trends-locked存在: {'PASS' if 'trends-locked' in v else 'FAIL'}")
print(f"skills-locked存在: {'PASS' if 'skills-locked' in v else 'FAIL'}")
print(f"页脚Claw AI: {'PASS' if 'Claw AI 智能助手平台' in v else 'FAIL'}")
