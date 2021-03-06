from setuptools import setup, find_packages


setup(
    name = 'CS4300sp2017-jtc267kls294cdb239jds459',
    description = 'CS4300 project',
    url = 'https://github.com/cbora/cs4300sp2017',
    author = '',
    email = '',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'alembic==0.8.6',
        'aniso8601==1.1.0',
        'appdirs==1.4.3',
        'autoenv==1.0.0',
        'bcrypt==2.0.0',
        'cffi==1.6.0',
        'click==6.7',
        'Flask==0.10.1',
        'Flask-Bcrypt==0.7.1',
        'Flask-HTTPAuth==3.1.2',
        'Flask-JWT==0.3.2',
        'flask-marshmallow==0.6.2',
        'Flask-Migrate==1.8.0',
        'Flask-RESTful==0.3.5',
        'Flask-Script==2.0.5',
        'Flask-SocketIO==2.3',
        'Flask-SQLAlchemy==2.1',
        'Flask-WTF==0.12',
        'gevent==1.1.1',
        'greenlet==0.4.9',
        'gunicorn==19.7.0',
        'hiredis==0.2.0',
        'itsdangerous==0.24',
        'Jinja2==2.8',
        'Mako==1.0.4',
        'MarkupSafe==0.23',
        'marshmallow==2.7.3',
        'marshmallow-sqlalchemy==0.8.1',
        'nltk==3.2.2',
        'numpy==1.12.0',
        'packaging==16.8',
        'psycopg2==2.6.1',
        'pycparser==2.14',
        'PyJWT==1.4.0',
        'pyparsing==2.2.0',
        'python-dateutil==2.5.3',
        'python-editor==1.0',
        'python-engineio==0.9.1',
        'python-socketio==1.3',
        'pytz==2016.4',
        'redis==2.10.5',
        'requests==2.13.0',
        'scikit-learn==0.18.1',
        'scipy==0.19.0',
        'six==1.10.0',
        'SQLAlchemy==1.0.13',
        'Werkzeug==0.11.9',
        'WTForms==2.1'
        ],
    entry_points = {
        'console_scripts': [
            'cs4300 = app.frontendcli:frontendcli',
            'cs4300-admin = app.admincli:admincli'
            ]
        }
    )
        

    
