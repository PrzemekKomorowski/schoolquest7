from flask import Flask, render_template, url_for, request, redirect
import data_handler

app = Flask(__name__)


@app.route("/", methods=['GET'])
def main_page():
    return render_template('list.html')


@app.route('/question')
def question():
    pass


@app.route('/add-question')
def add_question():
    return render_template('add-question.html')


@app.route('/add-question', methods=['POST'])
def get_data():

    title = request.form['title']
    user_question = request.form['question']

    data_handler.save_data(title, user_question)
    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=9000,
        debug=True,
    )
