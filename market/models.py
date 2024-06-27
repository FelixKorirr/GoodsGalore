from market import db, bcrypt


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    barcode = db.Column(db.String(20), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(
        1024), nullable=False)
    owner_id = db.Column(
        db.Integer(), db.ForeignKey('users.id'))


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password_hash = db.Column(db.Integer(), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owner', lazy=True)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_password).decode('utf-8')
