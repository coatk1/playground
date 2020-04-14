:: Run test_batch.bat in command line

@echo off 
Rem This is for listing down all the files in the directory Program files 
:: dir "C:\Program Files" > C:\lists.txt
set completed=The program has completed
echo %completed%

SET /A a = 5 
SET /A b = 10 
SET /A c = %a% + %b% 
echo %c%

set list = 1 2 3 4 
(for %%a in (%list%) do ( 
   echo %%a 
))