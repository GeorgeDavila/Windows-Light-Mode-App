import os
import copy

def setLightmodeState(stateString):
    #"0" or "1"
    lightmodestateFile0 = open("state.txt", "w")
    lightmodestateFile0.write(stateString)
    lightmodestateFile0.close()

def readLightmodeState():
    #"0" or "1"
    lightmodestateFile = open("state.txt", "r")
    lightmodestateRead = str( lightmodestateFile.read() )
    lightmodestate = copy.deepcopy( lightmodestateRead )#str to avoid error in case user puts in a random character
    lightmodestateFile.close()

    return lightmodestate

def lightmode():
    os.system("powershell.exe New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 1 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 1 -Type Dword -Force")
    setLightmodeState("1")

def darkmode():
    os.system("powershell.exe New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme -Value 0 -Type Dword -Force; New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name AppsUseLightTheme -Value 0 -Type Dword -Force")
    setLightmodeState("0")

def getCurrentValue():
    #pain to return anython well-ordered. Don't end up using this. But leaving it in in case you want it 
    os.system("powershell.exe Get-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize -Name SystemUsesLightTheme")

def toggle():
    #wrap in func to prent cross-contamination of state
    if readLightmodeState() == "0": #if its currently in dark mode
        lightmode()
        return 0
    elif readLightmodeState() == "1": #if its currently in light mode
        darkmode()
        return 0
    else: #case where state file potentially corrupted, reset to light mode
        lightmode()

toggle()