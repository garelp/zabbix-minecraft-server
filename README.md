# zabbix-minecraft-server
Zabbix template to Minecraft server

## Requirements:
    1. pyton-pip: 
        apt-get install python-pip
    2. Python module to get info from Minecraft server: 
        pip install mcstatus
    3. Of course a properly installed Zabbix agent.

## Usage:
    0. Copy the stats_mcserver.py in /usr/local/bin on the Minecraft server.

    - `case 1` monitoring local server:
    1. Copy the Zabbix config file into /etc/zabbix/zabbix_agentd.d/ on the Minecraft server.
    2. Restart the Zabbix Agent.
    3. Import the template XML file into your zabbix server and add to the correct host, change minecraft server port in host macros.

    - `case 2` monitoring remote server:
    1. Copy the Zabbix config file into /etc/zabbix/zabbix_agentd.d/ on the any server(e.g. local server).
    2. Restart the Zabbix Agent.
    3. Import the template XML file into your zabbix server and add to the correct host, change minecraft server address and port in host macros.

    - `case 3` manual `stats_mcserver.py` using:
    run `python stats_mcserver.py param1, param2, param3`
    where:
        param1(check type):
        parameter that we want to get
        possible variants:
            getOnline:
                returns the number of players online
            getLatency:
                returns the response time to the remote server, in ms
            (any other data):
                returns the number of players online and the response time in csv format, first the players, then the response time (e.g. 5;3.12)

        param2(ip address or dns)
        param2(port)

##Note:
This template was tested on zabbix 5.0, but you can try importing the template to an older version.
This template was modified so that it would be compatible with the fork.
I also plan to refine this template by adding discovering rules.
