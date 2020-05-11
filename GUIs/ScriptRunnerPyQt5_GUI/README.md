# Script GUI based on PyQt5
This script runs on Mac OS X, Windows 10, Windows 8.x, Windows 7, Debian, Ubuntu, and Manjaro Linux

## List of supported commands:
### Universal Commands
#### Updates: 
This command will update your Operating System (Only the Operating System if you are using Windows 10 or Mac OS) When using on windows 10, it will continue to keep cheking for updates until there are none left compared to Settings > Updates which will only check once and update. NOTE: For other updates to third party apps, I recommend using software such as PatchMyPc which will update up 250+ apps at once. 
______________________________________________
#### Search For Prohibited Media: 
This command will search through the entire system looking for the following file types: .jpg, .mp4, .flv, .avi, .wmv, .mov, .png, .tif, .gif, .mp3, .wma, .aif, .jar  This command will output it's results into a text file on the Desktop.
______________________________________________
#### Remove Prohibited Software: 
This command will search through your system looking for known games and software that is known to be against the rules of Cyber Patriots. E.g. Wireshark and BitTorrent
_________________________________________________________
#### Check the Hash of a File: 
This command will check the hash of a file of your choosing. (helpful for Forensics Questions)
______________________________________________
#### Services Configurations: 
This command will apply premade configurations to services like ssh, ftp, and samba.
______________________________________________

### Windows Specific Commands
#### Windows Firewall Settings: 
This command will open or close certain ports based upon the configurations you made when you first opened the app. Along with those changes it will also close a couple of other ports that are known vulnerabilities.
______________________________________________
#### Windows Basic Configurations: 
This command will install prebuilt Local Policies (E.g. Lockout policies, audit policies, and password policies) and Group Policies and making sure that IE is also installed, because that will always be required. I have missed too many points due to forgetting about Internet Explorer 
______________________________________________

### Linux Specific Commands
#### Linux Firewall Settings: 
This command will open or close certain ports based upon the configurations you made when you first opened the app. Along with those changes it will also close a couple of other ports that are known vulnerabilities.
______________________________________________
#### Audit System: 
This command will install an auditing program called Lynis that checks for vulnerabilities that you will want to change. It will ouput the results into a text file on the Desktop
______________________________________________
#### Malware Removal: 
This command will use the program called ClamAV/ClamTK to search for Malware on this machine.
______________________________________________
#### Linux Basic Configurations: 
This command will install premade Local Policies (E.g. Lockout Policies and Password Policies)
