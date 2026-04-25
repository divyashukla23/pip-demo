from flask import Flask 
app = Flask(__name__) 
@app.route("/") 
def home(): 
    return "Hello from Python + pip! this is using FLASK" 
if __name__ == "__main__": 
    app.run(port=5000)