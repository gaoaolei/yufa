import subprocess
ret = subprocess.check_output('dir', shell=True)
print(ret.decode('gbk'))
print(ret)
