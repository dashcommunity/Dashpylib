from Dashpylib  import Dashpylib
from time import sleep

Pydash = Dashpylib(dir="/home/nova/Downloads/dash-0.12.1/bin")
execute = Pydash.command("./dash-cli getinfo")
#b = raw_input("what block do you want to be notified at? \ndashd is at block number " + str(execute) + "\n")
trigger = True
#print int(execute) >= int(b)
print execute

