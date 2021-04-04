"""Profile models"""
from django.db import models

from cride.utils.models import CRideModel

class Profile(CRideModel):
    """
    A profile holds a user's public data like biography, picture, and stataistics
    """

    user = models.OneToOneField('users.Users', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default = 5.0,
        help_text="user's reputation based on the rides taken and ofered"
    )

    def __str__(sefl):
        return str(self.user)
