# 价格趋势分析页面修改脚本
# 目标：找到index.html中的价格趋势部分并修改

$path = "E:\智能整理\openclaw\app\index.html"
$content = Get-Content $path -Raw

# 查找"价格趋势"出现的位置
$positions = @()
$lines = $content -split "`n"
for ($i=0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "价格趋势") {
        $positions += "Line $($i+1): $($lines[$i].Trim())"
    }
}

Write-Host "找到的'价格趋势'出现位置：" -ForegroundColor Cyan
$positions | ForEach-Object { Write-Host "  $_" }

# 找到section-trends部分
if ($content -match "section-trends") {
    Write-Host "`n✅ 找到section-trends部分" -ForegroundColor Green
    
    # 提取该部分代码
    $startIdx = $content.IndexOf("section-trends")
    $extract = $content.Substring($startIdx, [Math]::Min(500, $content.Length - $startIdx))
    Write-Host "`nssection-trends前500字符：" -ForegroundColor Yellow
    Write-Host $extract
} else {
    Write-Host "`n❌ 未找到section-trends部分" -ForegroundColor Red
}