import os
import subprocess

from tkinter import *


# Functions
# Run shell commands
def run_command(command):
    return subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]


# Split terminal strings
def split_string(string, keyword, characterLengthAfterKeyword):
    keywordStartingFrom = string.find(keyword)
    return string[keywordStartingFrom:keywordStartingFrom + len(keyword) + characterLengthAfterKeyword]


# Check if zsh installed
def is_zsh():
    if os.path.exists('/bin/zsh'):
        return 'ZSH is installed'


def brew_version():
    try:
        brewTerminalOutput = str(run_command(['brew', '-v']))
        return split_string(brewTerminalOutput, 'Homebrew', 6)
    except:
        return "Not installed or bash paths incorrect"


def composer_version():
    try:
        brewTerminalOutput = str(run_command(['composer', '-V']))
        return split_string(brewTerminalOutput, 'Composer', 16)
    except:
        return "Not installed or bash paths incorrect"


window = Tk()
window.title('Valet dev pack')
window.geometry('600x400')
labelZsh = Label(window, text='Is ZSH installed').place(x=10, y=10)
labelZshData = Label(window, text=is_zsh()).place(x=200, y=10)
labelBrew = Label(window, text='Brew Version').place(x=10, y=40)
labelBrewData = Label(window, text=brew_version()).place(x=200, y=40)
labelComposer = Label(window, text='Composer Version').place(x=10, y=70)
labelComposerData = Label(window, text=composer_version()).place(x=200, y=70)
labelValet = Label(window, text='Valet Version').place(x=10, y=100)
labelValetData = Label(window, text=composer_version()).place(x=200, y=100)
window.mainloop()
