@echo off
cd /d "%~dp0"
echo Opening Hope Voucher V2 (HOPE PROJECT 2022). Keep this window open while using the app.
echo New system will open at /v2 - Classic remains at /
set HOPE_V2=1
python "%~dp0odyssey-local.py" 2>nul
if %errorlevel%==0 goto :end
py "%~dp0odyssey-local.py" 2>nul
if %errorlevel%==0 goto :end
"C:\Users\itoha\AppData\Local\Programs\Python\Python314\python.exe" "%~dp0odyssey-local.py"
:end
if errorlevel 1 pause
