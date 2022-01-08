install Homebrew
install git
from terminal window, run git clone
cd into directory

given more time, would add a User class to the model and created_by fields to Entries and Updates tables. Use flask sessions to store the user_id of the logged in user to track who enters, edits, deletes inventory items.
Would also add a table for product to the model, to standardize the names of inventory items. This table would have a one:many relationship with the entries table, with entries containing a product_id field which is a foreign key to the products table.
With more time, would not allow users to overwrite entries in the entries table. Log updates and changes in separate table

Considerations about how edits and updates should work.
Ideally want one table just for initial entries, 


additional feature = allow comments for deletion