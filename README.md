The first thing to do is to clone the repository:

$ git clone https://github.com/rxg8255/inventoryAPIs_Django.git
$ cd inventoryAPIs_Django
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd inventoryAPIs_Django
(env)$ python manage.py runserver