from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect(app):
    db.app = app
    db.init_app(app)


class Users(db.Model):
    """
        users model
    """

    __tablename__ = "users"
    userID = db.Column(db.Integer, unique = True, primary_key = True, autoincrement = True)
    fullname = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.Text, nullable = False)

    @classmethod
    def signup(cls, name, email, password):
        """
            encrypt password and add user to db
        """
        ## encrypt password
        hashed_password = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = Users(fullname = name, email = email, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def login(cls,email, password):
        """
         authenticate user
        """
        try:
            user = cls.query.filter(cls.email==email).first()
            if user:
                auth = bcrypt.check_password_hash(user.password, password)
                if auth:
                    print(user)
                    return user
            return False
        except:
            print("user not found")
        


     






class Sellers(db.Model):
    """
        sellers model
    """

    __tablename__ = "sellers"

    sellerID = db.Column(db.Integer, autoincrement = True, primary_key= True)
    businessName = db.Column(db.Text, nullable = True, unique = True)
    address = db.Column(db.Text, nullable = False)
    city = db.Column(db.Text, nullable = False)
    state = db.Column(db.Text, nullable = False)
    nif = db.Column(db.Text, nullable = False)
 

class Categories(db.Model):
    """
        categories model
    """
    __tablename__= "categories"
    categoryId = db.Column(db.Integer, autoincrement =True, primary_key = True)
    categoryName = db.Column(db.Text, unique = True, nullable = False)
   
class Products(db.Model):
    """
        products model
    """
    __tablename__ = "products"
    productId = db.Column(db.Integer, autoincrement = True, primary_key = True) 
    productTitle= db.Column( db.Text, nullable = False)
    productName = db.Column( db.Text, nullable = False)
    color = db.Column( db.Text, nullable = False)
    price = db.Column( db.Float, nullable = False)
    size = db.Column( db.Text, nullable = False)
    weight= db.Column( db.Float, nullable = False)
    otherDetails = db.Column( db.Text, nullable = False)
    promotionID = db.Column( db.Integer, db.ForeignKey('promotions.promoId'), nullable = False)
    ownerID = db.Column( db.Integer,  db.ForeignKey('sellers.sellerID'), nullable = False)
    categoryID = db.Column( db.Integer,db.ForeignKey('categories.categoryId'), nullable = False)
    

class Promotions(db.Model):
    """
        promotions model
    """

    __tablename__ = "promotions"
    promoId = db.Column(db.Integer, primary_key = True, autoincrement = True)
    promoCode = db.Column(db.Text, nullable= False, unique = True)
    ownerId = db.Column(db.Integer,db.ForeignKey('sellers.sellerID'), nullable = False,)
    promoValue = db.Column(db.Integer, nullable = False)
   

class Reviews(db.Model):
    """
        reviews model
    """
    __tablename__ = "reviews"
    reviewId = db.Column(db.Integer, primary_key = True, autoincrement = True)
    reviewTitle = db.Column(db.Text, nullable = False)
    reviewDetail = db.Column(db.Text, nullable = False)
    reviewerID = db.Column(db.Integer,  db.ForeignKey('users.userID'), nullable = False,)
    productID = db.Column(db.Integer, db.ForeignKey('products.productId'), nullable = False,)
    createdDate = db.Column(db.DateTime, nullable = False)
    updatedDate = db.Column(db.DateTime, nullable = False)
   

class Orders(db.Model):

    __tablename__ = "orders"
    orderId = db.Column(db.Integer, autoincrement = True, primary_key = True) 
    createdDate = db.Column(db.DateTime, nullable = False) 
    updatedDate = db.Column(db.DateTime, nullable = False) 
    userID = db.Column(db.Integer, db.ForeignKey('users.userID'), nullable = False) 
    userAddr = db.Column(db.Text, nullable = False) 
    userCity = db.Column(db.Text, nullable = False) 
    userState = db.Column(db.Text, nullable = False) 
    userZipCode = db.Column(db.Text, nullable = False) 
    userPhone = db.Column(db.Text, nullable = False) 
    userEmail = db.Column(db.Text, nullable = False)
    totalPrice = db.Column(db.Float, nullable = False)
    promoId = db.Column(db.Integer,  db.ForeignKey('promotions.promoId'), nullable = False) 

      
   

class OrderLines(db.Model):
    __tablename__ = "orderlines"
    lineId = db.Column(db.Integer, primary_key =True) 
    orderId = db.Column(db.Integer, db.ForeignKey("orders.orderId")) 
    productID = db.Column(db.Integer, db.ForeignKey('products.productId'), primary_key = True, nullable = False) 
    productName = db.Column(db.Text, nullable = False) 
    quantity = db.Column(db.Integer, nullable = False) 
    price = db.Column(db.Float, nullable = False) 
