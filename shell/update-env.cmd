:: Author(s): Corey Atkins
:: This script will update dev environment
@echo off

REM Launches the windows cmd
call PATH_TO_ANACONDA\activate.bat base

REM Check if the environment exists.
if exists %APPDATA%\conda\conda\env\dev\ %* goto yesfile
if not exists %APPDATA%\conda\conda\env\dev\ %* goto nofile
goto end

:yesfile
REM If it exists, update environment.
echo Environment does exist, updating...
pause
call conda activate dev
call conda env update coatk1/dev
goto end

:nofile
REM If it does not exists, install environment.
echo Environment does not exist, installing...
pause
call conda env create coatk1/dev
goto end

:end

echo done
