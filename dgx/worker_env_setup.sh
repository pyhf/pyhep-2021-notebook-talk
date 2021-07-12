#!/bin/bash

if [ -d "${HOME}/.pyenv/bin" ]; then
    export PYENV_ROOT="${HOME}/.pyenv"
    export PATH="${PYENV_ROOT}/bin:${PATH}"

    if command -v pyenv 1>/dev/null 2>&1; then
        eval "$(pyenv init -)"
    fi

    # Add pyenv-virtualenv
    if [ -d "${HOME}/.pyenv/plugins/pyenv-virtualenv" ]; then
        eval "$(pyenv virtualenv-init -)"
    fi
	# Supress prompt changing warning
	export PYENV_VIRTUALENV_DISABLE_PROMPT=1
fi

pyenv deactivate
pyenv activate pyhf-funcx
printf "Active pyenv environment: \n"
pyenv version
