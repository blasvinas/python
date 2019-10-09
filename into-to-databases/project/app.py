from database import Database
from user import User

Database.initialise(user='postgres', password='ys0828bv', database='learning', host='localhost')

my_user = User('anne@smith.com','Anne','Smith',None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('anne@smith.com')

print(user_from_db)


