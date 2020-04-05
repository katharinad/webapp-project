from flask import Flask
# create an app instance
app = Flask(__name__)

# at the end point "/" call method "hello", which returns "hello world"
@app.route("/")
def hello():
    try:  
        return "Hello World!!!"
    except Exception as e:
        print(e)

@app.route("/Katha")
def hello_katha():
    try:  
        return "Hello Katha!!!"
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"),debug=True)