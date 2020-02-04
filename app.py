from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)


global correct
global incorrect
global total
correct = 0
incorrect = 0
total = correct + incorrect

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    option1 = db.Column(db.Text, nullable=False)
    option2 = db.Column(db.Text, nullable=False)
    option3 = db.Column(db.Text, nullable=False)
    option4 = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'Question ' + str(self.id)


class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    correct = db.Column(db.Integer, nullable=True)
    incorrect = db.Column(db.Integer,  nullable=True)




    def __repr__(self):
        return 'Result ' + str(self.id)


@app.route('/', methods=['GET', 'POST'])
def frontpage():
    if request.method == 'POST':
        global question_option1
        question_text = request.form['question']
        question_option1 = request.form['option1']
        question_option2 = request.form['option2']
        question_option3 = request.form['option3']
        question_option4 = request.form['option4']
        new_question = Question(text=question_text, option1=question_option1, option2=question_option2, option3=question_option3, option4=question_option4)
        db.session.add(new_question)
        db.session.commit()
        return redirect('/')
    else:
        all_questions = Question.query.order_by().all()
        return render_template('frontpage.html', questions=all_questions)


@app.route('/answers', methods=['GET', 'POST'])
def answers():
    correct = Results.correct
    incorrect = Results.incorrect
    if request.method == 'POST':
        submitted_answer = request.form['answer']
        if submitted_answer == Question.option1:
            correct = int(0)
            incorrect = int(0)
            correct += int(1)
            new_result = Results(correct=correct, incorrect=incorrect)
            db.session.add(new_result)
            db.session.commit()
        else:
            correct = int(0)
            incorrect = 0
            incorrect += int(1)
            new_result = Results(correct=correct, incorrect=incorrect)
            db.session.add(new_result)
            db.session.commit()
        return redirect('/answers')
    all_questions = Question.query.order_by().all()
    all_results = Results.query.order_by().all()
    return render_template('answers.html', questions=all_questions, all_results=all_results)


@app.route('/results', methods=['GET', 'POST'])
def restults():
        return render_template('results.html', correct=correct, incorrect=incorrect, total=total)


@app.route('/delete/<int:id>')
def delete(id):
    question_to_delete = Question.query.get_or_404(id)
    try:
        db.session.delete(question_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "error"


if __name__ == "__main__":
    app.run(debug=True)
