#!/usr/bin/python

import sys

###sys.argv[1] - check type
###sys.argv[2] - ip address
###sys.argv[3] - port


# Get server instance
try:
    from mcstatus import JavaServer
    server = JavaServer(sys.argv[2], int(sys.argv[3]))
except:
    from mcstatus import MinecraftServer
    server = MinecraftServer(sys.argv[2], int(sys.argv[3]))

###sys.argv[1] - check type
###sys.argv[2] - ip address
###sys.argv[3] - port


# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
# get server motd
try:
    status = server.status()
    # parse
    if sys.argv[1] == "getOnline":
        print(status.players.online)
    elif sys.argv[1] == "getLatency":
        print(status.latency)
    else:
        print("{0};{1}".format(status.players.online, status.latency))
except:
    print(0)
