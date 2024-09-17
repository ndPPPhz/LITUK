from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

def get_random_question():
    conn = sqlite3.connect('lituk.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT question, opt1, opt2, opt3, opt4, answer FROM questions ORDER BY RANDOM() LIMIT 1;")
    question_data = cursor.fetchone()
    conn.close()
    return question_data

@app.route('/')
def index():
    question_data = get_random_question()
    question = question_data[0]
    options = question_data[1:5]
    correct_answer_index = int(question_data[5]) - 1
    return render_template('index.html', question=question, options=options, correct_answer_index=correct_answer_index)

@app.route('/answer', methods=['POST'])
def answer():
    question_data = get_random_question()
    correct_answer_index = int(question_data[5]) - 1
    question = question_data[0]
    options = question_data[1:5]
    return render_template('index.html', question=question, options=options, correct_answer_index=correct_answer_index)

if __name__ == '__main__':
    app.run(debug=True)
