import subprocess

a=subprocess.Popen(['/home/fearofchou/Tools/libfm-1.40.src/bin/libFM']\
    ,shell=True,stdout = subprocess.PIPE)
a.wait()

