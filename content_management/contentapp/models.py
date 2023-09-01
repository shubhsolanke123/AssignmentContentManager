from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator


# Created models and applied field validation.

class UserDetails(models.Model):
   email = models.EmailField(
        unique=True,
        validators=[EmailValidator(message='Please provide a valid email address.')]
    )
   password = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(8, message='Password must be at least 8 characters long.'),])
   first_name = models.CharField(
        max_length=30,
        validators=[RegexValidator(r'^[a-zA-Z]*$', message='First name should only contain alphabetic characters.')]
    )
    
   last_name = models.CharField(
        max_length=30,
        validators=[RegexValidator(r'^[a-zA-Z]*$', message='Last name should only contain alphabetic characters.')]
    )
   phone = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(10, message='Phone number must be exactly 10 digits long.'),
            RegexValidator(r'^\d+$', message='Phone number should only contain numeric digits.')
        ]
    )
   address=models.CharField(max_length=50,blank=True)
   city=models.CharField(max_length=50,blank=True)
   state=models.CharField(max_length=50,blank=True)
   country=models.CharField(max_length=50,blank=True)
   pincode = models.CharField(
        max_length=6,
        validators=[
            MinLengthValidator(6, message='Pincode must be exactly 6 digits long.'),
            RegexValidator(r'^\d+$', message='Pincode should only contain numeric digits.')
        ]
    )


class Content(models.Model):
    title=models.CharField(max_length=30)
    body=models.CharField(max_length=300)
    summary=models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/')
    CATEGORY_CHOICES = (
        ('technology', 'Technology'),
        ('science', 'Science'),
        ('travel', 'Travel'),
        ('food', 'Food'),
        
    )
    categories = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    userdetails = models.ForeignKey(UserDetails, on_delete=models.CASCADE,null=True)