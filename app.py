import os
from flask import (
     Flask, 
     request, 
     render_template)

from generate import generate
app = Flask(__name__, static_url_path='/static') #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

@app.route('/')
def top():
    return  render_template('top.html')

@app.route('/index/<sakka>', methods=['GET', 'POST'])
def index(sakka):
    #honbun = request.form["honbun"]
    #print(honbun)
    #generate(honbun, 'dazai_finetune', 100)

    if request.method == "GET":
        with open('gen.txt', 'r+' ,encoding='utf-8') as f:
            f.truncate(0)
        return render_template('index.html', sakka = sakka)
    elif request.method == "POST":
        textdata = request.form.get("honbun")
        with open('gen.txt', 'w' ,encoding='utf-8') as f:
            f.write(textdata)
            print(textdata)
        generate(textdata, 'dazai_finetune_500', 100)
        with open('gen.txt', 'r+' ,encoding='utf-8') as f:
            novel = f.read()
            #gassaku= textdata + novel
        return render_template('index.html', gassaku = novel, sakka = sakka)

# @app.route('/syori', methods=['GET', 'POST'])
# def syori():
#     honbun = request.form["honbun"]
#     print(honbun)
#     generate(honbun, 'dazai_finetune')
#     return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)