from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class SingleBulkForm(Form):
    answer = RadioField('Choose your input method:',
                        choices=[('bulk', 'Bulk'), ('single', 'Single')])
    submit = SubmitField('Go')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SingleBulkForm()
    if form.validate_on_submit():
        if form.answer.data == 'bulk':
            return redirect(url_for('bulk'))
        else:
            return redirect(url_for('single'))
    return render_template('index.html', form=form)


@app.route('/single')
def single():
    return render_template('single.html')


@app.route('/single_report')
def single_report():
    return render_template('single_report.html')


@app.route('/bulk')
def bulk():
    return render_template('bulk.html')


@app.route('/bulk_report')
def bulk_report():
    return render_template('bulk_report.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
