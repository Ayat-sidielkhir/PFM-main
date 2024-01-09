# category/admin.py
from django.contrib import admin
from .models import Category  # Importez la classe Category depuis le fichier models.py de votre application

# Register your models here.
admin.site.register(Category)
