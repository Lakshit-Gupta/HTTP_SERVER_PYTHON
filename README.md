Python_HTTP_Server(IN_BUILT) + CUSTOM
#************************************************************#
Some Command Line to follow In order to start the start open the terminal/powershell/cmd and Type " python -m http.server " This is an inbuilt command in order to start a http server where python describe the language use ,followed by spaace and -m which is use to give attribute or use as a flag to modify the command ,where m specifies as module used and then the module name ,this will open a simple http server on local host port 8000 by default In order to host a server available to all Local area natwork ,Type this command "python -m http.server 1024 -b 192.168.29.147" This command starts an connection at a particular port and your ip address , 1024 is the port no -b is used for binding and then ip address to which it will be binded Now this has opened a local server accessible to the people connected in the LAN network , all they have to do is to open a browser and type the ip address with colon and then port they would be abel to access the file where you opened your server ,like 192.168.29.147:1024 and you are done . NOTE:- OPEN THE CMD AS ADMIN AND USE COMMAND ipcinfig TO KNOW YOUR IP ADDRESS IN WINDOWs, ABOUT THE PORTS SOME PORT MIGHT NOT WORK AS SOME PORTS ARE PRIVILIGE PORTS I RECOMMEND TO USE PORT 1024-65535
