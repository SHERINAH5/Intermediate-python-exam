from app.extensions import migrate, db
from  datetime import datetime

#creating the product model
class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text(), nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    category = db.relationship('Category',backref='products')
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())

    def __init__(self, name, description, category_id):
        super(Product, self).__init__()
        self.name = name
        self.description = description
        self.category_id = category_id

    def __repr__(self):
        return f'{self.name} {self.description}'
    
        




    

