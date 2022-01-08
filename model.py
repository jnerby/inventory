from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri="postgresql:///inventory", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = False
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


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
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Entry product={self.product_name} qty={self.qty}>" 


if __name__ == "__main__":
    from server import app
    connect_to_db(app)