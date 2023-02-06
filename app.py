from flask import Flask

app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

@app.route('設定したいパス')
def 関数名():
    (処理の内容)
    return "表示したい内容"

@app.route('設定したいパス')
def 関数名():
    (処理の内容)
    return "表示したい内容"

@app.route('設定したいパス')
def 関数名():
    (処理の内容)
    return "表示したい内容"

if __name__ == "__main__":
    app.run(debug=True)