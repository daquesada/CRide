"""
Django models utilities.
"""
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base Model
    CRideModel acts as an abstract base clase from which every
    other model in this project will inherit. This class provides
    every table with the following attributes
        *created(DateTime):Store the datetime the object was created
        *modified(DataTime):Store the las datetime the object was modified
    """

    created = models.DateTimeField('created at',
        auto_now_add=True,
        help_text='date Time on which the object was created'
    )
    modified = models.DateTimeField('modified at',
        auto_now_add=True,
        help_text='date Time on which the object was last modified'
    )
    class Meta:
        """Meta options"""
        abstract = True
        get_latest_by = 'created'
        ordering =['-created','-modified']
