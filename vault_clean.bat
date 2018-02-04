@echo off
IF EXIST "%LOCALAPPDATA%\PandorAstrum" (
echo Vault Tools previously used
echo Trying to clean old cache
rmdir "%LOCALAPPDATA%\PandorAstrum" /s
echo Directory Cleaned..
PAUSE
) ELSE (
echo Vault Tools not used...
PAUSE
)