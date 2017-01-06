import os
from subprocess import check_output
from time import sleep
from json import loads
from shlex import split
#run this module while ./dashd is running
class Dashpylib:


    def __init__(self, dir):
        #check if global var, dir has ./dash-cli in the directory dir is pointing at
        assert (not os.path.isfile('./dash-cli')), "global var 'dir', is not pointing toward a directory with ./dash-cli in it. or is file is under a different name? "
        self.dir = dir


    def command(self, arg):
        #splits args into individual strings to work with shell syntax, using shlex
        splitArg = arg.split()
        x = True
        while x:
            sleep(.1)
            turp = check_output(splitArg, shell=False, cwd=self.dir, )
            if turp == None:
                pass
            else:
                x = False
                new = turp.translate(None, "\n")
                return loads(new)
