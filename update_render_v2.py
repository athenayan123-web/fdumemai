# -*- coding: utf-8 -*-
"""
更新renderAPITable：支持4梯队+子类分组+展开详情
"""
import re
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 找到renderAPITable函数体
idx_start = c.find("function renderAPITable()")
idx_tbody = c.find("tbody.innerHTML = html;", idx_start)

old_section = c[idx_start:idx_tbody]

new_section = """function renderAPITable() {
  const tbody = document.getElementById('api-tbody');
  let html = '';
  const tiers = [
    {id:'T1',label:'\\U0001f3c6 旗舰系列',color:'#ffd700',desc:'各厂商最强模型'},
    {id:'T2',label:'\\U0001f948 主力系列',color:'#c0c0c0',desc:'性能与成本的最佳平衡'},
    {id:'T3',label:'\\U0001f949 轻量系列',color:'#cd7f32',desc:'快速响应、极致低价'},
    {id:'T4',label:'\\U0001f52c 特化系列',color:'#e040fb',desc:'推理、数学等专项能力'}
  ];
  tiers.forEach(tier => {
    const items = API_DATA.filter(d => d.tier === tier.id);
    if (items.length === 0) return;
    html += '<tr><td colspan="7" style="background:rgba(255,255,255,.03);padding:12px 16px;font-weight:700;font-size:14px;color:' + tier.color + ';border-left:3px solid ' + tier.color + '">' + tier.label + '<span style="font-size:11px;color:var(--text2);margin-left:8px;font-weight:400">' + items.length + '\\u6b3e \\u00b7 ' + tier.desc + '</span></td></tr>';
    // 按子类分组
    const subs = [...new Set(items.map(d => d.sub))];
    subs.forEach(sub => {
      const subItems = items.filter(d => d.sub === sub);
      if (subs.length > 1) {
        html += '<tr><td colspan="7" style="padding:6px 16px 4px 28px;font-size:11px;color:var(--text2);font-weight:600;letter-spacing:1px">' + sub + '</td></tr>';
      }
      subItems.forEach(d => {
        const tagHTML = d.tag === 'hot' ? '<span class="tag tag-hot">\\U0001f525 \\u70ed\\u95e8</span>' :
                        d.tag === 'new' ? '<span class="tag tag-new">\\u2728 \\u65b0</span>' :
                        d.tag === 'low' ? '<span class="tag tag-low">\\U0001f4b0 \\u4f4e\\u4ef7</span>' : '';
        const regionTag = d.region === '\\u56fd\\u9645' ? '<span class="tag tag-intl">\\u56fd\\u9645</span>' : '<span class="tag tag-cn">\\u56fd\\u5185</span>';
        const featHTML = d.features ? '<div style="font-size:10px;color:var(--text2);margin-top:2px;max-width:200px">' + d.features + '</div>' : '';
        const benchHTML = d.bench ? '<div style="font-size:9px;color:var(--accent);margin-top:2px;opacity:.7">\\U0001f4ca ' + d.bench + '</div>' : '';
        html += '<tr>' +
          '<td><div class="provider-cell"><div class="provider-logo">' + d.logo + '</div>' + d.provider + '</div></td>' +
          '<td>' + d.model + ' ' + tagHTML + featHTML + benchHTML + '</td>' +
          '<td class="price-cell">' + d.input + '</td>' +
          '<td class="price-cell">' + d.output + '</td>' +
          '<td>' + d.context + '</td>' +
          '<td>' + regionTag + '</td>' +
          '<td><a class="btn-reg" href="' + d.url + '" target="_blank">\\u5b98\\u7f51\\u6ce8\\u518c \\u2192</a></td>' +
          '</tr>';
      });
    });
  });
  """

c = c[:idx_start] + new_section + c[idx_tbody:]

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"旗舰系列: {'PASS' if '旗舰系列' in v else 'FAIL'}")
print(f"主力系列: {'PASS' if '主力系列' in v else 'FAIL'}")
print(f"轻量系列: {'PASS' if '轻量系列' in v else 'FAIL'}")
print(f"特化系列: {'PASS' if '特化系列' in v else 'FAIL'}")
print(f"子类分组: {'PASS' if 'sub' in v else 'FAIL'}")
print(f"bench显示: {'PASS' if 'benchHTML' in v else 'FAIL'}")
