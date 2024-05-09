import paramiko
ssh = paramiko.SSHClient()     # 创建远程连接实例对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # 自动授权（安全级别较低）
ssh.connect('192.168.159.128', 22, 'gaoaolei', '4209841413pl')

stdin, stdout, stderr = ssh.exec_command('pwd')   # 执行命令并标准输出
print(stdout.read() + stderr.read())

cmd = '''echo 'yuanchengddengluchengongle
adsfadsfakdfnakdfk' > remotelink'''
ssh.exec_command(cmd)

cmd = 'cat remotelink'
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read() + stderr.read())

cmd = 'ls'
stdin, stdout, stderr = ssh.exec_command(cmd)
print(stdout.read() + stderr.read())

stdin, stdout, stderr = ssh.exec_command('pwd;ls;mkdir daiqiaozhen;ls')   # 一次性输入
print(stdout.read() + stderr.read())

sftp = ssh.open_sftp()     # 传输文件
sftp.put(r'c:\1.log', '/home/gaoaolei/1.log')
sftp.get('/home/gaoaolei/a', r'c:\a')
sftp.get('/home/gaoaolei/a', r'd:\b')
sftp.close()
ssh.close()
