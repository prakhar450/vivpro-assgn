from flask import Flask, Blueprint

application = Blueprint('application', __name__)


@application.route("/")
@application.route("/home")
def home():
    # Returning an api for showing in  reactjs
    return {
        'Name': "geek",
        "Age": "22",
        "Date": "x",
        "programming": "python"
    }


if __name__ == '__main__':
    application.run(debug=True)
