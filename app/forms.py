from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Weekly_Reflection

class LoginForm(FlaskForm):
    username = StringField('Are you Chloe or Sean?', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Let us go')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')

    def valdiate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class PostForm(FlaskForm):
    post = TextAreaField('Say your words', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

class WeeklyReflectionForm(FlaskForm):
    q1 = StringField('🌱 What did I learn last week?', validators=[DataRequired()], render_kw={"placeholder": "Write here"})
    q2 = StringField('🍑 What was my greatest accomplishment over the past week?', render_kw={"placeholder": "Write here"})
    q3 = StringField('😊 Which moment from last week was the most memorable and why?', render_kw={"placeholder": "Write here"})
    q4 = StringField('💪 What’s the #1 thing I need to accomplish this week?', render_kw={"placeholder": "Write here"})
    q5 = StringField('😼 What can I do right now to make the week less stressful?', render_kw={"placeholder": "Write here"})
    q6 = StringField('🙈 What have I been avoiding that needs to get done?', render_kw={"placeholder": "Write here"})
    q7 = StringField('🦋 Is there anyone I’ve been meaning to talk to?', render_kw={"placeholder": "Write here"})
    q8 = StringField('😌 How can I help someone else this coming week?', render_kw={"placeholder": "Write here"})
    q9 = StringField('🤗 What are my top 3 goals for the next 3 years?', render_kw={"placeholder": "Write here"})
    q10 = StringField('🕺 Have any of my recent actions moved me closer to my goals?', render_kw={"placeholder": "Write here"})
    q11 = StringField('🌈 What am I looking forward to during the upcoming week?', render_kw={"placeholder": "Write here"})
    q12 = StringField('✨ What am I most grateful for?', render_kw={"placeholder": "Write here"})
    q13 = StringField('🕺 Have any of my recent actions moved me closer to my goals?', render_kw={"placeholder": "Write here"})
    q14 = StringField('😊 How can I help someone else this coming week?', render_kw={"placeholder": "Write here"})
    submit = SubmitField('Submit')