# 配置邮件内容
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

from_address = '853573584@qq.com'
to_address = 'gaoaolei@km.com'
mail_host = "smtp.qq.com"  # 设置服务器
mail_password = "mjxnwectfmfvbfih"  # 口令

message = MIMEMultipart()
message['From'] = Header('QQ高傲雷<%s>' %from_address,'utf8')
message['To'] = Header('七猫高傲雷<%s>' %to_address,'utf8')
message['Subject'] = Header('这是一封python练习邮件','utf8')
txt_part = MIMEText('这是带附件邮件的文本部分','plain','utf8')
annex_part = MIMEText(open('E:/free100.png','rb').read(),'base64','utf8')
annex_part["Content-Type"] = "application/octet-stream"
annex_part["Content-Disposition"] = "attachment;filename='1234.png'" # 此处邮件名字不能是汉字，不知道为啥
annex_part2= MIMEText(open('E:/report.html','rb').read(),"base64",'utf8')
annex_part2["Content-Type"] = "application/octet-stream"
annex_part2["Content-Disposition"] = "attachment;filename='report.html'" # 此处邮件名字不能是汉字，不知道为啥
message.attach(txt_part)
message.attach(annex_part)
message.attach(annex_part2)


# 配置邮件服务
import smtplib
# s = smtplib.SMTP(mail_host,25)   # 这种走不通，好像qq邮箱必须走安全模式，如下
s = smtplib.SMTP_SSL()
s.connect(mail_host, 465)
s.login(from_address,mail_password)
# 发送邮件
s.sendmail(from_address,to_address,message.as_string())
s.quit()