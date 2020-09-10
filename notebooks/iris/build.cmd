@echo off

if exist C:\Users\Corey\Miniconda3\envs\pyBase1\Scripts\anaconda-project.exe %* goto yesfile
if not exist C:\Users\Corey\Miniconda3\envs\pyBase1\Scripts\anaconda-project.exe %* goto nofile
goto end
:yesfile
echo File does exist
C:\Users\Corey\Miniconda3\envs\pyBase1\Scripts\anaconda-project.exe %* run notebook
goto end
:nofile
echo File does NOT exist
conda create -n anaconda-project python=3 anaconda-project
goto end
:end
