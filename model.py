from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///inventory", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

# class Product(db.Model):
#     """A product to be stored in inventory"""

#     __tablename__ = "products"

#     product_id = db.Column(db.Integer,
#                         primary_key=True,
#                         autoincrement=True)
#     product_name = db.Column(db.String(25))

#     entry = db.relationship("Entry", back_populates="product")

#     def __repr__(self):
#         return f"<Product name={self.product_name}>"

class Entry(db.Model):
    """An entry in inventory"""

    __tablename__ = "entries"

    entry_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    product_name = db.Column(db.String(50),
                            nullable=False)
    qty = db.Column(db.Integer,
                    nullable=False)
    # product_id = db.Column(db.Integer,
    #                 db.ForeignKey("products.product_id"),
    #                 nullable=False)
    timestamp = db.Column(db.DateTime)

    # product = db.relationship("Product", back_populates="entry")
    update = db.relationship("Update", back_populates="entry")

    def __repr__(self):
        return f"<Entry product={self.product_id} qty={self.qty}>"    

class Update(db.Model):
    """An update to an inventory entry"""

    __tablename__ = "updates"

    update_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    entry_id = db.Column(db.Integer,
                    db.ForeignKey("entries.entry_id"),
                    nullable=False)
    updated_qty = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    created_by = db.Column(db.Integer,
                    db.ForeignKey("users.user_id"),
                    nullable=False)


    entry = db.relationship("Entry", back_populates="update")

    def __repr__(self):
        return f"<Update update_id={self.update_id} qty={self.updated_qty}>" 

class User(db.Model):
    """A user"""
    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    username = db.Column(db.String(20))

    def __repr__(self):
        return f"<User user_id={self.user_id} username={self.username}>" 


if __name__ == "__main__":
    from server import app
    connect_to_db(app)