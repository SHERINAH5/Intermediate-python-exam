from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED 
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.category import Category
from app.extensions import db

#categories blueprint
categories= Blueprint('categories', __name__,url_prefix='/api/v1/categories')

#creating a category
@categories.route('/create', methods = ['POST'])

def createCategory():
     #storing request values
    data = request.json
    name = data.get('name')
    description = data.get('description')

     #validations of the incoming request
    if not name or not description:
        return jsonify({'error':'All fields are required'}),HTTP_400_BAD_REQUEST
    
    try:

       #creating a new category
        new_category = Category(name=name,description=description)
        db.session.add(new_category)
        db.session.commit()

        return jsonify({
            'message': name + ' has been created successfully as a',
            'product':{
                'id':new_category.id,
                'name':new_category.name,
                'description':new_category.description,

            }
            }),HTTP_201_CREATED 

    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    
    


    



    
