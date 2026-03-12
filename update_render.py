# -*- coding: utf-8 -*-
"""
更新renderAPITable函数：按梯队分组显示
"""
path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

old_render = """function renderAPITable() {
  const tbody = document.getElementById('api-tbody');
  let html = '';
  // 按输出价格升序排列
  const sortedData = [...API_DATA].sort((a, b) => {
    const priceA = parseFloat(a.output.replace(/[^0-9.]/g, '')) || 0;
    const priceB = parseFloat(b.output.replace(/[^0-9.]/g, '')) || 0;
    return priceA - priceB;
  });
  sortedData.forEach(d => {
    const isBlur = !user && d.region === '国际';
    const tagHTML = d.tag === 'hot' ? '<span class="tag tag-hot">🔥 热门</span>' :
                    d.tag === 'new' ? '<span class="tag tag-new">✨ 新</span>' :
                    d.tag === 'low' ? '<span class="tag tag-low">💰 低价</span>' : '';
    const regionTag = d.region === '国际' ? '<span class="tag tag-intl">国际</span>' : '<span class="tag tag-cn">国内</span>';
    html += `<tr>
      <td><div class="provider-cell"><div class="provider-logo">${d.logo}</div>${d.provider}</div></td>
      <td>${d.model} ${tagHTML}</td>
      <td class="price-cell ${isBlur ? 'blur' : ''}" ${isBlur ? 'onclick="openModal(\\'modal-restricted\\')"' : ''}>${d.input}</td>
      <td class="price-cell ${isBlur ? 'blur' : ''}" ${isBlur ? 'onclick="openModal(\\'modal-restricted\\')"' : ''}>${d.output}</td>
      <td>${d.context}</td>
      <td>${regionTag}</td>
      <td><a class="btn-reg" href="${d.url}" target="_blank">官网注册 →</a></td>
    </tr>`;
  });"""

new_render = """function renderAPITable() {
  const tbody = document.getElementById('api-tbody');
  let html = '';
  const tiers = [
    {id:'T1',label:'🏆 第一梯队（顶级旗舰）',color:'#ffd700'},
    {id:'T2',label:'🥈 第二梯队（高性价比主力）',color:'#c0c0c0'},
    {id:'T3',label:'🥉 第三梯队（轻量/特化）',color:'#cd7f32'}
  ];
  tiers.forEach(tier => {
    const items = API_DATA.filter(d => d.tier === tier.id);
    if (items.length === 0) return;
    html += `<tr><td colspan="7" style="background:rgba(255,255,255,.03);padding:10px 16px;font-weight:700;font-size:14px;color:${tier.color};border-left:3px solid ${tier.color}">${tier.label}<span style="font-size:11px;color:var(--text2);margin-left:8px;font-weight:400">${items.length}款</span></td></tr>`;
    items.forEach(d => {
      const tagHTML = d.tag === 'hot' ? '<span class="tag tag-hot">🔥 热门</span>' :
                      d.tag === 'new' ? '<span class="tag tag-new">✨ 新</span>' :
                      d.tag === 'low' ? '<span class="tag tag-low">💰 低价</span>' : '';
      const regionTag = d.region === '国际' ? '<span class="tag tag-intl">国际</span>' : '<span class="tag tag-cn">国内</span>';
      const featHTML = d.features ? `<div style="font-size:10px;color:var(--text2);margin-top:2px">${d.features}</div>` : '';
      html += `<tr>
        <td><div class="provider-cell"><div class="provider-logo">${d.logo}</div>${d.provider}</div></td>
        <td>${d.model} ${tagHTML}${featHTML}</td>
        <td class="price-cell">${d.input}</td>
        <td class="price-cell">${d.output}</td>
        <td>${d.context}</td>
        <td>${regionTag}</td>
        <td><a class="btn-reg" href="${d.url}" target="_blank">官网注册 →</a></td>
      </tr>`;
    });
  });"""

if old_render in c:
    c = c.replace(old_render, new_render)
    print("PASS: renderAPITable已更新（梯队分组）")
else:
    print("FAIL: 未找到旧renderAPITable，尝试备用匹配")
    # 备用：只替换函数开头到forEach结束
    idx_start = c.find("function renderAPITable()")
    if idx_start > 0:
        # 找到 sortedData.forEach 或 API_DATA.forEach 的结束
        # 简单方式：找到 });  后面跟着 tbody.innerHTML
        idx_tbody = c.find("tbody.innerHTML = html;", idx_start)
        if idx_tbody > 0:
            # 从函数开头到 tbody.innerHTML 之前
            old_section = c[idx_start:idx_tbody]
            new_section = new_render + "\n  "
            c = c[:idx_start] + new_section + c[idx_tbody:]
            print("PASS: 备用方案替换成功")
        else:
            print("FAIL: 备用方案也失败")

with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# 验证
with open(path, "r", encoding="utf-8") as f:
    v = f.read()
print(f"验证 梯队分组: {'PASS' if '第一梯队' in v and '第二梯队' in v and '第三梯队' in v else 'FAIL'}")
print(f"验证 features显示: {'PASS' if 'featHTML' in v else 'FAIL'}")
