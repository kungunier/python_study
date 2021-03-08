# 使用Python发送邮件

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

# smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
# 这里是上面语法的参数细节 -
#     host - 这是运行SMTP服务器的主机。可以指定主机的IP地址或类似yiibai.com的域名。这是一个可选参数。
#     port - 如果提供主机参数，则需要指定SMTP服务器正在侦听的端口。通常这个端口默认值是：25。
#     local_hostname - 如果SMTP服务器在本地计算机上运行，那么可以只指定localhost选项。
# SMTP对象有一个sendmail的实例方法，该方法通常用于执行邮件发送的工作。它需要三个参数 -
#     sender - 具有发件人地址的字符串。
#     receivers - 字符串列表，每个收件人一个。
#     message - 作为格式如在各种RFC中指定的字符串

try:
    # 实例化smtp对象
    smtp = smtplib.SMTP('smtp.163.com')
    # 连接邮箱服务器
    # smtp.connect('smtp.163.com')
    # 邮箱账户和密码
    smtp.login('liuhailong0511','L11h37L40')
    # 发送邮件
    # sender - 具有发件人地址的字符串
    # receivers - 字符串列表，每个收件人一个
    # message - 作为格式如在各种RFC中指定的字符串
    sender = 'liuhailong0511@163.com'
    receviers = ['liuhailong@motie.com']
    message = MIMEMultipart()
    message['From'] = formataddr(['liuhailong0511@163.com'])
    message['To'] = ','.join(receviers)
    subject = '自动化测试报告'
    message['Subject'] = Header(subject,'UTF-8')
    message['Accept-Language'] = 'zh-CN'
    message['Accept-Charset'] = 'ISO-8859-1,utf-8,gbk'
    # 邮件正文
    message.attach(MIMEText('自动化测试结果','plain','UTF-8'))
    smtp.sendmail(sender,receviers,message.as_string())
    smtp.quit()
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败',e)