import paho.mqtt.client as mqtt
import time
import aliLink
import time,json
import random
import global_var
#flagg = False



def on_connect(client, userdata, flags, rc):
    print("Connected with result code ",rc)


def ali_iot_connect():
    clientId="h2g3TCG357v.raspberrypi|securemode=2,signmethod=hmacsha256,timestamp=1650195417106|"
    username="raspberrypi&h2g3TCG357v"
    password="208058b9e62d41579e68e326477835a170027dddabf0d9a8211f5a4dbf021280"
    mqttHostUrl="iot-06z00aafjgmi1n7.mqtt.iothub.aliyuncs.com"
    port=1883
    POST = '/sys/h2g3TCG357v/raspberrypi/thing/event/property/post'
    global flagg
    
    client = mqtt.Client(clientId)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(mqttHostUrl, 1883, 60)
#    client.loop_forever()

    while(1):
#        data=random.randint(0,20)
        print(global_var.get_value("Led"))
        updateMsn = {
            'pdi':global_var.get_value("Led")
        }
        JsonUpdataMsn = aliLink.Alink(updateMsn)
        client.publish(POST,JsonUpdataMsn,qos=0)
        time.sleep(3)
