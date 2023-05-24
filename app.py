from flask import Flask, render_template, request
import datetime
app = Flask(__name__)
@app.route("/")
def index():
    with open("output.txt", "r") as file:
        content = file.read()
    return render_template('index.html', content = content)

@app.route('/save', methods=['POST'])
def save_text():
    today = datetime.date.today()
    text = request.form.get('text')
    if text:
        with open('output.txt', 'a') as file:
            file.write(f"{text} {today}\n")
        return "Text saved successfully!"
    else:
        return "No text provided"



if __name__ == "__main__":
    app.run(debug=True)
