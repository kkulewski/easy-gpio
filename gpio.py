from flask import Flask
app = Flask(__name__)
import os


@app.route("/gpio<number>/export")
def gpioExport(number):
	cmd = 'echo {} > /sys/class/gpio/export'.format(number)
	os.system(cmd)
	return "gpio{} exported".format(number)

@app.route("/gpio<number>/unexport")
def gpioUnexport(number):
	cmd = 'echo {} > /sys/class/gpio/unexport'.format(number)
	os.system(cmd)
	return "gpio{} unexported".format(number)


@app.route("/gpio<number>/direction")
def gpioDirectionRead(number):
	cmd = 'cat /sys/class/gpio/gpio{}/direction'.format(number)
	direction = os.popen(cmd).read()
	return "gpio{} direction == {}".format(number, direction)

@app.route("/gpio<number>/direction/<direction>")
def gpioDirectionSet(number, direction):
	cmd = 'echo {} > /sys/class/gpio/gpio{}/direction'.format(direction, number)
	os.system(cmd)
	return "gpio{} direction set {}".format(number, direction)


@app.route("/gpio<number>/value")
def gpioValueRead(number):
	cmd = 'cat /sys/class/gpio/gpio{}/value'.format(number)
	state = os.popen(cmd).read()
	return "gpio{} value == {}".format(number, state)

@app.route("/gpio<number>/value/<state>")
def gpioValueSet(number, state):
	cmd = 'echo {} > /sys/class/gpio/gpio{}/value'.format(state, number)
	os.system(cmd)
	return "gpio{} value set {}".format(number, state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)