
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': "port_database",
        'USER': "portuser",
        'PASSWORD': "12345",
        'HOST': 'localhost',
        'PORT': '5433'
    }
}
DEBUG = True
