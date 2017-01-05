#!/usr/bin/python

from mcstatus import MinecraftServer

# If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
server = MinecraftServer.lookup("localhost")

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()
print("{0};{1}".format(status.players.online, status.latency))
