try:
    from config import ssh_user, ssh_password
except:
    from zabbix_admin.tasks.config import ssh_user, ssh_password

from zabbix_admin.tasks.get_zabbix_machines import main as get_maquinas_zabbix
from zabbix_admin.tasks.update_servers import main as update_servers

import sh
import sys
def instalar(servidor, os):
    instalado = False
    if 'linux' in os.lower():
        print('Linux nao implementado')
    elif 'windows' in os.lower():
        comando =  '"C:\zabbix_installer\zabbix_installer.bat" {servidor}'.format(servidor=servidor)
        resultado = sh.winexe('--user=dcnova/{username}%{password}'.format(username=ssh_user,
                                                                   password=ssh_password),
                             '--runas=dcnova/{username}%{password}'.format(username=ssh_user,
                                                                             password=ssh_password),
                             '//hp-sitescope003.dc.nova',
                             comando
                             )
        if 'iniciado' in resultado:
            instalado = True

    get_maquinas_zabbix()
    update_servers()
    return instalado


if __name__ == '__main__':
    servidor = sys.argv[1]
    instalar(servidor, 'windows')


