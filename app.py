from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField, SelectField, IntegerField, FloatField, DateField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


class YesNoField(SelectField):
    def __init__(self, *args, **kwargs):
        super(YesNoField, self).__init__(*args, **kwargs)
        self.choices = [(1, 'Yes'), (0, 'No')]
        self.default = 0


class EducationField(SelectField):
    def __init__(self, *args, **kwargs):
        super(EducationField, self).__init__(*args, **kwargs)
        eds = ['Doctorate', 'Master\'s', 'Bachelor\'s', 'Associate\'s',
               'High School', 'None', 'Other']
        self.choices = [(name, name) for name in eds]


class SingleBulkForm(Form):
    answer = RadioField('Choose your input method:',
                        choices=[('bulk', 'Bulk'), ('single', 'Single')])
    submit = SubmitField('Go')


class SingleForm(Form):
    refile = YesNoField('Is the application being refiled?')
    employer_num_employees = IntegerField('How many employees does the company\
                                          have?')
    foreign_worker_ownership_interest = YesNoField('Does the foreign worker\
                                                    have an ownership interest\
                                                    in the company?')
    pw_amount_9089 = FloatField('What is the prevailing wage for this job?')
    wage_offer_from = FloatField('Low offer:')
    wage_offer_to = FloatField('High offer:')
    job_info_training = YesNoField('Is training required for the job?')
    job_info_training_num_months = IntegerField('How many months of training?')
    job_info_experience = YesNoField('Is experience required for the job?')
    job_info_experience_num_months = IntegerField('How many months of\
                                                  experience?')
    job_info_alt_field = YesNoField('Is an alternative field of study\
                                     acceptable for the eduction requirement?')
    job_info_foreign_ed = YesNoField('Is a foreign equivalent of the required\
                                      education acceptable?')
    job_info_alt_occ = YesNoField('Is experience in an alternate occupation\
                                   acceptable?')
    job_info_alt_occ_num_months = IntegerField('How many months of experience\
                                               in the alternate occupation?')
    job_info_job_req_normal = YesNoField('Are the job opportunity\'s \
                                          requirements normal for occupation?')
    job_info_foreign_lang_req = YesNoField('Is there a foreign language\
                                            requirement?')
    job_info_combo_occupation = YesNoField('Does the job include a combination\
                                            of occupations?')
    ji_foreign_worker_live_on_premises = YesNoField('Will the worker live on\
                                                     the premises?')
    ji_live_in_domestic_service = YesNoField('Will the worker be a live-in\
                                              domestic worker?')
    ji_live_in_dom_svc_contract = YesNoField('If so, has a contract been\
                                              executed, and a copy been sent\
                                              to the foreign worker?')
    recr_info_professional_occ = YesNoField('Is the application for a\
                                             professional occupation, other\
                                             than a university or college\
                                             professor?')
    recr_info_coll_univ_teacher = YesNoField('Is the application for a\
                                              college or university teacher?')
    recr_info_coll_teach_comp_proc = YesNoField('If this is for a university\
                                                 teaching position, was the\
                                                 candidate selected using a\
                                                 competitive recruitment and\
                                                 selection process?')
    ri_posted_notice_at_worksite = YesNoField('Was he notice of filing posted\
                                               for 10 business days in a\
                                               conspicuous location at the\
                                               place of employment, ending at\
                                               least 30 days before but not\
                                               more than 180 days before the\
                                               date the application was filed')
    ri_layoff_in_past_six_months = YesNoField('Did the employer have a layoff\
                                               in the intended area of \
                                               employment in the last six\
                                               months?')
    ri_us_workers_considered = YesNoField('If there was a layoff, were the\
                                           laid-off workers notified and\
                                           considered for this job\
                                           opportunity?')
    foreign_worker_info_training_comp = YesNoField('Has the foreign worker\
                                                    completed the required\
                                                    training for the job?')
    foreign_worker_info_req_experience = YesNoField('Does the foreign worker\
                                                     have the required\
                                                     experience?')
    foreign_worker_info_alt_edu_experience = YesNoField('Does the foreign\
                                                         worker possesses the\
                                                         alternate combination\
                                                         of education and\
                                                         experience?')
    foreign_worker_info_rel_occup_exp = YesNoField('Does the foreign worker\
                                                    have the required\
                                                    alternate experience?')
    preparer_info_emp_completed = YesNoField('Was the application completed\
                                              by the employer?')
    month = SelectField('What month was the application filed?',
                        choices=[(1, 'Jan'), (2, 'Feb'), (3, 'Mar'),
                                 (4, 'Apr'), (5, 'May'), (6, 'Jun'),
                                 (7, 'Jul'), (8, 'Aug'), (9, 'Sep'),
                                 (10, 'Oct'), (11, 'Nov'), (12, 'Dec')])
    JOB_INFO_EDUCATION = EducationField('What is the highest level of education\
                                        acheived by the foreign worker?')


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
