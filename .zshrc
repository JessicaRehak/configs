# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi


# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac
                       
# Prompt #############################################################

# Load in the git branch prompt and autocompletion script.
fpath=(~/.scripts $fpath)
zstyle ':completion:*:*:git:*' script ~/.scripts/git-completion.bash
. ~/.scripts/git-prompt.sh

setopt PROMPT_SUBST
PS1='[%n@%m %~$(__git_ps1 " (%s)")]\$ '

. ~/.zsh_aliases        # Aliases

source /opt/powerlevel10k/powerlevel10k.zsh-theme

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
