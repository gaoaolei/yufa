import os
import importlib
import hashlib
import json
from OperateDatabase import MysqlData
import GetPath


def get_md5(s):
    """
    md5加密字符串
    :param s:
    :return:
    """
    md5 = hashlib.md5(s.encode(encoding='UTF-8')).hexdigest()
    return md5


def get_func_by_path(func_path):
    """
    通过字符串路径获取可执行方法
    :param func_path:
    :return:
    """
    func_path_list = func_path.rsplit('.', 1)

    try:
        import_package = importlib.import_module(func_path_list[0])
    except ModuleNotFoundError:
        return False
    func = getattr(import_package, func_path_list[1])
    return func


def get_dict_from_kv(kv, sep='\r\n'):
    """
    将键值对字符串转换成dict
    :param kv: 键值对字符串
    :param sep: 不同键值对的分隔符
    :return:
    """

    if sep == '\r\n' and sep not in kv:
        sep = '\n'
    elif sep == '\n' and sep not in kv:
        sep = '\r\n'
    dict_data = {}
    if kv.strip() != '':
        header_list = kv.strip().split(sep)
        for header in header_list:
            if header.strip() != '':
                key_value = header.strip().split(':', 1)
                dict_data[key_value[0].strip()] = key_value[1].strip()
    return dict_data


def get_kv_from_dict(dict_data, sep='\r\n'):
    """
    将字典格式数据转换成键值对字符串
    :param dict_data:
    :return:
    """
    kv = ''
    for key, value in dict_data.items():
        kv += str(key) + ': ' + str(value) + sep
    return kv


def get_value_by_key_path(text, key_path):
    """
    通过key路径形式获取字典中的值
    :param text: 字典形式的数据
    :param key_path: key路径字符串，例如：data>info>id
    :return:
    """
    value = json.loads(text)
    order_list = key_path.split('>')
    for order in order_list:
        value = value[order.strip()]
    return value


def exec_cmd(cmd):
    """
    执行cmd命令并获取打印结果
    :param cmd:
    :return:
    """
    r = os.popen(cmd)
    res = r.read()
    return res


def get_headers(net_env, channel, sys_ver, device_id, platform, app_version):
    headers = '''
net-env: {netenv}
channel: {channel}
is-white: 0
hardware-id: ffffffff-8d61-83d7-ffff-ffffc50eefef
uuid: 00000000-6ee7-9cb3-ffff-ffffe9983c01
device-id: {deviceid}
mac: E0:13:B5:C0:04:E7
platform: {platform}
app-version: {appversion}
sys-ver: {sysver}
reg: 
trusted-id: DuqWHsbFINpRT6SNkslcfZEXe29h4pEDo4bbhrFRdj2grlyUDR5nbv/39uVxiwRlSKaNxaegSkBC+6muQE/SeH6g
imei: 868795049782259
model: V1813BA
wlb-imei: 868795049782259
wlb-uid: 868795049782259
client-id: 41115ae5c02d5198
brand: vivo
oaid: 
application-id: com.kmxs.reader
AUTHORIZATION: 
QM-it: 1551715200
QM-ii: 2886735079
User-Agent: webviewversion/40100

Connection: Keep-Alive
Accept-Encoding: gzip
If-Modified-Since: Fri, 03 Apr 2020 12:46:31 GMT
'''.format(netenv=net_env, channel=channel, sysver=sys_ver, deviceid=device_id, platform=platform,
           appversion=app_version)

    # 需要验证的header
    need_check_header = ['uuid', 'imei', 'platform', 'device-id', 'app-version', 'application-id', 'mac', 'client-id',
                         'brand', 'model', 'sys-ver', 'AUTHORIZATION', 'channel', 'wlb-imei', 'reg', 'Authorization',
                         'is-white', 'hardware-id', 'trusted-id', 'oaid', 'wlb-uid', 'net-env']

    headers = get_dict_from_kv(headers, '\n')

    secretKey = 'd3dGiJc651gSQ8w1'  # 秘钥
    sign = ''
    need_check_header = sorted(need_check_header)  # 需要正序排列再加密
    for key in need_check_header:
        if headers.__contains__(key):
            if key == 'Authorization':  # ios是小写需要转换成大小
                sign += '{}={}'.format(key.upper(), headers[key])  # 拼接键值对
            else:
                sign += '{}={}'.format(key, headers[key])  # 拼接键值对
    sign += secretKey  # 拼接秘钥
    sign = get_md5(sign)  # md5加密
    headers['sign'] = sign
    return headers


# 根据device_id  md5加密计算手机user_area
def get_user_area(device_id):
    result = get_md5(device_id)
    result = result[-2:]
    user_area = int(result, 16)
    return user_area


# 根据app_versoin获取min_app_version
def get_min_app_version(app_version, area_config_id, platform):
    sql = 'select min_app_version from adv_version where area_config_id=%s and platform=%s and app_type=0' % (
        area_config_id, platform)
    mysql = MysqlData()
    data = mysql.getdata(sql)
    min_app_version_list = []
    for i in data:
        min_app_version_list.append(i[0])
    min_app_version_list_tmp = sorted(min_app_version_list, reverse=True)
    min_app_version = 0  # 默认值
    for j in min_app_version_list_tmp:
        if app_version >= j:
            min_app_version = j
            break
    return min_app_version


def get_abgroup_data(device_id, area_config_id, platform, app_version):
    user_area = get_user_area(device_id)
    min_app_version = get_min_app_version(app_version, area_config_id, platform)
    sql = "SELECT * FROM adv_ab WHERE area_config_id=%s AND platform=%s AND STATUS=0 AND \
    start_at<UNIX_TIMESTAMP(NOW())AND min_app_version=%s " % (area_config_id, platform, min_app_version)
    mysql = MysqlData()
    data = mysql.getdata(sql)  # 最多一条数据

    # 参数默认值
    ab_data = {
        'id': '',
        'plan_name': '',
        'platform': platform,
        'area_config_id': area_config_id,
        'min_app_version': min_app_version,
        'max_app_version': '',
        'groups': '',
        'start_at': '',
        'end_at': '',
        'remark': '',
        'conclusion': '',
        'statistical_code': '',
        'status': '',
        'updated_at': '',
        'created_at': '',
        'group_id': '',
        'group_name': '',
        'index': '0',
        'user_area': '',
        'price': '',
        'page_num': '',
        'form_type': '',
        'coopen_form_type': '',
        'interval_time': '',
        'show_total': ''
    }

    if data != []:
        i = 0
        groups = json.loads(data[0][7])
        for group in groups:
            if str(user_area) in group['user_area'].split(','):
                ab_data['id'] = data[0][0]
                ab_data['plan_name'] = data[0][1]
                ab_data['plan_key'] = data[0][2]
                # ab_data['platform'] = data[0][3]
                # ab_data['area_config_id'] = data[0][4]
                # ab_data['min_app_version'] = data[0][5]
                ab_data['max_app_version'] = data[0][6]
                ab_data['groups'] = data[0][7]
                ab_data['start_at'] = data[0][8]
                ab_data['end_at'] = data[0][9]
                ab_data['remark'] = data[0][10]
                ab_data['conclusion'] = data[0][11]
                ab_data['statistical_code'] = data[0][12]
                ab_data['status'] = data[0][13]
                ab_data['updated_at'] = data[0][14]
                ab_data['created_at'] = data[0][15]

                ab_data['group_id'] = groups[i]['group_id']
                ab_data['group_name'] = groups[i]['group_name']
                ab_data['index'] = groups[i]['index']
                # 非必须字段判空
                try:
                    ab_data['price'] = groups[i]['price']
                except Exception as e:
                    ab_data['price'] = ''
                else:
                    ab_data['price'] = groups[i]['price']

                try:
                    ab_data['page_num'] = groups[i]['page_num']
                except Exception as e:
                    ab_data['page_num'] = ''
                else:
                    ab_data['page_num'] = groups[i]['page_num']

                try:
                    ab_data['form_type'] = groups[i]['form_type']
                except Exception as e:
                    ab_data['form_type'] = ''
                else:
                    ab_data['form_type'] = groups[i]['form_type']

                try:
                    ab_data['coopen_form_type'] = groups[i]['coopen_form_type']
                except Exception as e:
                    ab_data['coopen_form_type'] = ''
                else:
                    ab_data['coopen_form_type'] = groups[i]['coopen_form_type']

                try:
                    ab_data['interval_time'] = groups[i]['interval_time']
                except Exception as e:
                    ab_data['interval_time'] = ''
                else:
                    ab_data['interval_time'] = groups[i]['interval_time']

                try:
                    ab_data['show_total'] = groups[i]['show_total']
                except Exception as e:
                    ab_data['show_total'] = ''
                else:
                    ab_data['show_total'] = groups[i]['show_total']

                break
            i = i + 1
    return ab_data


# 最终的查询adv表的sql语句
def sql(device_id, area_config_id, platform, app_version):
    ab_data = get_abgroup_data(device_id, area_config_id, platform, app_version)
    sql = "SELECT * FROM adv WHERE app_type=0 and area_config_id=%s AND platform=%s AND STATUS=1 AND min_app_version=%s AND ab_group_id=%s AND adv_code !=''"
    # ab['group_id']=''时，sql会是AND ab_group_id= AND adv_code !=''，会报错，改成用sql，params的形式
    params = [area_config_id, platform, ab_data['min_app_version'], ab_data['group_id']]

    return sql, params


# 渠道屏蔽
def channel_filter(allow_channel, deny_channel, channel):
    '''如果对advs处理会有两次（GetMysqlData和用例）循环，影响效率，因此对adv处理，只在用例中判断'''
    flag = False
    if allow_channel != '':
        a = allow_channel.split(',')
        b = []
        for i in a:
            j = i.strip()
            b.append(j)
        if channel not in b:
            flag = True

    if deny_channel != '':
        c = deny_channel.split(',')
        d = []
        for m in c:
            n = m.strip()
            d.append(n)
        if channel in d:
            flag = True
    return flag


# 大屏蔽


# vip
def is_vip(token):
    return False


# 根据网络环境返不同的id
def net(list, net_env):
    '''list是adv_code的列表'''
    list2 = []
    for i in list:
        j = i.split(';')
        if len(j) == 1:
            list2.append(j[0])
        else:
            if net_env == 1:
                list2.append(j[1])
            else:
                list2.append(j[0])
    return list2


def zhangnei_form_type(app_version, area_config_id, platform):
    min_app_version = get_min_app_version(app_version, area_config_id, platform)
    sql = "select value from global_setting where `key` = 'adMiddle'"
    mysql = MysqlData()
    data = mysql.getdata(sql)
    form_type = json.loads(data[0][0])[0]['1'][str(min_app_version)]['form_type']
    return form_type


def write_result(content):
    resultFile = os.path.join(GetPath.get_Path(), r'result\result.txt')
    with open(resultFile, 'a', encoding='utf-8') as f:
        f.write(content)
    resultFile = os.path.join(GetPath.get_Path(), r'result\resultbackup.txt')
    with open(resultFile, 'a', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    # a = get_headers(1,'unknown', 9, '20190712141352c5590aeffbbec19d7b474f3958f971c8018c311326c075ea', 'android', 40100)
    # print(a)
    zhangnei_form_type(40200, 30, 1)
