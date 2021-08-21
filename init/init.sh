#!/bin/bash
#
# Copyright (C) 2020-2021 by TR-TECH-GUIDE.
# All rights reserved.

. init/logbot/logbot.sh
. init/utils.sh
. init/checks.sh

trap handleSigTerm TERM
trap handleSigInt INT
trap 'echo hi' USR1

initUserge() {
    printLogo
    assertPrerequisites
    sendMessage "Initializing Userge ..."
    assertEnvironment
    editLastMessage "Starting Userge ..."
    printLine
}

startUserge() {
    startLogBotPolling
    runPythonModule userge "$@"
}

stopUserge() {
    sendMessage "Exiting Userge ..."
    endLogBotPolling
}

handleSigTerm() {
    log "Exiting With SIGTERM (143) ..."
    stopUserge
    exit 143
}

handleSigInt() {
    log "Exiting With SIGINT (130) ..."
    stopUserge
    exit 130
}

runUserge() {
    initUserge
    startUserge "$@"
    local code=$?
    stopUserge
    return $code
}
