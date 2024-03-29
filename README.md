# zabbix-minecraft-server
Zabbix template for Minecraft server

## Requirements:
    1. Python's PIP: 
        (DEB-Based) apt-get install python-pip
        (RPM-Based) yum install python3
        (RHEL 8+) dnf install python3
    2. Access to "unversioned python" 
        (DEB-Based) apt-get install python-is-python3
        (RHEL-Based) alternatives --set python /usr/bin/python3
    3. Python module to get info from Minecraft server: 
        pip install mcstatus
    4. Of course a properly installed Zabbix agent.

For more information about unversioned python see: [minecraftparam.conf](minecraftparam.conf)

## Usage:
    0. Copy the stats_mcserver.py in /usr/local/bin on the Minecraft server.

    - `case 1` monitoring local server:
    1. Copy the Zabbix config file into /etc/zabbix/zabbix_agentd.d/ on the Minecraft server.
    2. Restart the Zabbix Agent.
    3. Import the template XML file(zbx_minecraft_template.xml) into your zabbix server and add to the correct host, change minecraft server port in host macros.

    - `case 2` monitoring remote server:
    1. Copy the Zabbix config file into /etc/zabbix/zabbix_agentd.d/ onto any server(e.g. local server).
    2. Restart the Zabbix Agent.
    3. Import the template XML file(zbx_minecraft_template.xml) into your zabbix server and add to the correct host, change minecraft server address and port in host macros.

    - `case 3` manual `stats_mcserver.py` using:
    run `python stats_mcserver.py param1 param2 param3`
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
        param3(port)

## Note:
This template was tested on zabbix 5.0, but you can try zbx_minecraft_template_zabbix3.2_nottested.xml for zabbix3.2 or older.
This template was modified so that it would be compatible with the fork.
I also plan to refine this template by adding discovering rules.
