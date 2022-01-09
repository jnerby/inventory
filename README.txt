INSTRUCTIONS
To view this project on your local machine, complete the following steps:
1) Install Homebrew
2) Install Git
3) Open a new terminal window and run “git clone https://github.com/jnerby/inventory.git”
4) cd into the “inventory” directory and open the downloaded folder “inventory” in VS Code or similar application.
5) Run “pip3 install -r requirements.txt” in your terminal window.
6) Run “pip3 install flask-sqlalchemy”
7) Run “python3 server.py” to run the server in your local browser.

COMMENTS

I chose to use a Flask server and SQLAlchemy to create this inventory tracking system. The current data model has one table, entries, which records
the product name, quantity, and timestamp for every entry in the inventory database. 

Given more time, I would add the following classes: User, Update, Product. The User class would track user login information, such as usernames and password hashes. The User class's primary key would be stored in the Flask session, and the entries table would contain a "created_by" attribute, which would be a foreign key for the User's user_id.

This program currently allows users to edit and delete records directly from the entries table. Given more time, I would add an updates table to track changes to entries without directly editing and deleting raw data. The updates table would have an entries_id attribute which is a foreign key from the entries table. The updates table would track comments about updates, the user_id of the user who updated the entry, and the timestamp of the update.

I would also add a Product class to standardize information about products available in inventory. The product table would contain a producti_d and product_name, and the entries table would contain a "product_id" attribute, which would be a foreign key for the Product's product_id.

My additional feature generates a report on inventory levels over time. Users can select a month and year to view the counts of products in stock. This feature generates a csv report which sorts product counts from most in-stock to least in-stock.

SEED DB
to seed data, run psql inventory < inventory.sql
Data from 1/21 and 2/21