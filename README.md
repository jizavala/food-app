# Food APP
An API made with Flask, to track the total calories and macronutrients of food.

# Index

# Installation
## Virtual Enviroment Configuration

    #In Python >= 3.6
    $ python3 -m venv path/to/your/proyect

    #UIn Python < 3.6
    $ python3 pip install virtualenv
    $ python3 -m virtualenv path/to/your/proyect

    #When the virtual enviroment is created use, the following command to start the virtual enviroment
    $ [venv|virtualenv] source bin/activate

    #To deactivate the virtual enviroment, and work with you normal installation of python.
    $ deactivate

## Using and Installing flask-mysqldb instead of flask-SQLALchemy

One thing that I found is, if you don't have installed, this libmysqlclient-dev python-dev this library will be not installed until you install the first ones

     #Install the libraries using sudo
     $ sudo apt-get install libmysqlclient-dev python-dev

And woala, you can install now the library without a problem.
