import datetime
from app import db, models

#db.create_all()
def print_all():
    users = models.User.query.all()
    for u in users:
        print(u.id, u.nickname, u.email)


# database delete
def db_delete():
    users = models.User.query.all()
    for u in users:
        db.session.delete(u)
    posts = models.Post.query.all()
    for p in posts:
        db.session.delete(p)
    db.session.commit()

print_all()
u = models.User.query.get(1)
p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()
print_all()
