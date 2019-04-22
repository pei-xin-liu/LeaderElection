@echo off
if exist nMsg.txt (del /f nMsg.txt)
python -m da -I thread --logfile --logfilename nMsg.txt --logfilelevel output orig.da 2
del /f nMsg.txt
set /A maxProc = 500
set /A testPoints = 50
set /A repeats = 10
set /A step = maxProc / testPoints
for /l %%i in (%step%, %step%, %maxProc%) do (
	for /l %%j in (1, 1, %repeats%) do (
		pythonw -m da -I thread --logfile --logfilename nMsg.txt --logfilelevel output orig.da %%i
		echo proc =  %%i, repeat =  %%j
		)
	)