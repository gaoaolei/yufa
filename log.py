# import pymysql
#
# conn = pymysql.connect(user='ceshi',  # The first four arguments is based on DB-API 2.0 recommendation.
#         password="ceshi",
#         host='172.31.24.21',
#         database='galaxy_luna',
#         unix_socket=None,
#         port=3306,)
#
# cur = conn.cursor()
# for i in range(1):
#         cur.execute("insert into `query_write_off` (`part_id`, `gmt_create`, `gmt_modified`, `record_status`, "
#                     "`out_prize_id`, `user_prize_id`, `app_id`, `sync_time`) values('8',NOW(),NOW(),'0',"
#                     "'202209270007300217650DHGVU1T','734644992255496192','2018062860457318',NOW());"
#         )
#         conn.commit()

import pymysql

conn = pymysql.connect(user='dsp',  # The first four arguments is based on DB-API 2.0 recommendation.
                       password="dsp",
                       host='172.31.24.50',
                       database='dsp_db',
                       unix_socket=None,
                       port=3306, )

import random

for j in range(220000,223521):
    i = random.randint(30,100)
    print(i)
    cur = conn.cursor()
    cur.execute("UPDATE qcj_statistics_advert_hour SET advert_show_pv = %s where id = %s;" % (i, j))
    conn.commit()
