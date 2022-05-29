from flask import Flask, render_template, url_for, request, redirect
app=Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def about(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        result_data = "\nEmail " + data['email'] + " Subject " + data['subject'] + " Message " + data['message']
        file = open('database.txt','a')
        file.write(result_data)
        file.close()
        return redirect('/thankyou.html')
    else:
        return "Something went wrong. Try again!"

