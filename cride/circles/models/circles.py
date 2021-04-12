from django.db import models 

from cride.utils.models import CRideModel

class Circle(CRideModel):
    """Circle model
    A circle is a priivate group where rides are oddered and taken
    by its members. To join a circle a user must recived 
    """

    name = models.CharField('circle name',max_length=140)
    slug_name = models.SlugField(unique=True,max_length=40)

    about = models.CharField('circle description',max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)

    #stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)
    
    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='verified Circles are also known as official communities'
    )

    is_public = models.BooleanField(
        default = True,
        help_text = 'Public circles are listed in the main page so everyone can see this group'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text="limited circles can grow up to a fixed numbber of members"
    )
    members_limit = models.PositiveIntegerField(default=0,help_text = "if circles is limited, this will be the limit on the  numbers of members")

    def __str__(self):
        return self.name

    class Meta(CRideModel.Meta):
        ordering = ['-rides_taken', '-rides_offered']