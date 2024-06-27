from market import app, db
from market.models import User, Item


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        item1 = Item(name='Iphone 15', barcode=54321,
                     price=2250, description='latest Iphone')
        item2 = Item(name='Hp 840', barcode=98765,
                     price=800, description='best Hp laptop')
        item3 = Item(name='HDD', barcode=12345,
                     price=220, description='best HDD')

        db.session.add_all([item1, item2, item3])
        db.session.commit()
    app.run(debug=True)
