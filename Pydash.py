import os
import subprocess
#run this module while ./dashd is running
class Pydash:


    def __init__(self):
        #check if we are in right directory
        if os.path.isfile('./dashd'):
            print "in right directory"
        else:
            print "script is not in right directory"

    def command(self, arg):
        splitArg = arg.split()

        return_arg = subprocess.check_output(splitArg, stdin=None, stderr=None, shell=False, universal_newlines=False)
        print return_arg

