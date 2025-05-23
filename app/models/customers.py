from app.extensions import migrate,db
from  datetime import datetime

#creating the customer model
class Customer(db.Model):
    __tablename__='customers'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    biography = db.Column(db.Text(), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime,default=datetime.now())
    updated_at = db.Column(db.DateTime,onupdate=datetime.now())


    def __init__(self, name, email, biography, address, password ):
        super(Customer, self).__init__()
        self.name = name
        self.email = email
        self.address = address
        self.biography = biography
        self.password = password

    def get_name(self):
        return f'{self.name}'
    
        
    


    
    

    