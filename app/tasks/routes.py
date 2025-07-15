from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.tasks import tasks_bp  # Importa o blueprint criado
from app.models import Task, db
from app.forms import TaskForm

@tasks_bp.route('/')  # Aqui não precisa colocar /tasks porque já está no url_prefix do blueprint
@login_required
def task_list():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.timestamp.desc()).all()
    return render_template('tasks/list.html', tasks=tasks)

@tasks_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            done=form.done.data,
            owner=current_user
        )
        db.session.add(task)
        db.session.commit()
        flash('Tarefa criada com sucesso!', 'success')
        return redirect(url_for('tasks.task_list'))
    return render_template('tasks/create.html', form=form)