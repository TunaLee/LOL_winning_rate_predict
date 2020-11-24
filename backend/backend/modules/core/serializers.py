# Python
from collections import OrderedDict

# Django
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class ModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        create_only_fields = getattr(self.Meta, 'create_only_fields', [])
        for field_name in create_only_fields:
            field = self.fields.get(field_name)
            field.read_only = (self.instance is not None)
