import subscribe
import publish
from threading import Thread
import global_var

if __name__ == "__main__":
    global_var._init()
    t1 = Thread(target = subscribe.ICE_connect)
    t2 = Thread(target = publish.ali_iot_connect)
    
    t1.start()
    t2.start()
