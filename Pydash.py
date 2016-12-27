import os
import subprocess
from time import sleep
#run this module while ./dashd is running
class Pydash:


    def __init__(self, dir):
        #check if we are in right directory
        if not os.path.isfile('./dashd'): #I have a feeling i am not doing this right. Will fix
            return "error: dir varable is not pointing toward ./dash-cli "
        self.dir = dir


    def command(self, arg):
        splitArg = arg.split()
        for x in range(10):
            sleep(.1)
            info = subprocess.Popen(splitArg, shell=False, cwd=self.dir, ).communicate()
            if info == None:
                pass
            else:
                return info
        #add zip thing to return info as dict, not turple
