from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_200_OK,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED, HTTP_400_BAD_REQUEST 
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.customers import Customer
from app.extensions import db

#customers blueprint
customers= Blueprint('categories', __name__,url_prefix='/api/v1/customers')

#creating a customer
@customers.route('/create', methods = ['POST'])


def createCustomer():

     #storing request values
    data = request.json
    name = data.get('name')
    biography= data.get('biography')
    email = data.email('email')
    password = data.password('password')
    address = data.address('address')
    

     #validations of the incoming request
    if not name or not biography or not email or not password  or not address:
        return jsonify({'error':'All fields are required'}),HTTP_400_BAD_REQUEST
    
    try:

       #creating a new customer
        new_customer = Customer(name=name,biography=biography,address=address,password=password)
        db.session.add(new_customer)
        db.session.commit()

        return jsonify({
            'message': name + ' has been created successfully as a',
            'product':{
                'id':new_customer.id,
                'name':new_customer.name,
                'email':new_customer.email,
                'biography':new_customer.biography,
                'address':new_customer.address,
                'password':new_customer.password,


            }
            }),HTTP_201_CREATED 

    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    
    


    

