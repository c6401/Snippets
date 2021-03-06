touch ~/.bashrc.whitelist

function _source_rc () {
    if grep -Fxq "$PWD" ~/.bashrc.whitelist
    then
        source .bashrc
    else
        read -p "Whitelist $PWD/.bashrc file? " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]
        then
            echo $PWD >> ~/.bashrc.whitelist
            source .bashrc
        fi
    fi
}

if [ -f .bashrc ] && [ "$PWD" != "$HOME" ]
then
    _source_rc
fi

function cd () {
    builtin cd "$@"
    if [ -f .bashrc ]
    then
        _source_rc
    fi
}
