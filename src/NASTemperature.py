import logging
from SSH import SSH

class NASTemperature:
  def __init__(self):
    pass
  
  def get_temperature():
    username = "administrator"
    password = "TYwxz#@!564451"
    host = "192.168.1.20"
    port = 2222
    commands = [
      "smartctl -a /dev/sda | grep '194 Temperature'",
      "smartctl -a /dev/sdb | grep '194 Temperature'",
      "smartctl -a /dev/sdc | grep '194 Temperature'",
      "smartctl -a /dev/sdd | grep '194 Temperature'"
    ]
    logging.basicConfig(level=logging.ERROR)
    ssh = SSH()
    max_temp = 0
    for command in commands:
      status, output = ssh.run_sudo_command(ssh_username=username, ssh_password=password, ssh_machine=host, command=command, ssh_port=port)
      try:
        # get all temperatures from string 
        # 194 Temperature                                                      0x0022   044   055   000    Old_age   Always       -       44 (0 14 0 0 0)
        if status:
          for line in output:
            temp = int(line.split()[9])
            # print("Temp: %s" % temp)
            if temp > max_temp:
              max_temp = temp
      except Exception as e:
        logging.error("Error: %s" % e)
    
    return max_temp