# easy-gpio
Easy, remote GPIO control via sysfs using Flask Web API

## Setup
Add execute privilege
- `chmod 711 gpio.py`

Run as superuser
- `sudo python gpio.py`

You can also redirect stderr to a file and run server in the background
- `sudo python gpio.py 2> gpio.log &`

## Usage
Export GPIO to userspace
- `device-ip/gpioX/export`

Set direction (in or out)
- `device-ip/gpioX/direction/out`

Set value (0 or 1)
- `device-ip/gpioX/value/1`

Check value
- `device-ip/gpioX/value`

Unexport GPIO
- `device-ip/gpioX/unexport`

## Concrete example
Raspberry Pi 3 will serve as an example device. 192.168.0.100 is the IP address assigned to the device.

Find pair of GPIOs using [official pinout](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/). 

I have chosen GPIO2 and GPIO3 and connected them using jumper cable.
GPIO2 will be set as an output, and GPIO3 as an input - this way, I will be able to change GPIO3 value using GPIO2.

Export GPIO2 and GPIO3
- `192.168.0.100/gpio2/export`
- `192.168.0.100/gpio3/export`

Set GPIO2 as output, GPIO3 as input
- `192.168.0.100/gpio2/direction/out`
- `192.168.0.100/gpio3/direction/in`

Set GPIO2 value to 1, then check GPIO3 value (1 if connected properly)
- `192.168.0.100/gpio2/value/1`
- `192.168.0.100/gpio3/value`

Set GPIO2 value to 0, notice that GPIO3 value has changed too
- `192.168.0.100/gpio2/value/0`
- `192.168.0.100/gpio3/value`

You can use these GPIOs to turn on/off and control devices, blink LEDs etc.
