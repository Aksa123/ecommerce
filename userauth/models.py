from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator
from decimal import Decimal



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name2 = models.CharField(max_length=100, default="", blank=True, null=True)
    gender = models.CharField(max_length=25, default="unknown", blank=True, null=True)
    role = models.CharField(max_length=100, default="normal", blank=True, null=True)
    money = models.DecimalField(decimal_places=2, default=0.00,validators=[MinValueValidator(Decimal('0.00'))], help_text="Your money", max_digits=10)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)