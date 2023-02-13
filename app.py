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

@app.route('/index', methods=['GET', 'POST'])
def index():
    #honbun = request.form["honbun"]
    #print(honbun)
    #generate(honbun, 'dazai_finetune', 100)

    if request.method == "GET":
        with open('gen.txt', 'r+' ,encoding='utf-8') as f:
            f.truncate(0)
        return render_template('index.html')
    elif request.method == "POST":
        textdata = request.form.get("honbun")
        print(textdata)
        generate(textdata, 'dazai_finetune', 100)
        f = open('gen.txt', 'r+' ,encoding='utf-8')
        novel = f.read()
        gassaku= textdata + novel
        return render_template('index.html', gassaku = gassaku)

# @app.route('/syori', methods=['GET', 'POST'])
# def syori():
#     honbun = request.form["honbun"]
#     print(honbun)
#     generate(honbun, 'dazai_finetune')
#     return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)