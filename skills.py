def main():
    print("This is a module that contains a list of skills.")


def sumNumbers():
    print(1 + 1)

# Create a web server
# Path: webserver.py
from flask import Flask
app = Flask(__name__)

@app.route("/")

if __name__ == "__main__":
    main()
