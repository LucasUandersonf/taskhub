from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
    
class TaskForm(FlaskForm):
    title = StringField('Título', validators= [DataRequired(), Length(min = 1, max=140)])
    description = TextAreaField('Descrição')
    completed = BooleanField('Concluida')
    submit = SubmitField('Salvar')