# How to Update TamilKavi Python Package

## Steps to Update and Publish the Package

### 1. Update Version Number
✅ Already done - Version updated to 0.8.1

The version lives in **one place only**: `tamilkavi/__init__.py`. `setup.py` reads it
from there and `tamilkavi --version` reports it, so they cannot drift apart. To bump a
release, edit that one line.

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
- `dist/tamilkavi-0.8.1.tar.gz` (source distribution)
- `dist/tamilkavi-0.8.1-py3-none-any.whl` (wheel distribution)

### 5. Test the Build Locally (Optional)
```bash
# Install the new version locally
pip install dist/tamilkavi-0.8.1-py3-none-any.whl --force-reinstall

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

## What's New in Version 0.8.1

- ✅ **`--read` no longer opens a blank browser tab.** Asking for a poem that does
  not exist now prints `No results found.` and opens nothing. Previously the
  message was swallowed and an empty page appeared instead.
- ✅ **`-e` is honoured with `--read`.** The flag used to be silently ignored, so
  the browser always showed Tamil script. Ask for romanised output and you get it,
  whichever way you are reading.
- ✅ Fixed results leaking between runs of `main()` in the same process.

## What's New in Version 0.8.0

Corrects the record: the previous release was numbered 0.7.1, but it added features
rather than fixing bugs, so it should have been a minor bump. This release carries
that work under the right number, plus the documentation that was missed.

- ✅ **Read Tamil that actually renders**

  No terminal on any operating system shapes Tamil script correctly. A terminal draws
  one cell per Unicode code point, but a Tamil letter is usually several code points
  that must compose into one shape, so clusters always break apart. Two ways around it:

  - `-e` / `--english` prints the poem in Tanglish. It follows Tamil's own sound rules
    rather than swapping letters one by one, so `நதி` is *nadhi* but `அதிபதி` is
    *adhibadhi*, `பொங்கல்` is *pongal*, and `விட்ட` is *vitta*. Readable in every
    terminal, on every OS.
  - `-r` / `--read` opens the poem in your browser, which shapes Tamil properly. It
    prints nothing to the terminal, since the terminal copy is the broken one.

- ✅ **`--version`** reports the installed version.

- ✅ **No third-party dependencies** on Python 3.9+. Books are listed as labelled
  blocks instead of a table -- column widths can never be correct for Tamil, so the
  borders always tore -- which removed the last use of `prettytable`.

- ✅ **Fixed a break on Python 3.7 and 3.8.** `setup.py` installed the
  `importlib_resources` backport for those versions, but the code called
  `importlib.resources.files()` directly, which only exists from 3.9. The package
  installed and then crashed on startup.

- ✅ Works on Windows, macOS and Linux.

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

