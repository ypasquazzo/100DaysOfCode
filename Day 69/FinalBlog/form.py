from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class CreatePostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()], render_kw={'class': 'form-control'})
    subtitle = StringField(label="Subtitle", validators=[DataRequired()], render_kw={'class': 'form-control'})
    # author = StringField(label="Your Name", validators=[DataRequired()], render_kw={'class': 'form-control'})
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(), URL()],
                          render_kw={'class': 'form-control'})
    body = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    name = StringField(label="Name", validators=[DataRequired()])
    submit = SubmitField(label="SIGN ME UP!")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired()])
    password = StringField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="LOG IN")


class CommentForm(FlaskForm):
    body = CKEditorField(label="Comment", validators=[DataRequired()])
    submit = SubmitField(label="Submit Comment")
