from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField,FileField,TextAreaField,IntegerField
from wtforms.validators import DataRequired, EqualTo,ValidationError
from models import User
class LoginForm(FlaskForm):
    username =StringField(
        label=u"username",
        validators=[
            DataRequired(u"username can not be null")
        ],
        description=u"username",
        render_kw={
            "class":"form-control",
            "placeholder":"please input username!"
        }
    )
    password=PasswordField(
        label=u"password",
        validators=[
            DataRequired(u"password can not be null")
        ],
        description=u"password",
        render_kw={
            "class":"form-control",
            "placeholder":"please input password!"
        }
    )
    submit=SubmitField(
        u"login",
        render_kw={
            "class":"btn btn-primary"
        }
    )

    def validate_password(self,field):
        password=field.data
        user=User.query.filter_by(username=self.username.data).first()
        if not user.check_password(password):
            raise ValidationError(u"Worry password")


class RegisterForm(FlaskForm):
        username = StringField(
            label=u"username",
            validators=[
                DataRequired(u"username can not be null")
            ],
            description=u"username",
            render_kw={
                "class": "form-control",
                "placeholder": "please input username!"
            }
        )
        password = PasswordField(
            label=u"password",
            validators=[
                DataRequired(u"password can not be null")
            ],
            description=u"password",
            render_kw={
                "class": "form-control",
                "placeholder": "please input password!"
            }
        )
        repassword = PasswordField(
            label=u"repassword",
            validators=[
                DataRequired(u"password can not be null"),
                EqualTo('password', message=u"different form password")
            ],
            description=u"password",
            render_kw={
                "class": "form-control",
                "placeholder": "please confirm your password!"
            }
        )
        submit = SubmitField(
            u"register",
            render_kw={
                "class": "btn btn-success"
            }
        )
        #validate only one userame
        def validate_username(self,field):
            username=field.data
            user=User.query.filter_by(username=username).count()
            if user>0:
                raise ValidationError(u"username has been used by other people")

class ArticleForm(FlaskForm):
    title=StringField(
        label=u"title",
        description=u"title",
        validators=[
            DataRequired(u"Title can not be null!")
        ],
        render_kw={
            "class":"form-control",
            "placeholder":u"please input a title!"
        }
    )
    category=SelectField(
        label=u"category",
        description=u"category",
        validators=[
            DataRequired(u"Category can not be null!")
        ],
        choices=[(1,u"moves"),(2,u"comedy"),(3,u"others")],
        default=3,
        coerce=int,
        render_kw={
            "class":"form-control"
        }
    )
    logo=FileField(
        label=u"picture",
        validators=[
            DataRequired(u"picture can not be null!")
        ],
        description=u"picture",
        render_kw={
            "class":"form-control-file"
        }
    )
    content=TextAreaField(
        label=u"content",
        validators=[
            DataRequired(u"Content can not be null!")
        ],
        description=u"content",
        render_kw={
            "class":"form-control",
            "style":"height:300px;",
            "id":"content"
        }
    )
    submit=SubmitField(
        u"submit this review",
        render_kw={
            "class":"btn btn-primary"
        }
    )

class ArticleEditForm(FlaskForm):
    id=IntegerField(
        label=u"id",
        validators=[DataRequired(u"id can not be null")]
    )
    title=StringField(
        label=u"title",
        description=u"title",
        validators=[
            DataRequired(u"Title can not be null!")
        ],
        render_kw={
            "class":"form-control",
            "placeholder":u"please input a title!"
        }
    )
    category=SelectField(
        label=u"category",
        description=u"category",
        validators=[
            DataRequired(u"Category can not be null!")
        ],
        choices=[(1,u"moves"),(2,u"comedy"),(3,u"others")],
        default=3,
        coerce=int,
        render_kw={
            "class":"form-control"
        }
    )
    logo=FileField(
        label=u"picture",
        validators=[
            DataRequired(u"picture can not be null!")
        ],
        description=u"picture",
        render_kw={
            "class":"form-control-file"
        }
    )
    content=TextAreaField(
        label=u"content",
        validators=[
            DataRequired(u"Content can not be null!")
        ],
        description=u"content",
        render_kw={
            "class":"form-control",
            "style":"height:300px;",
            "id":"content"
        }
    )
    submit=SubmitField(
        u"submit this review",
        render_kw={
            "class":"btn btn-primary"
        }
    )