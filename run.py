# #실제 서비스

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'aws 홈페이지'

# if __name__=='__main__':
#     app.run(debug=True)
import os
from bs_corona.BusanCorona import wsgi
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BusanCorona.settings')
app = get_wsgi_application()
