from flask import Flask, render_template, request, redirect
import pathlib
import csv

app = Flask(__name__)



@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:pagename>')
def html_page(pagename):
    return render_template(pagename)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        file = database.write(f"\n{name}, {email}, {message}")

def write_to_csv(data):
    with open('database.csv', 'a', newline="") as database2:
        email = data['email']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter =',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "did not save to database"
    else:
        return 'something went wrong stoopid'
