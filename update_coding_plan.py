# -*- coding: utf-8 -*-
"""
更新 Coding Plan 表格为新的产品经理思维结构
"""
import re
import json

path = r"E:\智能整理\openclaw\app\index.html"
with open(path, "r", encoding="utf-8") as f:
    c = f.read()

# 读取新的 Coding Plan 数据
with open(r"E:\智能整理\openclaw\app\CODING_DATA.json", "r", encoding="utf-8") as f:
    data = json.load(f)

results = []

# ===== 1. 构建新的 CODING_DATA =====
coding_data_js = """const CODING_DATA = [

  // === AI编程助手 ===

  {product:'Claude系列',emoji:'🟠',target:'个人/企业用户',pricing:'免费/订阅制',monthly:'Free: $0 | Pro: $17 | Max: $100起',yearly:'Free: $0 | Pro: $17 | Max: $100起',features:'Free: 日常对话与轻量任务 | Pro: 优先访问、更高额度 | Max: 最高使用额度、团队协作',scenarios:'学习、日常开发、团队生产',price_page:'https://www.anthropic.com/pricing',buy_link:'https://claude.ai/',region:'国际',official_name:'Claude'},
  {product:'通义灵码',emoji:'🌐',target:'国内开发者',pricing:'免费',monthly:'免费',yearly:'免费',features:'Qwen驱动，代码补全、单元测试生成',scenarios:'国内开发者入门',price_page:'https://tongyi.aliyun.com/lingma',buy_link:'https://tongyi.aliyun.com/lingma',region:'国内',official_name:'通义灵码'},
  {product:'Trae',emoji:'🔥',target:'国内开发者',pricing:'免费',monthly:'免费',yearly:'免费',features:'字节出品、AI原生IDE，免费GPT-4o接入',scenarios:'国内开发者入门、学习使用',price_page:'https://www.trae.ai/',buy_link:'https://www.trae.ai/',region:'国内',official_name:'Trae'},
  {product:'MarsCode',emoji:'🚀',target:'国内开发者',pricing:'免费',monthly:'免费',yearly:'免费',features:'豆包驱动，AI补全、Chat交互',scenarios:'国内开发者入门',price_page:'https://www.marscode.com/',buy_link:'https://www.marscode.com/',region:'国内',official_name:'MarsCode'},
  {product:'Baidu Comate',emoji:'🐻',target:'国内开发者',pricing:'免费',monthly:'免费',yearly:'免费',features:'文心驱动，代码生成、智能补全',scenarios:'国内开发者入门',price_page:'https://comate.baidu.com/',buy_link:'https://comate.baidu.com/',region:'国内',official_name:'Baidu Comate'},
  {product:'Tencent Cloud AI Code',emoji:'🐧',target:'国内开发者',pricing:'免费',monthly:'免费',yearly:'免费',features:'混元驱动，代码补全、代码解释',scenarios:'国内开发者入门',price_page:'https://cloud.tencent.com/product/acc',buy_link:'https://console.cloud.tencent.com/acc',region:'国内',official_name:'腾讯云AI代码助手'},

  // === AI插件工具 ===

  {product:'GitHub Copilot',emoji:'🐙',target:'个人/企业开发者',pricing:'订阅制',monthly:'Individual: $10 | Business: $19',yearly:'Individual: $8.33 | Business: $19',features:'Individual: IDE插件式AI助手，多模型切换 | Business: 团队管理、IP保护',scenarios:'日常编码、企业研发',price_page:'https://github.com/features/copilot#pricing',buy_link:'https://github.com/features/copilot',region:'国际',official_name:'GitHub Copilot'},
  {product:'Windsurf',emoji:'🏄',target:'独立/技术创业者',pricing:'订阅制',monthly:'Pro: $15',yearly:'$12.50',features:'AI Flow开发体验，多模型切换、代码重构',scenarios:'轻量级开发、日常编码',price_page:'https://codeium.com/pricing',buy_link:'https://codeium.com/download',region:'国际',official_name:'Windsurf'},
  {product:'Cursor',emoji:'⚡',target:'专业开发者/团队',pricing:'订阅制',monthly:'Pro: $20 | Business: $40',yearly:'Pro: $16.67 | Business: $33.33',features:'Pro: 无限代码补全、500次快速请求 | Business: 团队协作、集中计费',scenarios:'重度编码、团队协作',price_page:'https://www.cursor.com/pricing',buy_link:'https://www.cursor.com/',region:'国际',official_name:'Cursor'},
  {product:'Augment Code',emoji:'🧩',target:'团队开发者',pricing:'订阅制',monthly:'Pro: $30',yearly:'$25',features:'全仓库上下文理解、多文件编辑、智能重构',scenarios:'大型项目维护',price_page:'https://www.augmentcode.com/pricing',buy_link:'https://www.augmentcode.com/',region:'国际',official_name:'Augment Code'},
  {product:'智谱AI GLM Coding系列',emoji:'🟣',target:'个人开发者/团队',pricing:'季度订阅制(连续包季9折，拼好模立减10%)',monthly:'Lite: ￥119/季(≈￥39.7/月) | Pro: ￥362/季(≈￥120.7/月) | Max: ￥1139/季(≈￥379.7/月)',yearly:'季度制',features:'Lite: Claude Pro的3倍用量，轻量级工作负载 | Pro: Lite的5倍用量，复杂工作负载，生成速度更快 | Max: Pro的4倍用量，海量工作负载，新模型首发升级',scenarios:'轻量开发、复杂任务、海量调用',price_page:'https://open.bigmodel.cn/pricing',buy_link:'https://open.bigmodel.cn/',region:'国内',official_name:'智谱AI'},
  {product:'Baidu Comate企业版',emoji:'🐻',target:'国内企业',pricing:'订阅制',monthly:'企业版: ¥99',yearly:'¥79',features:'ERNIE 4.0驱动，团队管理、私有部署',scenarios:'企业内部研发、数据安全',price_page:'https://comate.baidu.com/',buy_link:'https://comate.baidu.com/',region:'国内',official_name:'Baidu Comate企业版'},

  // === 云端API服务 ===

  {product:'阿里云Qwen Coding Plan',emoji:'☁️',target:'个人/专业团队',pricing:'订阅制(预付费包月)',monthly:'Lite: 首月¥7.9，次月¥20，续订¥40 | Pro: 首月¥39.9，次月¥100，续订¥200',yearly:'Lite: ¥20起 | Pro: ¥100起',features:'Lite: 四大模型打包，每月1.8万次请求 | Pro: 月9万次请求，更高额度',scenarios:'OpenClaw AI机器人、多模型切换、原型验证、生产级应用',price_page:'https://www.aliyun.com/solution/tech-solution/copaw',buy_link:'https://dashscope.aliyun.com/',region:'国内',official_name:'阿里云百炼'},
  {product:'火山引擎系列',emoji:'🔥',target:'API开发者/团队',pricing:'订阅制',monthly:'Lite Plan: ¥49 | Pro Plan: ¥199',yearly:'Lite: ¥39 | Pro: ¥169',features:'Lite: 豆包/GLM/MiniMax/Kimi基础调用 | Pro: 高级调用+团队管理，更高额度',scenarios:'轻量API调用、团队开发',price_page:'https://www.volcengine.com/product/doubao',buy_link:'https://console.volcengine.com/',region:'国内',official_name:'火山引擎'},
  {product:'月之暗面Kimi开发者',emoji:'🌙',target:'API开发者',pricing:'订阅制',monthly:'Kimi开发者: ¥59',yearly:'¥49',features:'Kimi-128K驱动，超长上下文、文档理解',scenarios:'长文本处理、文档分析',price_page:'https://platform.moonshot.cn/pricing',buy_link:'https://platform.moonshot.cn/',region:'国内',official_name:'Kimi API'},
  {product:'科大讯飞Spark资源包',emoji:'🎤',target:'个人/企业开发者',pricing:'预付费资源包(有效期1年)',monthly:'免费包: 个人20万/企业100万tokens | 简享包: ¥300/1亿 | 套餐一: ¥5,400/20亿 | 套餐二: ¥12,000/50亿 | 套餐三: ¥66,000/300亿 | 套餐四: ¥250,000/1250亿',yearly:'资源包制',features:'适用于Spark X2/Ultra/Pro/Lite全系列，资源包内用量抵扣，超量按需计费',scenarios:'中小规模应用、生产级部署、企业核心业务',price_page:'https://xinghuo.xfyun.cn/buy',buy_link:'https://console.xfyun.cn/',region:'国内',official_name:'讯飞星火API'},

];"""

# 替换 CODING_DATA
old_coding_start = c.find("const CODING_DATA = [")
old_coding_end = c.find("];", old_coding_start) + 2

if old_coding_start > 0:
    c = c[:old_coding_start] + coding_data_js + c[old_coding_end:]
    results.append("[1] CODING_DATA已更新为产品经理思维结构")
else:
    results.append("[1] ERROR: 未找到CODING_DATA")

# ===== 2. 更新表格渲染函数 =====
old_render = """function renderCodingTable() {
  const tbody = document.getElementById('coding-tbody');
  let html = '';
  // 免费在前，其余按月费升序
  const sortedCoding = [...CODING_DATA].sort((a, b) => {
    const aFree = a.monthly === '免费' ? 1 : 0;
    const bFree = b.monthly === '免费' ? 1 : 0;
    if (aFree !== bFree) return bFree - aFree;
    const aNum = parseFloat(a.monthly.replace(/[^0-9.]/g, '')) || 0;
    const bNum = parseFloat(b.monthly.replace(/[^0-9.]/g, '')) || 0;
    return aNum - bNum;
  });
  sortedCoding.forEach(d => {
    const regionTag = d.region === '国际' ? '<span class="tag tag-intl">国际</span>' : '<span class="tag tag-cn">国内</span>';
    const isFree = d.monthly === '免费';
    html += `<tr>
      <td><div class="provider-cell"><div class="provider-logo">${d.logo}</div>${d.product}</div></td>
      <td>${d.plan}</td>
      <td class="price-cell">${d.monthly}${isFree ? '' : '/月'}</td>
      <td class="price-cell">${d.yearly}${isFree ? '' : '/月'}</td>
      <td style="font-size:12px;color:var(--text2);max-width:200px">${d.features}</td>
      <td>${regionTag}</td>
      <td><a class="btn-reg" href="${d.url}" target="_blank">官网注册 →</a></td>
    </tr>`;
  });"""

new_render = """function renderCodingTable() {
  const tbody = document.getElementById('coding-tbody');
  let html = '';
  
  // 按产品类型分组
  const categories = [
    {id:'AI编程助手',label:'🤖 AI编程助手',desc:'集成代码补全、生成与智能对话的AI开发工具'},
    {id:'AI插件工具',label:'🔌 AI插件工具',desc:'IDE插件式AI编程辅助工具'},
    {id:'云端API服务',label:'☁️ 云端API服务',desc:'通过API调用大模型能力的云服务'}
  ];
  
  categories.forEach(cat => {
    const items = CODING_DATA.filter(d => {
      if (cat.id === 'AI编程助手') return ['Claude系列','通义灵码','Trae','MarsCode','Baidu Comate','Tencent Cloud AI Code'].includes(d.product);
      if (cat.id === 'AI插件工具') return ['GitHub Copilot','Windsurf','Cursor','Augment Code','智谱AI GLM Coding系列','Baidu Comate企业版'].includes(d.product);
      if (cat.id === '云端API服务') return ['阿里云Qwen Coding Plan','火山引擎系列','月之暗面Kimi开发者','科大讯飞Spark资源包'].includes(d.product);
      return false;
    });
    
    if (items.length === 0) return;
    
    // 分类标题行
    html += `<tr><td colspan="7" style="background:rgba(102,126,234,.1);padding:12px 16px;font-weight:700;font-size:14px;color:var(--accent);border-left:3px solid var(--accent)">${cat.label}<span style="font-size:11px;color:var(--text2);margin-left:8px;font-weight:400">${cat.desc}</span></td></tr>`;
    
    items.forEach(d => {
      const regionTag = d.region === '国际' ? '<span class="tag tag-intl">国际</span>' : '<span class="tag tag-cn">国内</span>';
      const isFree = d.monthly === '免费';
      const pricingBadge = isFree ? '<span class="tag tag-low">免费</span>' : '';
      
      html += `<tr>
        <td><div class="provider-cell"><div class="provider-logo" style="font-size:20px">${d.emoji}</div><div><div style="font-weight:600">${d.product}</div><div style="font-size:10px;color:var(--text2)">${d.official_name}</div></div></div></td>
        <td><div style="font-size:11px;color:var(--text2)">${d.target}</div><div style="font-size:10px;color:var(--accent)">${d.pricing}</div></td>
        <td class="price-cell">${d.monthly} ${pricingBadge}</td>
        <td class="price-cell">${d.yearly}</td>
        <td style="font-size:11px;color:var(--text2);max-width:250px"><div style="font-weight:500;color:var(--text);margin-bottom:4px">${d.features.split(' | ')[0]}</div><div>${d.features.split(' | ').slice(1).join(' | ')}</div></td>
        <td><div style="font-size:10px;color:var(--text2);margin-bottom:4px">${d.scenarios}</div>${regionTag}</td>
        <td><a class="btn-reg" href="${d.buy_link}" target="_blank" style="font-size:11px">购买 →</a><a class="btn-reg" href="${d.price_page}" target="_blank" style="font-size:10px;background:var(--card2);margin-top:4px">定价页</a></td>
      </tr>`;
    });
  });"""

if old_render in c:
    c = c.replace(old_render, new_render)
    results.append("[2] renderCodingTable已更新为产品经理思维结构")
else:
    results.append("[2] WARNING: 未找到旧renderCodingTable，使用备用方案")
    # 备用方案：找到函数并替换
    idx = c.find("function renderCodingTable()")
    if idx > 0:
        # 找到函数结束位置（tbody.innerHTML = html;）
        end_marker = "tbody.innerHTML = html;"
        end_idx = c.find(end_marker, idx)
        if end_idx > 0:
            c = c[:idx] + new_render + c[end_idx:]
            results.append("[2] renderCodingTable已更新(备用方案)")

# ===== 3. 更新表格表头 =====
old_header = """          <tr>
            <th>产品</th>
            <th>计划</th>
            <th>月费</th>
            <th>年费(折合月)</th>
            <th>核心功能</th>
            <th>区域</th>
            <th>操作</th>
          </tr>"""

new_header = """          <tr>
            <th>产品名称<br><span style="font-size:10px;font-weight:400">官方名称</span></th>
            <th>目标用户<br><span style="font-size:10px;font-weight:400">定价模式</span></th>
            <th>月费/资源包价格</th>
            <th>年费(折合月)</th>
            <th>核心功能/价值主张</th>
            <th>典型应用场景<br><span style="font-size:10px;font-weight:400">区域</span></th>
            <th>操作</th>
          </tr>"""

if old_header in c:
    c = c.replace(old_header, new_header)
    results.append("[3] 表格表头已更新")

# ===== 写入 =====
with open(path, "w", encoding="utf-8") as f:
    f.write(c)

# ===== 验证 =====
with open(path, "r", encoding="utf-8") as f:
    v = f.read()

print("=" * 60)
print("Coding Plan 更新结果:")
for r in results:
    print(f"  {r}")
print("=" * 60)
print(f"验证 AI编程助手: {'PASS' if '🤖 AI编程助手' in v else 'FAIL'}")
print(f"验证 AI插件工具: {'PASS' if '🔌 AI插件工具' in v else 'FAIL'}")
print(f"验证 云端API服务: {'PASS' if '☁️ 云端API服务' in v else 'FAIL'}")
print(f"验证 产品经理表头: {'PASS' if '目标用户' in v and '定价模式' in v else 'FAIL'}")
print(f"验证 Claude系列: {'PASS' if 'Claude系列' in v else 'FAIL'}")
print(f"验证 智谱AI GLM Coding: {'PASS' if '智谱AI GLM Coding系列' in v else 'FAIL'}")
