# Djnago
from django.contrib import admin
from django.db import models
from django.forms import Textarea


# Main Section
class Admin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': Textarea(attrs={'rows': 1, 'style': 'width: 70%;'})}, }
