import os
from flask import (
     Flask, 
     request, 
     render_template)

from generate import generate
app = Flask(__name__,static_url_path='/static') #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

@app.route('/')
def top():
    return  render_template('top.html')

@app.route('/index')
def index():
    return  render_template('index.html')

@app.route('/syori', methods=['GET', 'POST'])
def syori():
    honbun = request.form["honbun"]
    print(honbun)
    generate(honbun, model)
    return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)