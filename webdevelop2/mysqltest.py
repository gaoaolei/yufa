import mysql.connector

def check(yuju):
    conn = mysql.connector.connect(user='qimao_free_test',password='d3R6d190ZXN0Cg==',host='172.16.100.93',port='3306',database='qimao_free')
    cursor = conn.cursor()
    cursor.execute(yuju)
    result = cursor.fetchall()
    return result
print check('select nickname from user limit 10')