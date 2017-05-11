# iGrill_bbqmqtt
Monitor your iGrill_v2 (with a Raspberry Pi 1/2/3) - and an forward it to an mqtt-server

## What do you need
### Hardware
* iGrill2 Device (and at least one probe) - [Weber Homepage - DE](http://www.weber.com/DE/de/zubehoer/werkzeuge/-igrill/7221.html)
* A bluetooth enabled computer - preferable a raspberry pi

### Software
* [bluepy](https://github.com/IanHarvey/bluepy)
* [paho mqtt](https://pypi.python.org/pypi/paho-mqtt/1.1)

## Installation
### iGrill
1. Start the Origianl iGrill app ( [iOS](https://itunes.apple.com/at/app/weber-igrill/id400796680?mt=8) | [Android](https://play.google.com/store/apps/details?id=com.weber.igrill) and connect it with your iGrill. 
1. Set an alarm (please refer to the apps manual how to do that) for any of the connected probes to an fantastic value (e.g. 500° Celsius in my case).
*This probe don't has to be connected the whole time - we also just need one alarm* 
### Receiver (e.g. Raspberry Pi)
1. Create a folder in /opt/igrill
1. Copy the main.py to /opt/igrill
*If you have a system running systemd please proceed - otherwise you have to start it manually or create your own startup script*
1. Copy the igrill.server file to your systemd path (e.g. /lib/systemd/system)
1. `systemctl daemon-reload`
1. `systemctl start igrill` 
(if it starts proper you can enable the in at boot-time with the command `systemctl enable igrill`

## Troubleshooting
Sometimes the iGrill does not send any values to the receiver - this mostly happens after a longer shutted down period.
* Stop the service/process (or just shut it down) - the Bluetooth LED on the iGrill will start to blink. 
* Start the Origianl iGrill app ( [iOS](https://itunes.apple.com/at/app/weber-igrill/id400796680?mt=8) | [Android](https://play.google.com/store/apps/details?id=com.weber.igrill) and connect it with your iGrill. 
* Set an alarm (please refer to the apps manual how to do that) for any of the connected probes to an fantastic value (e.g. 500° Celsius in my case). 
* Finally disconnect your smartphone from the iGrill and start the service/process (or device) again
