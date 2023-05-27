from flask import Flask, render_template, request
from pymongo import MongoClient 
import datetime

app = Flask(__name__)
uri = "mongodb+srv://nhkhan7773:3kwaPuB77gvtJJK1@cluster0.mdmusq4.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)
db = client["rewind_db"]
collection = db["journals"]

@app.route("/")
def index():
    documents = list(collection.find().sort("_id", -1).limit(3))
    return render_template('index.html', documents = documents)

@app.route("/save", methods=['POST'])
def save_text():
        today = datetime.datetime.today()
        text = request.form.get('text')
        if text:
            document = {
                "entry": text,
                "date": today
            }
            result = collection.insert_one(document)
            return "Text saved successfully"          
        else:
             return "No text provided"

if __name__ == "__main__":
    app.run(debug=True)
