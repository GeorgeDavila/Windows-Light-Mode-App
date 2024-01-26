# Windows app to toggle light mode
Windows app to toggle light mode. Because apparently the UI geniuses at the trillion dollar company built on its OS think users like to navigate to settings just to toggle light/dark mode. 

Simply install the EXE file. Can then right click to pin it to your desktop or whereever 

# credits
Credits to these posts for the powershell script
https://www.windowscentral.com/how-switch-between-light-and-dark-colors-schedule-automatically-windows-10

https://superuser.com/questions/1544089/how-to-switch-between-light-and-dark-modes-via-command-line-in-win-10

# troubleshooting 
Will briefly open a console window since it needs to run a script on your system. This isn't suppressible with pyinstaller's exe options. But if you're worried about saftey you can build it completely from source following instructions in the Build your own exe section (assumes basic knowledge and use of python).

Only really tested for personal use, you may encounter errors. 
You may need to let python run scripts in powershell by running the following in powershell: `Set-ExecutionPolicy RemoteSigned`

see
https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow

# Build your own exe
for safety, customizability, or OS imcompatibility reasons you may want to build your own exe. Install library pyinstaller `pip install pyinstaller` or get it from source at `pip install https://github.com/pyinstaller/pyinstaller/tarball/develop` then run `python buildEXE.py` and the exe file will appear in your current directory