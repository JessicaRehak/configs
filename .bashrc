
# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# History ############################################################
HISTCONTROL=ignoreboth # ignore duplicate lines or leading spaces
HISTSIZE=1000          # Set history size to 1000 commands
HISTFILESIZE=2000      # Set the size of the history file
shopt -s histappend    # Don't wipe history on shell exit

# Misc ###############################################################
# After each command check window size and resize if necessary
shopt -s checkwinsize  
                       
# Make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# Prompt #############################################################

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# Load in the git branch prompt and autocompletion script.
source ~/.scripts/git-prompt.sh
source ~/.scripts/git_completion.sh

case "$TERM" in
    xterm-color) color_prompt=yes;;
esac

#Check for color support in the terminal
if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
    color_prompt=yes
else
    color_prompt=
fi

if [ "$color_prompt" = yes ]; then
    PS1='\[\e[0;32m\]\u@\h\[\e[m\] \[\033[38;5;14m\]\w\[\e[m\]$(__git_ps1 " (%s)")\[\e[1;32m\] \$\[\e[m\] \[\e[1;37m\]'
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac
#export TERM=xterm-256color
# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Start X at login
#[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]] && exec startx

# LS_COLORS=$LS_COLORS:'di=1;44:' ; export LS_COLORS
