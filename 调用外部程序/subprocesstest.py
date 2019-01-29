# subprocess中的check_output,检出输出
# from subprocess import check_output
import subprocess
ret = subprocess.check_output('dir', shell=True, encoding='gbk')     # 返回码为字节流
# 且系统我中文Windows系统，所以要用gbk编码
print(ret)



