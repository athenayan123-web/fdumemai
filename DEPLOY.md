# OpenClaw AI 全网比价智能平台 - 部署指南

## 项目说明

本项目为**纯静态网站**，无需构建步骤，直接部署 HTML/CSS/JS 文件即可。

## 文件结构

```
openclaw/app/
├── index.html              # 原版平台（保留）
├── index_new.html          # 新版比价平台（主要）
├── crawl_pricing.py        # 数据采集脚本
├── data/
│   └── pricing_data.json   # 定价数据
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions 自动部署
├── CNAME                   # 自定义域名配置
└── README.md               # 项目说明
```

## GitHub Pages 部署步骤

### 1. 推送代码到 GitHub

已完成推送到仓库：https://github.com/athenayan123-web/openclaw-app123

### 2. 启用 GitHub Pages

1. 进入仓库 Settings → Pages
2. Source 选择：**GitHub Actions**（不是 Deploy from a branch）
3. 保存后会自动触发部署

### 3. 配置自定义域名（可选）

1. 在 Settings → Pages → Custom domain 输入：`fdumemai.com`
2. 勾选 **Enforce HTTPS**
3. 在域名服务商处添加 DNS 记录：
   ```
   类型: CNAME
   主机记录: @
   记录值: athenayan123-web.github.io
   ```

### 4. 访问地址

- **GitHub Pages**: https://athenayan123-web.github.io/openclaw-app123/index_new.html
- **自定义域名**: https://fdumemai.com （DNS 生效后）

## 本地开发

```bash
# 启动本地服务器
python -m http.server 8080

# 访问
http://localhost:8080/index_new.html
```

## 数据更新

运行数据采集脚本更新定价数据：

```bash
python crawl_pricing.py
```

生成的 `data/pricing_data.json` 会被前端页面自动读取。

## 技术栈

- **前端**: 原生 HTML + CSS + JavaScript
- **数据采集**: Python 3.x
- **部署**: GitHub Pages + GitHub Actions
- **域名**: fdumemai.com

## 常见问题

### Q: 为什么没有 dist 文件夹？
A: 本项目是纯静态网站，不使用构建工具（Vite/Webpack），无需构建步骤，直接部署源文件。

### Q: 如何更新网站内容？
A: 直接修改 HTML/CSS/JS 文件，推送到 GitHub，Actions 会自动部署。

### Q: GitHub Actions 部署失败？
A: 检查 Settings → Pages → Source 是否选择了 **GitHub Actions**。

## 联系方式

- **技术支持**: 杭州华寰科技有限责任公司
- **邮箱**: athenayan123@gmail.com
- **版权**: © 2025 复旦大学2025未来信息创新学院工程管理
