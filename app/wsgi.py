# -*- coding: utf-8 -*-

from flask import Flask
application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    return 'Hello Docker!'

if __name__ == '__main__':
    application.run(debug=True)
