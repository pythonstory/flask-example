# Flask-boilerplate

## Requirements

* Flask
* Flask-script
* Flask-SQLAlchemy
* Flask-WTP

## Features

* Custom config file support
* Structure with blueprint
    * templates and static folders
    * theme supported

## Configuration and Run

It is not recommended to use ```config.py``` for your production server.

You have to have your own config file such as ```config_production.py```, and you can run as shown below:

```
python manage.py -c config_production runserver
```

If you not specify ```-c``` option, it will import the default ```config.py```.

## Commands

### runserver

### shell

## TODO

* Themes with AlloyUI
* Models/Forms file
* Time(moment)
* i18n/l10n
* Logger
* Mail
* Flask-migrate
* db.create_all(), db.drop_all() command
* Tests

## References

* Flask Web Development - Chapter 7, Miguel Grinberg, O'Reilly
* [How to Structure Large Flask Applications](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
* [Modular Applications with Blueprints](http://flask.pocoo.org/docs/0.11/blueprints/#blueprints)
