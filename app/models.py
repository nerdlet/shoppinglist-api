#third party pluggins
from datetime import datetime

#local imports
from app import db


class ShoppingList(db.Model):
    """Shopping list table here"""

    __tablename__ = 'shoppinglists'#should be plural always

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    creator = db.Column(db.String(64), db.ForeignKey(''))
    items = db.relationship('Item', backref='shoppinglists', lazy='dynamic')


    def __init__(self, name=None, creator=None, date_created=None):
        self.name = title or 'untitled'
        self.creator = creator
        self.date_created = date_created or datetime.utcnow()

    #instance created when queried
    def __repr__(self):
        return "<ShoppingList: {}>".format(self.name)


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return ShoppingList.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



class Item(db.Model):
    """Items table here"""

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(128))
    price = db.Column(db.Integer)
    creator = db.Column(db.String(64), db.ForeignKey(''))
    shoppinglist_id = db.Column(db.Integer, db.ForeignKey('shoppinglist_id'))

    def __init__(self, description, todolist_id, creator=None,
                 created_at=None):
        self.item_name = item_name
        self.shoppinglist_id = shoppinglist_id
        self.creator = creator

    def __repr__(self):
        return '<Item: {}>'.format(self.item_name)


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Item.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
