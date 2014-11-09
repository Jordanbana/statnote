from flask import Flask, request
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def root(name="yooooo"):
    return app.send_static_file('website.html')
    #return """<html><body><p>hello world</p></body></html>"""

if __name__ == '__main__':
  app.run()
