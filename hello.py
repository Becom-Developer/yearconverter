from flask import Flask
app = Flask(__name__)

# 変数をつくる
index_word = "Hello World! yearconverter word"

# index のテキスト情報
index_html = """<!doctype html>
<html lang="ja">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
  <title>暦変換くん</title>
</head>

<body>
  <section class="jumbotron text-center">
    <div class="container">
      <h1 class="jumbotron-heading">暦変換くん</h1>
      <p class="lead text-muted">西暦と和暦を変換してくれます</p>
      <p>
        <a href="seireki.html" class="btn btn-primary my-2">西暦→和暦</a>
        <a href="wareki.html" class="btn btn-info my-2">和暦→西暦</a>
      </p>
    </div>
  </section>
  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</body>

</html>"""

@app.route('/')
def hello_world():
    # return "Hello World! yearconverter add"
    # return index_word
    # index のテキスト情報を出力
    return index_html

app.debug = True

if __name__ == '__main__':
    app.run()
