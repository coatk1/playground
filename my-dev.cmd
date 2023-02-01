:: Author(s): Corey Atkins
:: This script will update dev environment
@echo off

REM Launches the windows cmd
call PATH_TO_ANACONDA\activate.bat base

REM Check if the environment exists.
if exists %APPDATA%\conda\conda\env\my-dev\ %* goto yesfile
if not exists %APPDATA%\conda\conda\env\my-dev\ %* goto nofile
goto end

:yesfile
REM If it exists, update environment.
echo Environment does exist.
pause
call conda activate my-dev
:: echo Updating environment
:: call conda env update coatk1/my-dev
goto end

:nofile
REM If it does not exists, install environment.
echo Environment does not exist, installing...
pause
:: call conda env create coatk1/my-dev
call conda env create -f dev.yml
goto end

:end

echo done
