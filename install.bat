@echo off
title Ball Game Installer
echo Installing needed modules!
echo Please wait...
mkdir Logs
cd Logs
python -m pip install pygame > module1.txt
python -m pip install pymunk > module2.txt
python -m pip install keyboard > module3.txt
python -m pip install pyautogui > module4.txt
cd ..
cls
echo All modules needed are installed!
echo You can find the logs for those downloaded modules in the 'logs' directory!
pause
cls
echo Thanks for playing HighTide's ball game!
echo ----------------------------------------
echo Press any key to exit!
pause > nul
exit 0