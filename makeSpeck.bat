@ECHO OFF
REM Runs both my project scripts

ECHO Running pyinstaller to generate spec
pyi-makespec Vault main.py
ECHO Finished making spec file
PAUSE