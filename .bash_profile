#
# ~/.bash_profile
#

export PATH

#Set editor
EDITOR=emacs
export EDITOR

VISUAL=emacs
export VISUAL

#Set XDG Base directory specification
XDG_CONFIG_HOME=~/.config
export XDG_CONFIG_HOME

[[ -f ~/.bashrc ]] && . ~/.bashrc

# Other files ########################################################
. ~/.bash_aliases        # Bash aliases
. ~/.bash_local          # Local settings
