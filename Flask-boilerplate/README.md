# Flask-boilerplate

## Requirements

* Flask
* Flask-script
* Flask-SQLAlchemy
* Flask-WTP

## Configuration and Run

It is not recommended to use ```config.py``` for your production server.

You have to have your own config file such as ```config_production.py```, and you can run as shown below:

```
python manage.py -c config_production runserver
```
