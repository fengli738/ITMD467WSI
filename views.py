#coding:utf8
import datetime
import uuid
import os
from flask import Flask, render_template, url_for, flash, session, request
from werkzeug.utils import secure_filename
from werkzeug.utils import redirect
from forms import LoginForm ,RegisterForm,ArticleForm,ArticleEditForm
from models import User, db,Article
from werkzeug.security import generate_password_hash
app=Flask(__name__)
app.config["SECRET_KEY"]="12345678"
app.config["UP"]=os.path.join(os.path.dirname(__file__),"static/uploads")

#login
@app.route("/",methods=["GET","POST"] )
def login():
  try:
    loginform =LoginForm()
    if loginform.validate_on_submit():
        data=loginform.data
        session["user"]=data["username"]
        flash("Login successfully","ok")
        return redirect("/art/list/1/")
    return render_template("login.html",form=loginform)
  except Exception as e:
      print(e)
#register
@app.route("/register/",methods=["GET","POST"] )
def register():
  try:
    registerform=RegisterForm()
    if registerform.validate_on_submit():
        data=registerform.data
        #save user information
        user =User(
            username=data["username"],
            password=generate_password_hash(data["password"]),
            addtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        db.session.add(user)
        db.session.commit()
        flash(u"Register successfully","ok")
        return redirect("/login/")
    else:
        flash(u"input right information","err")

    return render_template("register.html",form=registerform)
  except Exception as e:
      print(e)
#exit
@app.route("/logout/",methods=["GET"])
def logout():
    return redirect("/")
#update file name
def change_filename(name):
    information=os.path.splitext(name)
    #filename:time+string+others
    name=datetime.datetime.now().strftime('%Y%m%d%H%M%S')+str(uuid.uuid4().hex)+information[-1]
    return name;

#add art
@app.route("/art/add/",methods=["GET","POST"])
def art_add():
    articleform=ArticleForm()
    if articleform.validate_on_submit():
        data=articleform.data
        #update picture
        datas=secure_filename(articleform.logo.data.filename)
        logo=change_filename(datas)
        if not os.path.exists(app.config["UP"]):
            os.makedirs(app.config["UP"])
        #save file
        articleform.logo.data.save(app.config["UP"]+"/"+logo)
        #get userID
        user=User.query.filter_by(username=session["user"]).first()

        user_id=user.id
        #save data
        articale =Article(
            title=data["title"],
            category=data["category"],
            user_id=user_id,
            logo=logo,
            content=data["content"],
            addTime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.session.add(articale)
        db.session.commit()
        flash(u"Add review successfully!","ok")


    return render_template("artadd.html",form=articleform)
#edit art
@app.route("/art/edit/<int:id>/",methods=["GET","POST"])
def art_update(id):
    art=Article.query.get_or_404(int(id))
    form=ArticleEditForm()
    if request.method=="GET":
     form.content.data=art.content
     form.category.data=art.category
     form.logo.data=art.logo
    if form.validate_on_submit():
        data=form.data
        # update picture
        datas = secure_filename(form.logo.data.filename)
        logo = change_filename(datas)
        if not os.path.exists(app.config["UP"]):
            os.makedirs(app.config["UP"])
        # save file
        form.logo.data.save(app.config["UP"] + "/" + logo)
        art.logo=logo
        art.title=data["title"]
        art.category=data["category"]
        art.content=data["content"]
        db.session.add(art)
        db.session.commit()
        flash(u"edit article successfully")
    return render_template("artedit.html",form=form,art=art)
#delete art
@app.route("/art/del/<int:id>/",methods=["GET"])
def art_delete(id):
    article=Article.query.get_or_404(int(id))
    db.session.delete(article)
    db.session.commit()
    return redirect("art/list/1/")
#art list
@app.route("/art/list/<int:page>/",methods=["GET"])
def art_list(page=None):
    try:
     if page is None:
         page=1
     user=User.query.filter_by(username=session["user"]).first()
     page_data=Article.query.filter_by(
         #user_id=user.id
     ).order_by(
        Article.addTime.desc()
     ).paginate(page=page,per_page=10)
     category= [(1, u"moves"), (2, u"comedy"), (3, u"others")]
     return render_template("artlist.html",page_data=page_data,category=category)
    except Exception as e:
        print(e)

#art content
@app.route("/art/content/<int:id>/",methods=["GET","POST"])
def art_content(id):
    art=Article.query.get_or_404(int(id))
    return render_template("artcontent.html",data=art)
if __name__ == '__main__':
    app.run(debug=True,host="127.0.0.1",port=8080)




