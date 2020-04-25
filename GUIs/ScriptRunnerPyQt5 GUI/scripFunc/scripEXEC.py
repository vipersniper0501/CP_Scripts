import os
import subprocess as sub
from sys import platform
import getpass
from threading import *
import distro #for figuring out what linux distro
import configparser


OS = distro.linux_distribution()
ops = OS[0]

config = configparser.ConfigParser()
config.read('config.ini')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ScriptRunnerFunc:
    def test():
        print('Hello World')

    def updateos(self):
        if ops == 'Ubuntu' or ops == 'debian':
            command = 'sudo apt update && upgrade -y'
            sub.Popen(command.split())
            print('Updates Completed!')
        elif platform == 'darwin':
            command = 'sudo softwareupdate -i -a'
            sub.Popen(command.split())
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -Syu'
            sub.Popen(command.split())
        elif platform == 'win32':
            #command = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", ". \"./mmfucntions.ps1\";", "&winupd"
            #sub.Popen(command)
            commands = """ Write-Host("Installing module PSWindowsUpdate if not already installed... ")
            Install-Module PSWindowsUpdate
            Write-Host("PSWindowsUpdate is now installed.")
            Write-Host("")
            Write-Host("Getting Windows Updates...")
            Import-Module PSWindowsUpdate
            $updates = Invoke-Command -ScriptBlock {Get-Wulist -verbose}
            $updatenumber = ($updates.kb).count
            if ($null -ne $updates){
                Get-WindowsUpdate -AcceptAll -Install | Out-File C:\PSWindowsUpdate.log
                do {$updatestatus = Get-Content c:\PSWindowsUpdate.log
                    "Currently processing the following update:"
                    Get-Content c:\PSWindowsUpdate.log | select-object -last 1
                    Start-Sleep -Seconds 10
                    $ErrorActionPreference = 'SilentlyContinue'
                    $installednumber = ([regex]::Matches($updatestatus, "Installed" )).count
                    $ErrorActionPreference = ‘Continue’
                }until ( $installednumber -eq $updatenumber)
            }
            Remove-Item -path C:\PSWindowsUpdate.log -ErrorAction SilentlyContinue
            Write-Host("")
            Write-Host("All updates are installed!")"""
            sub.Popen(["powershell","& {" + commands + "}"])
            # Definitely is executing but it needs to be run as admin. Must figure out a way to do that.

            # print('This function (updates) does not currently support this OS.')
        else:
            print('This command does not currently support this OS')

    def srchmedia(self):
        if platform == 'linux' or platform == 'darwin':
            extensions = ('.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
            for root, dirs, files in os.walk('/home/'):
                for filename in files:
                    if any(filename.endswith(extension) for extension in extensions):
                        # f = open('Q:\\Cyber Patriots\\my_scripts_and_STIGS\\Scripts\\CP_ScriptsREPAIR\\Script Runner GUI\\logTest.txt', 'a+')
                        f = open('/home/' + getpass.getuser() + '/Desktop/LogTest.txt', 'a+')
                        filepath = os.path.join(root, filename)
                        f.write(filepath + '\n')
                        f.close()
                        print(filepath)
            print('Scan for unapproved media complete.')
        elif platform == 'win32':
            extensions = ('.jpg', '.mp4', '.flv', '.avi', '.wmv', '.mov', '.png', '.tif', '.gif', '.mp3', '.wma', '.aif', '.jar')
            for root, dirs, files in os.walk('C:\\Users\\'):
                for filename in files:
                    if any(filename.endswith(extension) for extension in extensions):
                        f = open('C:\\Users\\' + getpass.getuser() + '\\Desktop\\logTest.txt', 'a+')
                        #f = open('/home/' + getpass.getuser() + '/Desktop/LogTest.txt', 'a+')
                        filepath = os.path.join(root, filename)
                        f.write(filepath + '\n')
                        f.close()
                        print(filepath)
            print('Scan for unapproved media complete.')

    def fwl(self):
        if platform == 'linux':

            commandtest = 'sudo ufw status'
            exec = sub.Popen(commandtest.split(), stdout=sub.PIPE)
            stdout, _ = exec.communicate()
            output = stdout.decode('utf-8')

            if output == 'sudo: ufw: command not found':
                if ops == "Manjaro Linux":
                    commandufw = 'sudo pacman -S ufw --noconfirm'
                else:
                    commandufw = 'sudo apt install ufw -y'
                sub.call(commandufw.split())
                command = 'sudo ufw enable'
                sub.Popen(command.split())


            commandlog = 'sudo ufw status > firewallLOG.txt'
            os.system(commandlog)
            with open('firewall.txt', 'r') as f:
                for line in f:
                    output = f.read()
            print('The following is the output of your original firewall settings:\n')
            print(output)

            print('-----------------------Firewall Settings Has Started-----------------------')
            #SSH
            ssh = config.get('Services', 'ssh')
            if ssh == 'yes':
                command = 'sudo ufw allow 22'
                sub.Popen(command.split())
            elif ssh == 'no':
                command = 'sudo ufw deny 22'
                sub.Popen(command.split())
            #FTP
            ftp = config.get('Services', 'ftp')
            if ftp == 'yes':
                command = 'sudo ufw allow 21'
                sub.Popen(command.split())
            elif ftp == 'no':
                command = 'sudo ufw deny 21'
                sub.Popen(command.split())
            #WEB
            web = config.get('Services', 'web')
            if web == 'yes':
                command = 'sudo ufw allow 80'
                sub.Popen(command.split())
                https = config.get('Services', 'https')
            elif web == 'no':
                command = 'sudo ufw deny 80'
                sub.Popen(command.split())
            #HTTPS
            https = config.get('Services', 'https')
            if https == 'yes':
                command = 'sudo ufw allow 443'
                sub.Popen(command.split())
            elif https == 'no':
                command = 'sudo ufw deny 443'
                sub.Popen(command.split())
            #Samba
            smb = config.get('Services', 'smb')
            if smb == 'yes':
                command = 'sudo ufw allow 139'
                sub.Popen(command.split())
            elif smb == 'no':
                command = 'sudo ufw deny 139'
                sub.Popen(command.split())
            #SQL
            sql = config.get('Services', 'sql')
            if sql == 'yes':
                command = 'sudo ufw allow 3306'
                sub.Popen(command.split())
            elif sql == 'no':
                command = 'sudo ufw deny 3306'
                sub.Popen(command.split())
            #Rsync
            rsnc = config.get('Services', 'rsnc')
            if rsnc == 'yes':
                command = 'sudo ufw allow 873'
                sub.Popen(command.split())
            elif rsnc == 'no':
                command = 'sudo ufw deny 873'
                sub.Popen(command.split())

            print('------------------The Following Ports Have Been Closed Automatically-----------------')
            print('Port 19 has been closed to stop potential DoS attack')
            command = 'sudo ufw deny 19'
            sub.Popen(command.split())
            print('Port 123 has been closed to stop potential trojans (NetController)')
            command = 'sudo ufw deny 123'
            sub.Popen(command.split())
            print('Port 161 has been closed to stop SNMP functionality')
            command = 'sudo ufw deny 161'
            sub.Popen(command.split())
            print('Port 162 has been closed to stop SNMPtrap functionality')
            command = 'sudo ufw deny 162'
            sub.Popen(command.split())
            print('Port 1434 has been blocked to stop potential DoS attack')
            command = 'sudo ufw deny 1434'
            sub.Popen(command.split())
            print('Port 23 has been denied due to Telnet functionality is not necessary')
            command = 'sudo ufw deny 23'
            sub.Popen(command.split())

            #This next service should probably be asked during first time configurations

            #print('Port 53 has been closed to stop the use of DNS functionality since this is not a DNS Server')
            #command = 'sudo ufw deny 53'
            #sub.Popen(command.split())

            print('--------------------Firewall Settings Have Finished-----------------------')

        elif platform == 'win32':
             print('-----------------------Firewall Settings Has Started-----------------------')
             ssh = config.get('Services', 'ssh')
             if ssh == 'yes':
                command = "netsh advfirewall firewall add rule name='ssh' dir=in action=allow protocol=TCP localport=22"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ssh' dir=out action=allow protocol=TCP localport=22"
                sub.Popen(["powershell","& {" + command + "}"])
             elif ssh == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=22"
                sub.call(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ssh' dir=in action=block protocol=TCP localport=22"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ssh' dir=out action=block protocol=TCP localport=22"
                sub.Popen(["powershell","& {" + command + "}"])
            #FTP
             ftp = config.get('Services', 'ftp')
             if ftp == 'yes':
                command = "netsh advfirewall firewall add rule name='ftp' dir=in action=allow protocol=TCP localport=21"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ftp' dir=out action=allow protocol=TCP localport=21"
                sub.Popen(["powershell","& {" + command + "}"])
             elif ftp == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=21"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ftp' dir=in action=block protocol=TCP localport=21"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='ftp' dir=in action=block protocol=TCP localport=21"
                sub.Popen(["powershell","& {" + command + "}"])
             #WEB
             web = config.get('Services', 'web')
             if web == 'yes':
                command = "netsh advfirewall firewall add rule name='webserver' dir=in action=allow protocol=TCP localport=80"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='webserver' dir=out action=allow protocol=TCP localport=80"
                sub.Popen(["powershell","& {" + command + "}"])
             elif web == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=80"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='webserver' dir=in action=block protocol=TCP localport=80"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='webserver' dir=out action=block protocol=TCP localport=80"
                sub.Popen(["powershell","& {" + command + "}"])
             #HTTPS
             https = config.get('Services', 'https')
             if https == 'yes':
                command = "netsh advfirewall firewall add rule name='https' dir=in action=allow protocol=TCP localport=443"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='https' dire=out action=allow protocol=TCP localport=443"
                sub.Popen(["powershell","& {" + command + "}"])
             elif https == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=443"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='https' dir=in action=block protocol=TCP localport=443"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='https' dire=out action=block protocol=TCP localport=443"
                sub.Popen(["powershell","& {" + command + "}"])
             #Samba
             smb = config.get('Services', 'smb')
             if smb == 'yes':
                command = "netsh advfirewall firewall add rule name='SAMBA' dir=in action=allow protocol=TCP localport=139"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SAMBA' dire=out action=allow protocol=TCP localport=139"
                sub.Popen(["powershell","& {" + command + "}"])
             elif smb == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=139"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SAMBA' dir=in action=block protocol=TCP localport=139"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SAMBA' dire=out action=block protocol=TCP localport=139"
                sub.Popen(["powershell","& {" + command + "}"])
             #SQL
             sql = config.get('Services', 'sql')
             if sql == 'yes':
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=in action=allow protocol=TCP localport=3306"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=out action=allow protocol=TCP localport=3306"
                sub.Popen(["powershell","& {" + command + "}"])
             elif sql == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=3306"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=in action=block protocol=TCP localport=3306"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='SQLserver' dir=out action=block protocol=TCP localport=3306"
                sub.Popen(["powershell","& {" + command + "}"])
             #Rsync
             rsnc = config.get('Services', 'rsnc')
             if rsnc == 'yes':
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=in action=allow protocol=TCP localport=873"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=out action=allow protocol=TCP localport=873"
                sub.Popen(["powershell","& {" + command + "}"])
             elif rsnc == 'no':
                command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=873"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=in action=block protocol=TCP localport=873"
                sub.Popen(["powershell","& {" + command + "}"])
                command = "netsh advfirewall firewall add rule name='RSYNC' dir=out action=block protocol=TCP localport=873"
                sub.Popen(["powershell","& {" + command + "}"])
             #RDP
             rdp = config.get('Services', 'rdp') #must block/allow port 5985 and 3389
             if rdp == 'yes':
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=allow protocol=TCP localport=5985"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=allow protocol=TCP localport=3389"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=allow protocol=TCP localport=5985"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=allow protocol=TCP localport=3389"
                 sub.Popen(["powershell","& {" + command + "}"])
             elif rdp == 'no':
                 command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=5985"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall delete rule name=all protocol=TCP localport=3389"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=block protocol=TCP localport=5985"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=in action=block protocol=TCP localport=3389"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=block protocol=TCP localport=5985"
                 sub.Popen(["powershell","& {" + command + "}"])
                 command = "netsh advfirewall firewall add rule name='RDPconfig' dir=out action=block protocol=TCP localport=3389"
                 sub.Popen(["powershell","& {" + command + "}"])

        elif platform == 'darwin':
             print('This command is currently in developement')
        else:
            print('This command is currently in developement')

    def servSet(self):
        print('This command is currently in developement')

    def malRem(self):
        print('This command is currently in developement')

    def alyn(self):
        if ops == 'Ubuntu' or ops == 'debian':
            command = 'sudo apt install lynis -y'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system'
            sub.Popen(command2.split())
        elif ops == 'darwin':
            print('This function does not currently support this OS')
        elif ops == 'Manjaro Linux':
            command = 'sudo pacman -S lynis --noconfirm'
            sub.Popen(command.split())
            command2 = 'sudo lynis audit system'
            sub.Popen(command2.split())
        elif platform == 'win32':
            print('This function (alyn) does not currently support this OS.')

    def basConf(self):
        print('This command is currently in developement')

    def rmProCont(self):
        print('This command is currently in developement')
