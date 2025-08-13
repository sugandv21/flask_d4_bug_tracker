from flask import Flask, render_template, flash, redirect, url_for
from forms import BugReportForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def home():
    return render_template('layout/home.html')

@app.route('/bug-report', methods=['GET', 'POST'])
def bug_report():
    form = BugReportForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        description = form.description.data
        severity = form.severity.data

        if severity == "High":
            flash(" High severity bug reported! Our team will address it ASAP.", "danger")
        elif severity == "Medium":
            flash(" Medium severity bug submitted. We'll check it soon.", "warning")
        else:
            flash(" Low severity bug noted. Thank you!", "success")

        return redirect(url_for('home'))

    return render_template('layout/bug_report.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
