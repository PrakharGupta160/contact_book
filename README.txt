THIS DIGITAL CONTACT BOOK HELP US TO STORE CONTACT DETAILS ON SOMEONE ON YOUR DESKTOP ! (ONLY A PROJECT)

contact book contains these commands:

    > create   - this command will help us to create new contact.
    > search   - this command will help us to search any contact using particular detail.
    > show all - this command will let us see all the available contacts .
    > update   - this command will update an existing contact.
    > delete   - this command will help us to delete existing contact.

this contact book also contains constraints like:

    > group    - this constraint will allow us to add a contact in certain group.
    > division - this constraint will allow us to divide phone numbers in certain category.
        -> home    : for saving details which are related to particular's home.
        -> office  : for saving details which are related to particular's office.
        -> custom  : fpt saving details which are related to "custom" of particular.

data type of the files saved will be list. And each and every column will have their own data type which
are listed below :

    > name      - this column will save name of particular. (string)
    > nickname  - this column will save nickname of particular (string)
    > email     - this column will save email id of particular (dictionary)
    > phone     - this column will save phone number of particular. (dictionary)
    > address   - this column will save address of particular. (dictionary)
    > work info - this column will save work info of particular. (string)
    > website   - this column will save website related to particular. (list) (if any)
    > group     - this will save the group constraint for any particular. (list) (if any)

-> division will be applied on this as key in dictionary and it will save data in "default" by default.

an example file is given below with proper format :

-> # This is an example row :
->
-> ["Rakesh Singh",["nennu bhaiya","mantu"],{"default":[9653829521,3524719482]},{"default":["duckie.od@xyz.com"]
-> },{"default":[],"home":["beside alam bagh mosque, jabalpur"]},"advocate",["bharatfirm.com"],["friend"]]
->
