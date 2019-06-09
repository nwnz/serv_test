from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LinkForm


@app.route('/index',methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        flash('Сокращенная ссылка - {}'.format('СЮДА НАДО ВВЕСТИ СОКРАЗЕННУЮ ССЫЛКУ')) #Сюда сорасщенная ссылка
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', form=form)



