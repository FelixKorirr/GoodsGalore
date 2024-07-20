from market import app, item_data

if __name__ == "__main__":
    item_data.add_items()
    app.run(debug=True)
