# NAME

yearconverter - 西暦と和暦を変換して表示するアプリ

# SYNOPSIS

## URL

- GET - /index - TOP画面
- GET - /seireki - 西暦→和暦画面
- GET - /wareki - 和暦→西暦画面
- GET - /result - 結果表示画面

## SETUP

__事前のセットアップについて__

## START APP

__アプリケーションの起動__

### LOCAL

__手元のPCでのアプリの起動__

### DEVELOPMENT

__開発環境でのアプリケーションの起動__

## TEST

__動作確認、テストについて__

## WORK

__開発の流れ__

# TODO

```
開発にあたり調査したことなどをメモ
```

```
(パイソンがインストールされているかを確認)
$ which python
/usr/bin/python

(mac はデフォルトで2系のパイソンが入っているので、今回は3系をつかう)
$ which python3
/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
(3系は python3 コマンドとしておく、アナコンダを使うと python で 3系が入るので注意 )

$ python3 -V
Python 3.6.2
(バージョンを念のため確認)

(venv を使った利用方法で実行)
(アプリのディレクトリへ移動)
$ cd ~/github/yearconverter/
(ycenv のところは任意の名前でもかまわない)
(今回はアプリ名が yearconverter なので ycenv)

(venv環境の作成)
$ python3 -m venv ycenv

(venv環境の有効化)
$ source ycenv/bin/activate
(ycenv) $

(無効化)
(ycenv) $ deactivate
```

__Flask install__

Flask を始めとする必要なパッケージ一式のインストール実行

__解説__

```
pip インストールする場合一つ一つ指定してインストールするのは間違いがおこりやすいので
インストールするべきものをメモしてまとめて実行する
その場合
requirements.txt
という名前を作ってそのファイルを読み込んで実行させるやり方。
```

```
(ディレクトリのパスは読み換えて)
$ cd ~/github/yearconverter/
$ cat requirements.txt
Flask==1.0.2
...

(履歴からパッケージを再現)
$ source ycenv/bin/activate

(ycenv) $ cat requirements.txt 
Flask==1.0.2
(ycenv) $ pip install -r requirements.txt
Collecting Flask==1.0.2 (from -r requirements.txt (line 1))
...
Successfully installed Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24
(成功したが、pip をアップグレードせよとメッセージがあるのでやっておく)
You are using pip version 9.0.1, however version 10.0.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
$ pip install --upgrade pip
...
Successfully installed pip-10.0.1

(ライブラリをインストールした後は .gitignore を更新することを忘れないように)
```

__とりあえず動くものをつくる__

<https://a2c.bitbucket.io/flask/quickstart.html>

```
(こういう内容のテキストファイルをつくる)
$ cd ~/github/yearconverter/
$ cat hello.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```

```
$ FLASK_APP=hello.py flask run
```

```
(http://localhost:5000/)
(ycenv) $ FLASK_APP=hello.py flask run
(もしくは)
(ycenv) $ python3 hello.py
(こちらで起動)

(終了時は control + c で終了)

(ycenv) $ FLASK_APP=hello.py flask run

(無効化)
(ycenv) $ deactivate
```

__基本的な仕組みはwebサーバーからシンプルテキストを吐き出している__

```
(言語にかかわらず、コーディング内容を日本語で書いておく)
(例えば)

# index の内容を出力する

# index のテキスト情報

# index のテキスト情報を出力

```

```
(リスエストするURLをつくる)
こちらを参考にしてみる
https://github.com/Becom-Developer/iteenscore/blob/master/doc/iteenscore/controller/auth.md
```

# SEE ALSO

- <> - 
