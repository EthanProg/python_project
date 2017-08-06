import configparser


def parse_args(filename):
    cf = configparser.ConfigParser()
    cf.read(filename)

    _ip = cf.get("mysql", "host")
    print(_ip)


if __name__ == '__main__':
    parse_args("datasource.ini")