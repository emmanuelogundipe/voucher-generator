@echo off
cd /d "%~dp0"
echo Opening Odyssey. Keep this window open while using the app.
python "%~dp0odyssey-local.py" 2>nul
if %errorlevel%==0 goto :end
py "%~dp0odyssey-local.py" 2>nul
if %errorlevel%==0 goto :end
"C:\Users\itoha\AppData\Local\Programs\Python\Python314\python.exe" "%~dp0odyssey-local.py"
:end
if errorlevel 1 pause
