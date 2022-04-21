def _init():  # 初始化
    global _global_dict
    _global_dict = {"Led":0}

def set_value(key, value):
    #定义一个全局变量
    _global_dict[key] = value

def get_value(key):
    try:
        return _global_dict[key]
    except:
        print('读取'+key+'失败\r\n')