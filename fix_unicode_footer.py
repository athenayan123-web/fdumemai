# -*- coding: utf-8 -*-
"""
修复：
1. 去除Unicode转义字符，使用实际emoji
2. 修复页脚重复问题
3. 将"内容建议/技术支持"移到正文后面
4. 页脚只显示版权信息
"""
import re

path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

results = []

# ===== 1. 修复页脚重复问题 =====
# 查找所有页脚相关内容并清理
# 移除旧的页脚行
old_footer1 = '  <div style="margin-top:8px;font-size:12px;color:var(--text2)">内容建议 / 技术支持 / 加入校友会（微信：Aclouder）</div>'
old_footer2 = '  <div style="margin-top:4px;font-size:10px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>'

if old_footer1 in c:
    c = c.replace(old_footer1, '')
    results.append("[1] 移除旧页脚行1")

if old_footer2 in c:
    c = c.replace(old_footer2, '')
    results.append("[1] 移除旧页脚行2")

# 设置简洁页脚
old_copyright = '  <div>© 2026 Claw AI 智能助手平台 · 复旦大学未来信息创新学院工程管理校友会</div>'
new_copyright = '  <div>© 2026 Claw AI 智能助手平台</div>'

if old_copyright in c:
    c = c.replace(old_copyright, new_copyright)
    results.append("[1] 页脚简化为版权信息")

# ===== 2. 在正文后面添加内容建议/技术支持（在</div>之前） =====
# 找到最后一个section之后，footer之前添加
old_end = '<!-- ===== 底栏 ===== -->\n<div class="footer">'
new_end = '''  <!-- ===== 内容建议/技术支持 ===== -->
  <div style="text-align:center;padding:40px 20px;background:var(--card);border-top:1px solid var(--border)">
    <div style="font-size:18px;font-weight:600;color:var(--text);margin-bottom:16px">💬 内容建议 / 技术支持 / 加入校友会</div>
    <div style="font-size:14px;color:var(--text2);margin-bottom:8px">微信：Aclouder</div>
    <div style="font-size:12px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>
  </div>

<!-- ===== 底栏 ===== -->
<div class="footer">'''

if old_end in c:
    c = c.replace(old_end, new_end)
    results.append("[2] 内容建议/技术支持已移到正文后面")

# ===== 3. 去除Unicode转义字符 =====
# 查找所有 \\uXXXX 并替换为实际字符
import codecs

def decode_unicode_escape(match):
    try:
        return codecs.decode(match.group(0), 'unicode_escape')
    except:
        return match.group(0)

# 替换 \\uXXXX 格式的转义
pattern = r'\\u[0-9a-fA-F]{4}'
c = re.sub(pattern, decode_unicode_escape, c)
results.append("[3] Unicode转义字符已替换为实际emoji")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 验证 =====
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print("=" * 60)
print("修复结果:")
for r in results:
    print(f"  {r}")
print("=" * 60)
print(f"验证 页脚简洁: {'PASS' if v.count('© 2026') == 1 else 'FAIL'}")
print(f"验证 内容建议区块: {'PASS' if '内容建议 / 技术支持 / 加入校友会' in v else 'FAIL'}")
print(f"验证 微信Aclouder: {'PASS' if '微信：Aclouder' in v else 'FAIL'}")
print(f"验证 Unicode转义: {'PASS' if '\\u' not in v else 'FAIL (仍有转义)'}")
