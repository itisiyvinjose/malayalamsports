__author__ = 'Iyvin'

# custom manager classes
from django.db import models
from django.db.models import Q
from api.localisation import constants


class ActiveNewsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveNewsManager, self).get_queryset().filter(is_active=True)


