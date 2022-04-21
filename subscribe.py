import paho.mqtt.client as mqtt
import json
import global_var
flagg=False
def on_connect(client, userdata, flags, rc):
        print("Subscribe Connected with result code ",rc)
        client.subscribe("/ICE3/port/1/pdi")

def on_message(client, userdata, msg):
        global flag
        global flagg
        dict_json = json.loads(msg.payload)
#        print(dict_json["raw"][0])
        flag= dict_json["raw"]
        if flagg!= flag:
            flagg=flag
            global_var.set_value("Led",flagg)
            """if flagg:
                global_var.set_value("Led",flagg)
            else:
                global_var.set_value("Led",0)"""
#            print(global_var.get_value("Led"))

def ICE_connect():

    clientId="raspberrypi"
    username="leo"
    password="leo"
    mqttHostUrl="localhost"
    port=1883
    
    client = mqtt.Client(clientId)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(mqttHostUrl, port, 60)
    client.loop_forever()
