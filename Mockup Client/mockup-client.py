import random
import json
import paho.mqtt.client as mqtt
import time

def mockupdata(MAC):
	return { "MAC": MAC, "VL1": random.randint(215, 220), "VL2": random.randint(215, 220),
			 "VL3": random.randint(215, 220), "AL1": random.randint(5, 10), "AL2": random.randint(5, 10), 
			 "AL3": random.randint(5, 10),"P1": random.randint(10, 100), "P2": random.randint(10, 100),
			  "P3": random.randint(10, 100), "AE": random.randint(10, 100)}

def mockupdata1(sensor,MAC):
	return { "MAC": MAC, "s": sensor,"a":random.randint(5, 10) }

def test(MAC):
	return { "MAC": MAC, "a":random.randint(500, 1000) }

def mockupdata2(MAC):
	return { "MAC": MAC, "status": random.randint(0, 1)}


host = "localhost"
port = 1880
client = mqtt.Client()
client.username_pw_set(username="admin",password="password")
client.connect(host,port)
for _ in range(999):

	message = test("AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/my/computer",json.dumps(message))
	print("Publish: {}".format(message))


	message = mockupdata1(1,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(2,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(3,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(4,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(5,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata("AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/dm/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata2("AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/pir",json.dumps(message))
	print("Publish: {}".format(message))
	print("-"*15)


	message = mockupdata1(1,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(2,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(3,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(4,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(5,"AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata("AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/dm/air",json.dumps(message))
	print("Publish: {}".format(message))
	client.publish("/infbuu/IF/2/IF-204/dm/light",json.dumps(message))
	print("Publish: {}".format(message))
	client.publish("/infbuu/IF/2/IF-204/dm/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata2("AA-BB-CC-DD-EE")
	client.publish("/infbuu/IF/2/IF-204/pir",json.dumps(message))
	print("Publish: {}".format(message))
	print("-"*15)


	message = mockupdata1(1,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(2,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(3,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(4,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(5,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata("11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-302/dm/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata2("11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/pir",json.dumps(message))
	print("Publish: {}".format(message))
	print("-"*15)



	message = mockupdata1(1,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(2,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(3,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(4,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(5,"11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata("11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-302/dm/air",json.dumps(message))
	print("Publish: {}".format(message))
	client.publish("/infbuu/IF/3/IF-302/dm/light",json.dumps(message))
	print("Publish: {}".format(message))
	client.publish("/infbuu/IF/3/IF-302/dm/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata2("11-22-33-44-55")
	client.publish("/infbuu/IF/3/IF-304/pir",json.dumps(message))
	print("Publish: {}".format(message))
	print("-"*15)




	message = mockupdata1(1,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(2,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(3,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/light",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(4,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(5,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata("55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/dm/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata2("55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/pir",json.dumps(message))
	print("Publish: {}".format(message))

	message = mockupdata1(1,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(2,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(3,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/air",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(4,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata1(5,"55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/ct/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata("55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/dm/air",json.dumps(message))
	print("Publish: {}".format(message))
	client.publish("/infbuu/IF/6/IF-605/dm/light",json.dumps(message))
	print("Publish: {}".format(message))
	client.publish("/infbuu/IF/6/IF-605/dm/plug",json.dumps(message))
	print("Publish: {}".format(message))
	message = mockupdata2("55-55-55-55-55")
	client.publish("/infbuu/IF/6/IF-605/pir",json.dumps(message))
	print("Publish: {}".format(message))

	time.sleep(300)
