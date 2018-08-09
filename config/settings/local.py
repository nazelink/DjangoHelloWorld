from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='475pyo@bs8w@q(!987@@u%2cj$!hwj+i*fbco8@uhzam6_*$qr')

DEBUG = env.bool('DJANGO_DEBUG', True)