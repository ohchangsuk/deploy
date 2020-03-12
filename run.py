#실제 서비스

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '운동 화이뜌'

if __name__=='__main__':
    app.run(debug=True)