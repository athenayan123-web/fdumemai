# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 去除内容建议区块
old_block = '''  <!-- ===== 内容建议/技术支持 ===== -->
  <div style="text-align:center;padding:40px 20px;background:var(--card);border-top:1px solid var(--border)">
    <div style="font-size:18px;font-weight:600;color:var(--text);margin-bottom:16px">💬 内容建议 / 技术支持 / 加入校友会</div>
    <div style="font-size:14px;color:var(--text2);margin-bottom:8px">微信：Aclouder</div>
    <div style="font-size:12px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>
  </div>

'''

if old_block in c:
    c = c.replace(old_block, '')
    print("PASS: 已去除内容建议区块")
else:
    print("FAIL: 未找到内容建议区块")

# 去除页脚中的技术支持信息
old_footer = '  <div style="margin-top:4px;font-size:10px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>\n'
if old_footer in c:
    c = c.replace(old_footer, '')
    print("PASS: 已去除页脚技术支持信息")
else:
    print("SKIP: 页脚技术支持信息不存在")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print(f"\n验证 内容建议: {'PASS' if '💬 内容建议' not in v else 'FAIL (仍存在)'}")
print(f"验证 微信Aclouder: {'PASS' if '微信：Aclouder' not in v else 'FAIL (仍存在)'}")
print(f"验证 技术支持信息: {'PASS' if '杭州华寰' not in v else 'FAIL (仍存在)'}")
print(f"验证 页脚简洁: {'PASS' if v.count('© 2026') == 1 else 'FAIL'}")
