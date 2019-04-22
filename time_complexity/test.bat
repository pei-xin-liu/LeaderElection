@echo off
set /A repeats = 100
set /A n = 13
python -m da -I thread orig.da 2
for /l %%i in (1, 1, %repeats%) do (
	pythonw -m da -I thread orig.da %n%
	echo repeat =  %%i
	)