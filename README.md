# Forum App

Hi guys!! I developed an application where users vote , this app would be useful at the election of the President or Parliament=))

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework Django
* [HTML](https://devdocs.io/html/) - HTML

## Getting Started

To run this project on you computer , just enter the following commands below

### Prerequisites

Before installation , check if you have installed Python3 with the command

```
python -V
```

### Installing

Open the console and select directory , install the virtual environment . Then we clone by typing the commands below
```
git clone https://github.com/therealoggng/forum_app.git
```

 We should also install dependencies

```
pip install -r requirements.txt
```

After installing dependencies we have to do the migrations
```
python manage.py makemigrations
```
We did migrations, but it's time to do it all
```
python manage.py migrate
```
start the server 
```
python manage.py runserver
```
go to the web browser and enter http://localhost:8000


