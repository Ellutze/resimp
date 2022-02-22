
import subprocess
    
def cmd2(command,RTMFile=""):
    #Passes command to command line.
    #Required due to Visual-RTM having it's own library of python packages.
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd="C:\\Program Files\\ESI Group\\Visual-Environment\\17.0\\Windows-x64")
    proc_stdout = process.communicate()#[0].strip()
    print(command)
    print(proc_stdout)
    
cmd2("VEBatch -activeconfig Trade:CompositesandPlastics -activeapp VisualRTM -sessionrun D:\\VEt\\rc_13.py")