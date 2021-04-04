"""user models"""
#django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#utilites
from cride.utils.models import CRideModel


class Users(AbstractUser, CRideModel):
    """
    extend form Django's Abstract user, change the username field
    to email and add some extra fields
    """
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique':'User Already Exists'
        }
    )

    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message='phone number must be entered in the format: +999999999. up to 15 digists allowed'
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    is_client = models.BooleanField(
        'client status',
        default = True,
        help_text = (
            'help easily distinguish users and perform queries'
            'clientes are the main type of users'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default = True,
        help_text = 'set to true when the user have veified its email addres'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username