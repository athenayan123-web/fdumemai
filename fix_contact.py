# -*- coding: utf-8 -*-
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 在body结束前添加内容建议区块
old_body_end = '<!-- ===== 底栏 ===== -->'
new_body_end = '''  <!-- ===== 内容建议/技术支持 ===== -->
  <div style="text-align:center;padding:40px 20px;background:var(--card);border-top:1px solid var(--border)">
    <div style="font-size:18px;font-weight:600;color:var(--text);margin-bottom:16px">💬 内容建议 / 技术支持 / 加入校友会</div>
    <div style="font-size:14px;color:var(--text2);margin-bottom:8px">微信：Aclouder</div>
    <div style="font-size:12px;color:var(--text2)">技术支持：杭州华寰科技有限责任公司 · 联系邮箱：athenayan123@gmail.com</div>
  </div>

<!-- ===== 底栏 ===== -->'''

if old_body_end in c:
    c = c.replace(old_body_end, new_body_end)
    print("内容建议区块: PASS")
else:
    print("内容建议区块: 未找到插入位置")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"验证: {'PASS' if '💬 内容建议 / 技术支持 / 加入校友会' in v else 'FAIL'}")
