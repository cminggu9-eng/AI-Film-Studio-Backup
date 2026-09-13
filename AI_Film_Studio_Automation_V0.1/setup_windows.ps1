param(
    [string]$VaultPath = ""
)

$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host "=== AI Film Studio Automation V0.1 Setup ===" -ForegroundColor Cyan
Write-Host ""

if ([string]::IsNullOrWhiteSpace($VaultPath)) {
    $VaultPath = Read-Host "请粘贴你的 Obsidian Vault 完整文件夹路径"
}

$VaultPath = $VaultPath.Trim().Trim('"')

if (-not (Test-Path -LiteralPath $VaultPath -PathType Container)) {
    throw "找不到 Vault 文件夹：$VaultPath"
}

$HomeDir = Join-Path $VaultPath "00_HOME"
if (-not (Test-Path -LiteralPath $HomeDir -PathType Container)) {
    throw "这个路径看起来不像 AI Film Studio Vault：缺少 00_HOME 文件夹。"
}

$Config = [ordered]@{
    vault_path = $VaultPath
    progress_relative_path = "00_HOME/📋 当前进度.md"
    log_relative_dir = "00_HOME/工作日志"
    backup_relative_dir = "99_ARCHIVE/_AUTO_BACKUP"
}

$ConfigPath = Join-Path $ProjectRoot "studio.config.json"
$Config | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $ConfigPath -Encoding UTF8

New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot "runtime\_STAGING") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot "runtime\_PUBLISHED") | Out-Null

Write-Host ""
Write-Host "Vault 已绑定：" -ForegroundColor Green
Write-Host $VaultPath
Write-Host ""

try {
    $PythonVersion = & python --version 2>&1
    Write-Host "Python：" $PythonVersion -ForegroundColor Green
}
catch {
    Write-Warning "没有检测到 python 命令。发布脚本需要 Python 3。"
}

Write-Host ""
Write-Host "配置完成：" -ForegroundColor Green
Write-Host $ConfigPath
Write-Host ""
Write-Host "下一步：用 Codex 打开这个自动化文件夹，并让它先做 pipeline self-test。"
