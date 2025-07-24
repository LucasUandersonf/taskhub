from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Task, db
from app.forms.task_forms import TaskForm
from app.tasks import tasks_bp

@tasks_bp.route('/')
@login_required
def task_list():
    tasks = Task.query.filter_by(user_id = current_user.id).order_by(Task.timestamp.desc()).all()
    return render_template('tasks/list.html', tasks = tasks)

@tasks_bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        task =Task(
            title = form.title.data,
            description = form.description.data,
            done = form.done.data,
            owner = current_user
        )
        db.session.add(task)
        db.session.commit()
        flash('tarefa criada com sucesso!', 'success')
        return redirect(url_for('tasks.task_list'))
    return render_template('tasks/create.html', form = form)



@tasks_bp.route('/<int:task_id>/edit', methods = ['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        flash('Você não tem permissão para editar esta tarefa.', 'danger')
        return redirect(url_for('tasks.task_list'))
    
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data        
        task.done = form.done.data
        db.session.commit()
        flash('Tarefa atualizada com sucesso!','success')
        return redirect(url_for('tasks.task_list'))
    return  render_template('tasks/edit.html', form= form, task=task)


@tasks_bp.route('/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        flash('Você não pode excluir esta tarefa.', 'danger')
        return redirect(url_for('tasks.task_list'))
    db.session.delete(task)
    db.session.commit()
    flash('Tarefa excluida com sucesso!','info')
    return redirect(url_for('tasks.task_list'))




