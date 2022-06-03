import os
import subprocess
from tkinter import *
from tkinter import ttk, messagebox


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


def is_zsh_installed():
    if is_zsh == 'ZSH is installed':
        installZshButton.state = DISABLED


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


def php_version():
    try:
        brewTerminalOutput = str(run_command(['php', '-v']))
        return split_string(brewTerminalOutput, 'PHP', 13)
    except:
        return "Not installed or bash paths incorrect"


def valet_version():
    try:
        brewTerminalOutput = str(run_command(['valet', '-V']))
        return split_string(brewTerminalOutput, 'Laravel Valet', 7)
    except:
        return "Not installed or bash paths incorrect"


def install_zsh():
    try:
        run_command('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
        messagebox.showinfo(title=None, message='ZSH successfully installed')
    except:
        messagebox.showerror(title=None, message="Couldn't installed")


window = Tk()
window.title('Valet dev pack')
window.geometry('600x400')
window.attributes('-topmost', True)
# first row
labelZsh = Label(window, text='Is ZSH installed :').place(x=10, y=10)
labelZshData = Label(window, text=is_zsh()).place(x=200, y=10)
installZshButton = ttk.Button(window, text='Install ZSH', state=DISABLED, command=install_zsh).place(x=400, y=5)
# second row
labelBrew = Label(window, text='Brew Version :').place(x=10, y=40)
labelBrewData = Label(window, text=brew_version()).place(x=200, y=40)
# third row
labelComposer = Label(window, text='Composer Version :').place(x=10, y=70)
labelComposerData = Label(window, text=composer_version()).place(x=200, y=70)
# fourth row
labelPhp = Label(window, text='PHP Version :').place(x=10, y=100)
labelPhpData = Label(window, text=php_version()).place(x=200, y=100)
# fifth row
labelValet = Label(window, text='Valet Version :').place(x=10, y=130)
labelValetData = Label(window, text=valet_version()).place(x=200, y=130)
window.mainloop()
