import configparser
import os

def get_conf():
    conf_file = configparser.ConfigParser()

#os.path.join(path,name)   #连接目录与文件名或目录 结果为path/name
    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))

    conf = {}
    conf["lg_url"] = conf_file.get("login","url")

    conf["info_url"] = conf_file.get("userinfo","url")

    conf['sender'] = conf_file.get("email","sender")

    conf['receiver'] = conf_file.get("email","receiver")

    conf['smtpserver'] = conf_file.get("email","smtpserver")

    conf['username'] = conf_file.get("email","username")

    conf['password'] = conf_file.get("email","password") 
    print(conf)
    return conf

if __name__ == "__main__":
    get_conf()
