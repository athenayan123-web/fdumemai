# -*- coding: utf-8 -*-
"""
1. OpenAI官网链接改为 https://openai.com/zh-Hans-CN/
2. 去除商汤小浣熊"相关文章"链接
"""
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 1. OpenAI链接替换
old_openai = "https://platform.openai.com/docs/api-reference"
new_openai = "https://openai.com/zh-Hans-CN/"
count1 = c.count(old_openai)
c = c.replace(old_openai, new_openai)
print(f"[1] OpenAI链接: 替换{count1}处 -> {new_openai}")

# 2. 去除商汤小浣熊的wechat字段
# 找到商汤小浣熊那行，去掉wechat属性
lines = c.split("\n")
for i, line in enumerate(lines):
    if "商汤小浣熊" in line and "wechat:" in line:
        # 移除 ,wechat:'...' 部分
        new_line = re.sub(r",wechat:'[^']*'", "", line)
        lines[i] = new_line
        print(f"[2] 商汤小浣熊: 移除wechat字段")
        print(f"    旧: {line[:100]}...")
        print(f"    新: {new_line[:100]}...")
        break
else:
    print("[2] 商汤小浣熊wechat: 未找到，检查渲染函数")

c = "\n".join(lines)

# 3. 检查渲染函数中wechatHTML是否还会显示（如果数据没有wechat字段就不会显示）
if "c.wechat" in c:
    print("[3] 渲染函数中有c.wechat判断，数据无wechat字段则不显示，无需修改")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print(f"\n=== 验证 ===")
print(f"OpenAI新链接: {'PASS' if new_openai in v else 'FAIL'} ({v.count(new_openai)}处)")
print(f"OpenAI旧链接: {'PASS' if old_openai not in v else 'FAIL (仍存在!)'}")

# 检查商汤小浣熊是否还有wechat
shangtang_lines = [l for l in v.split("\n") if "商汤小浣熊" in l]
for sl in shangtang_lines:
    has_wechat = "wechat:" in sl
    print(f"商汤小浣熊wechat: {'FAIL (仍存在!)' if has_wechat else 'PASS (已移除)'}")
