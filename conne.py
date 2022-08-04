import paramiko


class FtpService(object):

    @classmethod
    def ftp_connect(cls, hostname):
        hostname = hostname
        port = 22
        username = "root"
        password = "gyjxwh.com!"

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password, compress=True)
        return client

    @classmethod
    def get_command(cls, args, key, module):
        'this is get the command the args to return the command'
        path = '/log/marketing-test01/{module}/common-default-{module}-test-{module}-deployment-*.log'.format(
            module=module
        )
        # grep ac2007f5202109111310000797abddb2 path
        cmd = '%s %s %s' % (args, key, path)
        return cmd

    @classmethod
    def get_cmd_result_list(cls, conn, cmd):
        stdin, stdout, stderr = conn.exec_command(cmd)
        lines = stdout.readlines()
        result =[]
        for line in lines:
            result.append(line.strip())
        return result

    @classmethod
    def get_cmd_result_text(cls, conn, cmd):
        stdin, stdout, stderr = conn.exec_command(cmd)
        result = stdout.read().decode('utf-8')
        return result

f = FtpService()
c = f.ftp_connect("172.31.24.11")
r = f.get_cmd_result_text(c, "kubectl get pods -o json -n gyjx-marketing-test01")
# print(r)
print(type(r))
import json
d = json.loads(r)
# print(d)
for i in d['items']:
    print(i)
    # print(i['status']['containerStatuses'][0].get('name'))
    print(i['status']['containerStatuses'][0]['name'])
