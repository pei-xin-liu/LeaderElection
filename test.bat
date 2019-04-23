@echo off
set /A repeats = 1000
set /A n = 16
for /l %%i in (1, 1, %repeats%) do (
	python -m da -I thread --logfile --logfilename test.txt --logfilelevel output orig.da %n%
	echo repeat =  %%i
	)