@echo off

if exist %LOCALAPPDATA%\conda\conda\envs\anaconda-project\Scripts\anaconda-project.exe %* goto yesfile
if not exist %LOCALAPPDATA%\conda\conda\envs\anaconda-project\Scripts\anaconda-project.exe %* goto nofile
goto end
:yesfile
echo File does exist
%LOCALAPPDATA%\conda\conda\envs\anaconda-project\Scripts\anaconda-project.exe %* run
goto end
:nofile
echo File does NOT exist
conda create -n anaconda-project python=3 anaconda-project
goto end
:end
