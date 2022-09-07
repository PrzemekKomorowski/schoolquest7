from flask import Flask, render_template, url_for, request, redirect
import data_handler

app = Flask(__name__)


@app.route("/list", methods=['GET'])
def list_page():
    return render_template('list.html')

@app.route("/", methods=['GET'])
def main_page():
    return render_template('main.html')

@app.route('/question/<id>')
def question(id):
    question_list = data_handler.get_all_questions()
    for i in question_list:
        if id in i:
            return render_template('question.html', user_question=i)


@app.route('/add-question')
def add_question():
    return render_template('add-question.html')


@app.route('/add-question', methods=['POST'])
def get_data():
    unique_id = data_handler.get_unique_id()
    title = request.form['title']
    user_question = request.form['question']

    data_handler.save_data(unique_id, title, user_question)
    return redirect(url_for('question', id=unique_id))

@app.route('/question-added', methods=['POST'])
def get_data_2():
    unique_id = data_handler.get_unique_id()
    anwser = request.form['anwser']

    data_handler.save_data(unique_id,anwser)
    return redirect(url_for('anwser', id=unique_id))


if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
