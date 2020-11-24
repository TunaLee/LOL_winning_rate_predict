# Python
import timeago

# Django
from django.db import models
from django.utils import timezone

# Third Party
from model_utils.models import TimeStampedModel


class Model(TimeStampedModel, models.Model):

    class Meta:
        abstract = True

    @property
    def time(self):
        return timeago.format(self.created, timezone.now(), 'ko')
