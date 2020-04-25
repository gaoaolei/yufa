

# 配置邮件内容
from email.mime.text import MIMEText
from email.header import Header

from_address = '853573584@qq.com'
to_address = 'gaoaolei@km.com'
mail_host = "smtp.qq.com"  # 设置服务器
mail_password = "mjxnwectfmfvbfih"  # 口令

txt = \
'''<html>
<body>
<h1>Hello</h1>
<p style="font-size:30px;color:orange">
    Welcome to python website <a href="http://www.python.org">Python链接</a>...
</p>
</body>
</html>
'''
message = MIMEText(txt,'html','utf8')
message['From'] = Header('QQ高傲雷<%s>' %from_address,'utf8')
message['To'] = Header('七猫高傲雷<%s>' %to_address,'utf8')
message['Subject'] = Header('这是一封python练习邮件','utf8')

# 配置邮件服务
import smtplib
# s = smtplib.SMTP(mail_host,25)   # 这种走不通，好像qq邮箱必须走安全模式，如下
s = smtplib.SMTP_SSL()
s.connect(mail_host, 465)
s.login(from_address,mail_password)
# 发送邮件
s.sendmail(from_address,to_address,message.as_string())
s.quit()