import bluepy.btle as btle
import binascii
import paho.mqtt.client as mqtt

# Please insert your details here
address = "d4:81:ca:12:12:12"
printoutloud = False
mqtt_server = "mqtt"
# Stop editing here - unless you know what you do ;-)

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

igrill = btle.Peripheral( address )
igrill.setDelegate(grillDelegate())

# MQTT Section
client = mqtt.Client()
client.connect(mqtt_server, 1883, 60)
client.loop_start()

while True:
 if igrill.waitForNotifications(60):
  continue
