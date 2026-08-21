# How to Update TamilKavi Python Package

## Steps to Update and Publish the Package

### 1. Update Version Number
✅ Already done - Version updated from 0.6.0 to 0.7.0 in `setup.py`

### 2. Clean Old Build Files
```bash
# Remove old build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/
```

Or on Windows PowerShell:
```powershell
Remove-Item -Recurse -Force build, dist, *.egg-info -ErrorAction SilentlyContinue
```

### 3. Install Build Tools (if not already installed)
```bash
python -m pip install --upgrade build twine
```

### 4. Build the Package
```bash
python -m build
```

This will create:
- `dist/tamilkavi-0.7.0.tar.gz` (source distribution)
- `dist/tamilkavi-0.7.0-py3-none-any.whl` (wheel distribution)

### 5. Test the Build Locally (Optional)
```bash
# Install the new version locally
pip install dist/tamilkavi-0.7.0-py3-none-any.whl --force-reinstall

# Test it
tamilkavi -a "Raj Thambu"
```

### 6. Upload to PyPI

#### Test PyPI (for testing):
```bash
python -m twine upload --repository testpypi dist/*
```

#### Production PyPI:
```bash
python -m twine upload dist/*
```

You'll need your PyPI credentials (username and password/token).

### 7. Verify Installation
After publishing, users can install the updated version:
```bash
pip install --upgrade tamilkavi
```

## What's New in Version 0.7.0
- ✅ Tamil now actually displays in the terminal
  - The console is switched to UTF-8 on startup; it previously used a legacy
    code page (437 on Windows) that cannot encode Tamil at all
  - Poems print as blocks instead of table rows, so the poet's own line breaks
    survive -- a table re-wrapped every cell and destroyed them
  - Text width is measured in Tamil letters rather than Unicode code points,
    so output no longer overflows
  - On the classic Windows console, a note explains that it cannot shape Tamil
    and points to Windows Terminal or the website
- ✅ Corrected poem data
  - Fixed `உன்பin`, where the Tamil `ின்` had been replaced by Latin `in`
  - Fixed a mid-sentence `?` that should have been a vocative comma
  - Meanings are now consistently in Tamil across both poets
- ✅ Updated the project website link to tamilkavi.anandsundaramoorthy.com
- ✅ Stopped tracking build artifacts (`__pycache__`, `.coverage`)

## What's New in Version 0.6.0
- ✅ Added new poems by Raj Thambu:
  - Pongal Vaazhthu (பொங்கல் வாழ்த்து)
  - Tamil New Year Greetings
  - Deepavali Greetings
  - Monsoon Rain Greetings
- ✅ Fixed ArgumentParser to always show 'tamilkavi' in usage
- ✅ Updated test assertions for better compatibility

