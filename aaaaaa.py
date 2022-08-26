# from pymemcache.client.base import Client
#
# mc = Client(('172.32.3.63', 11211))
# print(mc.get('2088412914365175_ct_new_exhibitionFlag'))
#


users = ['gaoaolei','luomengxia','zhouqinghui']
user_map = dict()
#
for user in users:
    user_map[user] = {
        'bug_close_nums': 0,
        'bug_open_nums': 0,
        'bug_nums': 0,
        'case_nums': 0,
        'worktime_nums': 0,
        'demand_nums': 0
    }
print(user_map)
user_map['wenyuan']['bug_nums'] += 3

