# Build script for TamilKavi package
# Run this script to clean, build, and prepare the package for upload

Write-Host "🧹 Cleaning old build files..." -ForegroundColor Yellow
Remove-Item -Recurse -Force build, dist, *.egg-info -ErrorAction SilentlyContinue

Write-Host "📦 Building package..." -ForegroundColor Green
python -m build

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Package built successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "📁 Built files in dist/:" -ForegroundColor Cyan
    Get-ChildItem dist/ | ForEach-Object { Write-Host "   - $($_.Name)" }
    Write-Host ""
    Write-Host "📤 To upload to PyPI, run:" -ForegroundColor Yellow
    Write-Host "   python -m twine upload dist/*" -ForegroundColor White
    Write-Host ""
    Write-Host "🧪 To test locally, run:" -ForegroundColor Yellow
    Write-Host "   pip install dist/tamilkavi-0.8.1-py3-none-any.whl --force-reinstall" -ForegroundColor White
} else {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    exit 1
}

