from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField, SelectField, IntegerField, FloatField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class SingleBulkForm(Form):
    answer = RadioField('Choose your input method:',
                        choices=[('bulk', 'Bulk'), ('single', 'Single')])
    submit = SubmitField('Go')


class SingleForm(Form):
    refile = SelectField('Is the application being refiled?',
                         choices=[(1, 'Yes'), (0, 'No')])
    employer_num_employees = IntegerField('How many employees does the company\
                                          have?')
    foreign_worker_ownership_interest = SelectField('Does the foreign worker\
                                                    have an ownership interest\
                                                    in the company?',
                                                    choices=[(1, 'Yes'),
                                                             (0, 'No')])
    pw_amount_9089 = FloatField('What is the prevailing wage for this job?')
    wage_offer_from = FloatField('Low offer:')
    wage_offer_to = FloatField('High offer:')
    job_info_training = SelectField('Is training required for the job?',
                                    choices=[(1, 'Yes'), (0, 'No')])
    job_info_training_num_months = IntegerField('How many months of training?')
    job_info_experience = SelectField('Is experience required for the job?',
                                      choices=[(1, 'Yes'), (0, 'No')])
    job_info_experience_num_months = IntegerField('How many months of\
                                                  experience?')
    job_info_alt_field = SelectField('Is an alternative field of study\
                                     acceptable for the eduction requirement?',
                                     choices=[(1, 'Yes'), (0, 'No')])
    job_info_foreign_ed = SelectField('Is a foreign equivalent of the required\
                                      education acceptable?',
                                      choices=[(1, 'Yes'), (0, 'No')])
    job_info_alt_occ = SelectField('Is experience in an alternate occupation\
                                   acceptable?',
                                   choices=[(1, 'Yes'), (0, 'No')])
    job_info_alt_occ_num_months = IntegerField('How many months of experience\
                                               in the alternate occupation?')
    job_info_job_req_normal = SelectField('Are the job opportunity\'s \
                                          requirements normal for occupation?',
                                          choices=[(1, 'Yes'), (0, 'No')])
    job_info_foreign_lang_req = SelectField('Is there a foreign language\
                                            requirement?',
                                            choices=[(1, 'Yes'), (0, 'No')])
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
    form = SingleForm()
    if form.validate_on_submit():
        return redirect(url_for('single_report'))
    return render_template('single.html', form=form)


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
