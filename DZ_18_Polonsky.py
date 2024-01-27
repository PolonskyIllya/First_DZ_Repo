from flask import Flask

app = Flask(__name__)
counter = 0

@app.route("/", methods = ["GET"])
def get_counter():
    return str(counter)

@app.route("/plus", methods = ["POST"])
def increase_counter():
    global  counter
    counter += 1
    return str(counter)

@app.route("/minus", methods = ["POST"])
def decrease_counter():
    global counter
    counter -= 1
    return str(counter)

if __name__ == "__main__":
    app.run()