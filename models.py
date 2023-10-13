# models.py

from config import db

class Passengers(db.Model):
     __tablename__ = "passengers"
     PassengerId = db.Column(db.Integer, primary_key=True)
     Survived = db.Column(db.Boolean, nullable=False)
     Pclass = db.Column(db.Integer, nullable=False)
     Name = db.Column(db.String(32), nullable=False)
     Sex = db.Column(db.String(32), nullable=False)
     Age = db.Column(db.Integer, nullable=False)
     SibSp = db.Column(db.Integer)
     Parch = db.Column(db.Integer)
     Ticket = db.Column(db.String(32))
     Fare = db.Column(db.Float)
     Cabin = db.Column(db.String(32))
     Embarked = db.Column(db.String(4))

     def __repr__(self):
        return f'<Passenger {self.PassengerId} {self.Name}>'
