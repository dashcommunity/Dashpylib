import os
import subprocess
#run this module while ./dashd is running
class Pydash:


    def __init__(self, dir):
        #check if we are in right directory
        if not os.path.isfile('./dashd'):
            return "error: dir varable is not pointing toward ./dash-cli "
        self.dir = dir


    def command(self, arg):

        splitArg = arg.split()
        return subprocess.Popen(splitArg, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=self.dir, env=None, universal_newlines=False, startupinfo=None, creationflags=0)