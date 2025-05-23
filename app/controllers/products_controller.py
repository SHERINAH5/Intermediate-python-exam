from flask import Blueprint,request,jsonify
from app.status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, HTTP_404_NOT_FOUND 
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.products import Product
from app.extensions import db

# products blueprint
products= Blueprint('products', __name__,url_prefix='/api/v1/products')

#creating a product
@products.route('/create', methods = ['POST'])

def createProduct():
    
     #storing request values
    data = request.json
    name = data.get('name')
    price = data.get('price')
    description = data.get('description')
    category_id = get_jwt_identity()

     #validations of the incoming request
    if not name or not description or not price or not category_id:
        return jsonify({'error':'All fields are required'}),HTTP_400_BAD_REQUEST
    
    try:

       #creating a new product
        new_product = Product(name=name,description=description,price=price,category_id=category_id)
        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            'message': name + ' has been created successfully as a',
            'product':{
                'id':new_product.id,
                'name':new_product.name,
                'price':new_product.price,
                'description':new_product.description,

            }
            }),HTTP_201_CREATED 

    except Exception as e:
        db.session.rollback()
        return jsonify({'error':str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
    

    
     #Deleting a product
@products.route('/delete/<int:id>',methods=['DELETE'])

def deleteCompany(id):

    try:
        current_user = get_jwt_identity()
        
         #get product by id
        product= Product.query.filter_by(id=id).first()

        if not product:
            return jsonify({"error":"Product not found"}),HTTP_404_NOT_FOUND
        
        
        else:

            db.session.delete(product)
            db.session.commit()


            return jsonify({'message':'Product has been deleted successfully'})
            

    except Exception as e:
        return jsonify({
            'error':str(e)
        }),HTTP_500_INTERNAL_SERVER_ERROR
    
    
    
    
    

    
    


    
