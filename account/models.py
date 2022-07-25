from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES = (
        ('man', 'Man'),
        ('woman', 'Woman'),
    )
    gender = models.CharField('Gender', max_length=5, choices=GENDER_CHOICES, default=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    image = models.ImageField('Image', upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    @property
    def profile_picture(self):
        if self.image:
            return self.image


    def __str__(self):
        return self.email
