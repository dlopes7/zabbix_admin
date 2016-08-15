# zabbix_admin

This project helps my company to figure which machines we still need to install Zabbix Agents on.

It scans the VSphere server, builds a JSON of all servers, their IPs, OS and state using pyVmOmi.
It scans the Zabbix server, builds a JSON of all servers, their IPs, Host ID and Host Name.

Periodically refreshes the list, and let's you ignore server or attempt to install the agent remotely.

Very experimental software, use at your own risk.

To install:

1. Install Docker and Docker-compose
2. git clone https://github.com/dlopes7/zabbix_admin.git
3. docker-compose build
4. docker-compose run
5. Create a config.py under the tasks directory with the username and passwords used on the 3 scripts.
6. Edit the get_vsphere_machines.py and get_zabbix_machines.py to fit your environment, and run them:
7. docker-compose exec web bash -c "cd zabbix_admin/tasks && /usr/bin/env python get_zabbix_machines.py"
8. docker-compose exec web bash -c "cd zabbix_admin/tasks && /usr/bin/env python get_vsphere_machines.py"

I use a crontab entry for these 2 commands, it runs every 5 minutes.

