#!/usr/bin/env python3
from halo import Halo
from time import sleep
import os
import sys

spinner = Halo(text='Starting the ping application', spinner='growHorizontal')
spinner.start()
sleep(2)

spinner.stop()
spinner.succeed("Pinger initialisation complete")
#spinner.info('Type pinger("IP") to start. IP can be an IP address or hostname')
#def pinger():

response = os.system("ping -c 1 " + sys.argv[1])
#spinner.start()
#sleep(1)
#spinner.stop()
if response == 0:
    print("============")
    spinner.succeed(sys.argv[1]+" is up")
    print("============")
else:
    print("============")
    spinner.fail(sys.argv[1]+" is down")
    print("============")
