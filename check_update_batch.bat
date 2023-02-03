@echo off
setlocal enabledelayedexpansion

for /f "tokens=*" %%i in (computers.txt) do (
    set host=%%i
    echo Checking update on %host%...
    python check_update.py %host%
)

pause
