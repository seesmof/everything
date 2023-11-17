@echo off
echo EXE Program:
exe.exe
echo %ERRORLEVEL%
echo --------------
echo COM Program without Function:
comNo.com
echo %ERRORLEVEL%
echo --------------
echo COM Program with Function:
comYes.com
echo %ERRORLEVEL%