from market import app, db
from market.models import User, Item


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        item1 = Item(name="Quantum Watch", barcode=483762, price=3450,
                     description="A sleek and modern watch that uses quantum technology for ultra-precise timekeeping.")
        item2 = Item(name="Echo Headphones", barcode=519284, price=1050,
                     description="High-fidelity wireless headphones with noise-cancellation and superior sound quality.")
        item3 = Item(name="Solar Backpack", barcode=273981, price=890,
                     description="A durable backpack with integrated solar panels to charge your devices on the go.")
        item4 = Item(name="Aero Drone", barcode=692347, price=390,
                     description="A lightweight, high-performance drone with 4K video capabilities and advanced flight controls.")
        item5 = Item(name="Crystal Lamp", barcode=158203, price=450,
                     description="A beautiful crystal lamp that creates a mesmerizing light display, perfect for any room.")
        item6 = Item(name="BioBlend Protein", barcode=834672, price=290,
                     description="A plant-based protein powder blend that provides essential nutrients for muscle recovery and growth.")
        item7 = Item(name="Velocity Bike", barcode=739451, price=120,
                     description="A high-performance road bike designed for speed and efficiency, perfect for competitive cyclists.")
        item8 = Item(name="Serenity Tea Set", barcode=562109, price=745,
                     description="A handcrafted tea set that includes a teapot, cups, and a variety of calming teas.")
        item9 = Item(name="Fusion Blender", barcode=210587, price=200,
                     description="A powerful blender with multiple settings for making smoothies, soups, and more.")
        item10 = Item(name="Horizon Treadmill", barcode=945731, price=250,
                      description="A top-of-the-line treadmill with interactive workout programs and a high-definition display.")

        db.session.add_all([item1, item2, item3, item4, item5,
                           item6, item7, item8, item9, item10])
        db.session.commit()
    app.run(debug=True)
