# zabbix-minecraft-server
Zabbix template to Minecraft server

## Requirements:
    1. pyton-pip: 
        apt-get install python-pip
    2. Python module to get info from Minecraft server: 
        pip install mcstatus
    3. Of course a properly installed Zabbix agent.

## Usage:
    1. Copy the stats_mcserver.py in /usr/local/bin
    2. Copy the Zabbix config file into /etc/zabbix/zabbix_agentd.d/
    3. Restart the Zabbix Agent.
    4. Import the template XML file into your zabbix server and add to the correct host.

