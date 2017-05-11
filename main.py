import bluepy.btle as btle
import binascii
import paho.mqtt.client as mqtt

address = "d4:81:ca:23:67:a1"
printoutloud = True
mqtt_server = "mqtt"

class grillDelegate(btle.DefaultDelegate):
 def handleNotification(self, cHandle, data):
  formatedData = binascii.b2a_hex(data)

  if cHandle == 52:
   temperature = int(formatedData[0:len(formatedData)-4],16)
   if printoutloud:
    print "Probe 1: ", temperature, "(Hex Value: ", formatedData[0:len(formatedData)-4], ")"
   client.publish("bbq/probe1", temperature)

  elif cHandle == 57:
   temperature = int(formatedData[0:len(formatedData)-4],16)
   if printoutloud:
    print "Probe 2: ", temperature, "(Hex Value: ", formatedData[0:len(formatedData)-4], ")"
   client.publish("bbq/probe2", temperature)

  elif cHandle == 62:
   temperature = int(formatedData[0:len(formatedData)-4],16)
   if printoutloud:
    print "Probe 3: ", temperature, "(Hex Value: ", formatedData[0:len(formatedData)-4], ")"
   client.publish("bbq/probe3", temperature)

  elif cHandle == 67:
   temperature = int(formatedData[0:len(formatedData)-4],16)
   if printoutloud:
    print "Probe 4: ", temperature, "(Hex Value: ", formatedData[0:len(formatedData)-4], ")"
   client.publish("bbq/probe4", temperature)

  elif cHandle == 82:
   batteryvalue = int(formatedData,16)
   if printoutloud:
    print "Battery: ", batteryvalue, "(Hex Value: ", formatedData, ")"
   client.publish("bbq/battery", batteryvalue)

  else:
   if printoutloud:
    print "Unknown cHandle: ", cHandle, " - Value: ", formatedData
   client.publish("bbq/unknown/handle", cHandle)
   client.publish("bbq/unknown/value", formatedData)

igrill = btle.Peripheral( address )
igrill.setDelegate(grillDelegate())

# MQTT Section
client = mqtt.Client()
client.connect(mqtt_server, 1883, 60)
client.loop_start()

while True:
 if igrill.waitForNotifications(60):
  continue
