from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

# <=============== THIS IS A DINAMIC ALTERNATIVE TO WHAT IS BELOW ===========================>
@app.route('/<string:page_name>')
def html_pages(page_name):
	return render_template(page_name)
# <=========== x ==== THIS IS A DINAMIC ALTERNATIVE TO WHAT IS BELOW ==============x==========>

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_file(data)
		write_to_csv(data)
		return redirect('/thank_u.html')
	else:
		return 'somethin wong'

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
	with open('database.csv', newline='\n',mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])



# @app.route('/about.html')
# def about():
# 	return render_template('about.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')

# @app.route('/contact.html')
# def contact():
# 	return render_template('contact.html')

# @app.route('/works.html')
# def works():
# 	return render_template('works.html')

# @app.route('/index.html')
# def home():
# 	return render_template('index.html')