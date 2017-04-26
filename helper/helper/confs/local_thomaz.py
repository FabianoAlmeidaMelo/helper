from helper.settings import * # noqa


SECRET_KEY = 'yjy7z*_n@w3%r%g8l$b$i@f(j-+@1u^$djodm-o@syrv(vcg)s'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'helper.sqlite3',
    }
}
