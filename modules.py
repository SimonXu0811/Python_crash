# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date
import time
import validator
from validator import validate_email

# today = datetime.date.today()
# today = date.today()


timestamp = time.time()

print(timestamp)



email = "test#test.com"
if validate_email(email) :
    print("email is vailed")
else:
    print("email is bad")
# pip3 install modules