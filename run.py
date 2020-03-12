#실제 서비스

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'aws 홈페이지 수정'

if __name__=='__main__':
    app.run(debug=True)