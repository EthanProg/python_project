import configparser

import pymysql


# 一行一行写文件
# filename 文件名
# str_content 文件内容
def file_Write(file_name, str_content):
    f_point = open(file_name, "a", 2, "utf-8")
    f_point.write(str_content)
    f_point.write('\n')
    f_point.close()


# 读取一个文件中所有的内容 返回list
def file_read(file_name):
    data_list = []
    f_point = open(file_name, "r")
    try:
        lines = f_point.readlines()
        for line in lines:
            data_list.append(line)
    finally:
        f_point.close()

    return data_list


# 读取配置文件属性信息
# file_name 文件名
# key_name 文件中key值
# pro_name 文件属性名称
# pro_type 文件属性类型 默认str 参数为 str int
def read_config(file_name, key_name, pro_name, pro_type="str"):
    cf = configparser.ConfigParser()
    cf.read(file_name)
    if pro_type == 'str':
        return cf.get(key_name, pro_name)
    else:
        return cf.getint(key_name, pro_name)


class DealDataInDb(object):
    host = read_config("datasource.ini", "mysql", "host")
    port = read_config("datasource.ini", "mysql", "port", "int")
    user = read_config("datasource.ini", "mysql", "user")
    password = read_config("datasource.ini", "mysql", "password")
    db_name = read_config("datasource.ini", "mysql", "db_name")

    def __init__(self):
        self.config = {
            'host': DealDataInDb.host,
            'port': DealDataInDb.port,
            'user': DealDataInDb.user,
            'password': DealDataInDb.password,
            'db': DealDataInDb.db_name,
            'charset': 'utf8mb4',
            'cursorclass': pymysql.cursors.DictCursor,
        }

    def sql_insert(self, sql_str, content_str):
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                sql = sql_str
                cursor.execute(sql, content_str)
            connection.commit()
        finally:
            connection.close()
