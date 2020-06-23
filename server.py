from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database_txt:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file_txt = database_txt.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database_csv:
        email=data['email']
        subject=data['subject']
        message=data['message']
        file_csv = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_csv.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong ... try again!'

# VERSÃO COM AS PÁGINAS HTML descriminadas por funções.... OLD
#
# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
