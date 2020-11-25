from flask import Flask
from asuswrt import AsusWRT
from . import config
import sys
sys.path.append('../')

app = Flask(__name__)

@app.route('/')
def index():
    router = AsusWRT(url='http://192.168.1.1', username=config.username, password=config.password)
    sys = router.get_sys_info()

    result = 'Model: %s' % sys['model']
    # print('Firmware: %s' % sys['firmware'])
    return result
@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)