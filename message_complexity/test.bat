@echo off
set /A repeats = 1000
set /A n = 25
for /l %%i in (1, 1, %repeats%) do (
	python -m da -I thread orig.da %n%
	echo repeat =  %%i
	)