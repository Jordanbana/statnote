# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return websites.html
#
# if __name__ == "__main__":
#     app.run()


# from flask import Flask, request
# # set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='')
#
# @app.route('/')
# def root():
#     return app.send_static_file('website.html')
#
#
# if __name__ == "__main__":
#     app.run()


from flask import Flask, request
app = Flask(__name__, static_url_path='')

@app.route('/index/')
def root():
    return app.send_static_file('websites.html')

if __name__ == '__main__':
  app.run()
