echoT() {
    echo "$(date '+%Y-%m-%d %H:%M:%S.%6N') — $*"
}

echoT "This is a test message."