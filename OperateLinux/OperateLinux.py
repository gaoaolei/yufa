
#导入paramiko包
import paramiko
#导入StringIO模块
from io import StringIO
'''
Paramiko包含两个核心组件：SSHClient和SFTPClient。
SSHClient的作用类似于Linux的ssh命令，是对SSH会话的封装，该类封装了传输(Transport)，通道(Channel)及SFTPClient建立的方法(open_sftp)，通常用于执行远程命令。
SFTPClient的作用类似与Linux的sftp命令，是对SFTP客户端的封装，用以实现远程文件操作，如文件上传、下载、修改文件权限等操作。
'''
'''
Paramiko中的几个基础名词：
1、Channel：是一种类Socket，一种安全的SSH传输通道；
2、Transport：是一种加密的会话，使用时会同步创建了一个加密的Tunnels(通道)，这个Tunnels叫做Channel；
3、Session：是client与Server保持连接的对象，用connect()/start_client()/start_server()开始会话。
'''
'''
基于SSHClient类连接服务器
'''
try:
    # 创建sshClient实例对象
    ssh = paramiko.SSHClient()
    # 设置信任远程机器，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #set_missing_host_key_policy
    '''
    设置远程服务器没有在know_hosts文件中记录时的应对策略。目前支持三种策略：
    AutoAddPolicy 自动添加主机名及主机密钥到本地HostKeys对象，不依赖load_system_host_key的配置。即新建立ssh连接时不需要再输入yes或no进行确认
    WarningPolicy 用于记录一个未知的主机密钥的python警告。并接受，功能上和AutoAddPolicy类似，但是会提示是新连接
    RejectPolicy 自动拒绝未知的主机名和密钥，依赖load_system_host_key的配置。此为默认选项
    '''
except:
    print("There is an error with the SSHClient")
try:
    # 设置ssh远程连接机器，参数依次为地址、端口、用户名、密码,ssh端口默认22
    ssh.connect("172.31.28.34",
                "22",
                "root",
                "gyjxwh.com!")
    '''
    connect参数详解：
    hostname 连接的目标主机，该项必填
    port=SSH_PORT 指定端口
    username=None 验证的用户名
    password=None 验证的用户密码
    pkey=None 私钥方式用于身份验证
    key_filename=None 一个文件名或文件列表，指定私钥文件
    timeout=None 可选的tcp连接超时时间
    allow_agent=True, 是否允许连接到ssh代理，默认为True 允许
    look_for_keys=True 是否在.ssh文件夹中搜索私钥文件，默认为True 允许
    compress=False, 是否打开压缩
    '''
    '''
    基于密钥连接
    关于SSH密钥链接大家可以参考我的这篇博客:https://www.cnblogs.com/victoryhan/p/16417898.html
    这里只专注于客户端Python代码的实现。
    #导入私钥
    privateKey = paramiko.RSAKey.from_private_key_file('./id_rsa')
    ssh.connect('ip',22,'username',pkey=privateKey)
    '''
    '''
    基于私钥字符串连接
    #私钥字符串就是私钥的内容，位置在这篇博文里有介绍：https://www.cnblogs.com/victoryhan/p/16417898.html
    keyStr = '[私钥内容]'
    privateKey = paramiko.RSAKey(file_obj=StringIO(keyStr))
    ssh.connect('ip','22','username',pkey=privateKey)
    '''
except:
    print("Failed to connect to remote server")

'''
执行linux命令
'''
for i in range(100):
    try:
        #设置代表需要执行的linux命令的变量，多条命令用分号隔开
        order = "mysql -h172.31.28.34 -P6033 -uctbasecomponent -pctbasecomponent -Dctbasecomponentdb  -e'select *,@@hostname from banner_area limit 1'"
        #每次执行命令会返回三个对象，对应标准输入、标准输出、标准错误。每调用一次exec_command方法就相当于重新打开一次linux终端，终端环境都是新的。
        stdin,stdout,stderr = ssh.exec_command(order)
        #如果使用了sudo命令请启用下面的代码并填入对应的密码
        #stdin.write("passwd")
        #stdin.flush()
        #打印输出结果
        print(stdout.readlines())
        #打印命令执行错误信息
        print(stderr.readlines())
    except:
        print('Fail to carry out command')
#关闭ssh链接
ssh.close()
# '''
# 基于SFTP类文件传输
# '''
# #创建SFTPClient对象、transport通道
# '''
# 上面介绍的验证方法在此处依然适用，将password项改为pkey项即可。此处不在赘述。
# '''
# transport = paramiko.Transport(('ip','22'))
# transport.connect('username','password')
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# #上传
# sftp.put('[localpath]','[remotepath]')
# #下载
# sftp.get('[remotepath]','[localpath]')
# '''
# 常用方法
# put(localpath, remotepath, callback=None, confirm=True) 将本地文件上传到服务器
# 参数confirm：是否调用stat()方法检查文件状态，返回ls -l的结果
# get(remotepath, localpath, callback=None) 从服务器下载文件到本地
# mkdir() 在服务器上创建目录
# remove() 在服务器上删除目录
# rename() 在服务器上重命名目录
# stat() 查看服务器文件状态
# listdir() 列出服务器目录下的文件
# '''
# #关闭transport通道
# transport.close()