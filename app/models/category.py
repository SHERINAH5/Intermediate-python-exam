from app.extensions import migrate, db
from  datetime import datetime

#creating the product model
class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text(100), nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self, name, description):
        super(Category, self).__init__()
        self.name = name
        self.description = description

    def __repr__(self):
        return f'{self.name}'
    
        


    
