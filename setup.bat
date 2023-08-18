@echo off

REM This script will install everything you'll need to build and use FyUTILS.
REM If you don't have go installed, the project won't be built.
REM If you have the binary file, the script will install the application.

echo Installing FyUTILS...

echo Installing Go dependencies...
go install

echo Building...
go build -v

echo Copying files...
copy %cd%\FyUTILS.exe %userprofile%

echo Prepairing start...
cd %userprofile%

echo Starting FyUTILS...
fyutils