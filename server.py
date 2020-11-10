from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('flskserver/database.txt', mode='a') as database:
#         email=data["email"]
#         subject=data["subject"]
#         message=data["message"]
#         file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('flskserver/database.csv', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        print(data)
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
           data = request.form.to_dict()


           write_to_csv(data)
           return redirect('Thank you.html')
        except:
            return 'did not save to db'
    else:
        return 'something went wrong'

# @app.route('/blog.html')
# def blog():
#     return render_template('blog.html')
#
# @app.route('/marketing.html')
# def marketing():
#     return render_template('/marketing.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/blog')
# def blog():
#     return "blog"

# @app.route('/blog/2020/dogs')
# def blog2():
#     return "dog"
#
# if __name__== "__main__":
#     app.run()

# Running a flask app
# export FLASK_APP= projectname.py
# flask run
# copy the ip


# py -3 -m venv venv

# for activating virtual env
# venv\scripts\activate
