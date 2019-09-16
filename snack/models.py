from snack import db,app
from flask_login import LoginManager,UserMixin

login_manager=LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),nullable=False)
    password=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return '{}'.format(self.name)