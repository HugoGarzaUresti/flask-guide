from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
