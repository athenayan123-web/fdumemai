# -*- coding: utf-8 -*-
"""
在模型API表格下方添加选型建议速查表
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 在模型API section的表格后、section结束前插入选型表
# 找到api-tbody所在table的结束标签
api_table_end = c.find("</table>", c.find("api-tbody"))
if api_table_end == -1:
    print("FAIL: api-tbody table not found")
    exit()

# 找到这个table后的</div>
next_div_end = c.find("</div>", api_table_end)

guide_html = """
    <!-- 选型建议速查表 -->
    <div style="margin-top:32px">
      <h3 style="font-size:18px;margin-bottom:16px;display:flex;align-items:center;gap:8px">
        <span style="font-size:24px">🎯</span> 快速选型建议速查表
      </h3>
      <div class="table-wrap" style="border-radius:var(--r);overflow:hidden;border:1px solid var(--border)">
        <table style="width:100%;border-collapse:collapse">
          <thead>
            <tr style="background:linear-gradient(135deg,#f093fb,#f5576c)">
              <th style="padding:12px 16px;text-align:left;color:#fff;font-weight:600;font-size:13px">你的需求</th>
              <th style="padding:12px 16px;text-align:left;color:#fff;font-weight:600;font-size:13px">首选模型</th>
              <th style="padding:12px 16px;text-align:left;color:#fff;font-weight:600;font-size:13px">备选</th>
              <th style="padding:12px 16px;text-align:left;color:#fff;font-weight:600;font-size:13px">月预估成本</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border)">
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">💰 完全免费</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">Gemini 2.0 Flash</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text)">Gemini 2.5 Flash-Lite</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--green);font-size:14px">$0</td>
            </tr>
            <tr style="background:rgba(255,255,255,.02);border-bottom:1px solid var(--border)">
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">💬 日常聊天问答</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">Gemini 2.5 Flash-Lite</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text)">GPT-4.1 Nano</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--green);font-size:14px">$3-5</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border)">
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">💻 代码辅助</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">Claude Sonnet 4</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text)">GPT-4.1 Mini</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--orange);font-size:14px">$15-25</td>
            </tr>
            <tr style="background:rgba(255,255,255,.02);border-bottom:1px solid var(--border)">
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">📄 长文档处理</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">Gemini 2.5 Pro</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text)">GPT-4.1 Mini</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--orange);font-size:14px">$10-18</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border)">
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">🔧 复杂重构</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">Claude Opus 4</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text)">GPT-5.4</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--red);font-size:14px">$30-50</td>
            </tr>
            <tr style="background:rgba(255,255,255,.02);border-bottom:1px solid var(--border)">
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">🖥️ 计算机操作</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">GPT-5.4</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text2)">-</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--text2);font-size:14px">按需</td>
            </tr>
            <tr>
              <td style="padding:12px 16px;font-size:13px;font-weight:600;color:var(--text)">🇨🇳 中文优化</td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;font-weight:600;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff">Qwen3-Max</span></td>
              <td style="padding:12px 16px"><span style="display:inline-block;padding:3px 10px;border-radius:12px;font-size:12px;background:var(--card2);color:var(--text)">DeepSeek V3</span></td>
              <td style="padding:12px 16px;font-family:Consolas,monospace;font-weight:700;color:var(--green);font-size:14px">&yen;10-20</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div style="margin-top:12px;padding:10px 16px;background:rgba(255,171,64,.08);border-left:3px solid var(--orange);border-radius:0 var(--r) var(--r) 0;font-size:12px;color:var(--text2)">
        💡 成本估算基于标准API调用频率（每日10万tokens），实际费用因使用模式而异。数据来源：各厂商官网。
      </div>
    </div>"""

# 插入位置：在api表格的</table>后，</div>前
insert_pos = api_table_end + len("</table>")
c = c[:insert_pos] + guide_html + c[insert_pos:]

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

checks = {
    "选型速查表标题": "快速选型建议速查表" in v,
    "完全免费行": "完全免费" in v,
    "日常聊天行": "日常聊天问答" in v,
    "代码辅助行": "代码辅助" in v,
    "长文档处理行": "长文档处理" in v,
    "复杂重构行": "复杂重构" in v,
    "计算机操作行": "计算机操作" in v,
    "中文优化行": "中文优化" in v,
    "Gemini 2.0 Flash": "Gemini 2.0 Flash" in v,
    "Claude Sonnet 4": "Claude Sonnet 4" in v,
    "Qwen3-Max": "Qwen3-Max" in v,
    "成本提示": "成本估算基于标准API" in v,
}

print("=" * 50)
print("选型建议速查表验证")
print("=" * 50)
all_pass = True
for name, ok in checks.items():
    print(f"  {'PASS' if ok else 'FAIL'} {name}")
    if not ok: all_pass = False
print(f"\n{'ALL PASS' if all_pass else 'SOME FAILED'}")
