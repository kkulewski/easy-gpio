from flask import Flask
app = Flask(__name__)
import os

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