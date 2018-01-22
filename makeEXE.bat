@ECHO OFF
REM Runs both my project scripts

ECHO Running pyinstaller
python -m PyInstaller --workpath localDump\build --distpath localDump\dist Vault.spec
ECHO Finished
PAUSE