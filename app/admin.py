from django.contrib import admin
from app.models import Product, Review

admin.site.register([Product, Review])
