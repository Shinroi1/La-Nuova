from datetime import datetime,timedelta
from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


# Create your models here.
class Customer(models.Model):
    
    fullname = models.CharField(
        max_length=200, 
        null=True
        )
    
    address = models.CharField(
        max_length=200, 
        null=True
        )
    
    phone = models.CharField(
        max_length=11, 
        null=True
        )
    
    date_created = models.DateTimeField(
        auto_now_add=True, 
        null=True
        )
    
    def __str__(self):
        return  self.fullname        

class Menu(models.Model):
    dish_name = models.CharField(
        max_length=200, 
        null=True
        )
    
    category = models.CharField(
        max_length=200, 
        null=True
        )
    
    sub_category = models.CharField(
        max_length=200, 
        default="None"
        )
    
    ingredients = models.CharField(
        max_length=200, 
        null=True
        )
    
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        null=True
        )    
    
    def __str__(self):
        return f"{self.dish_name} {self.category}"
                
class ReserveTable(models.Model):
    TABLESTATUS = (
        ('Reserved', 'Reserved'), 
        ('Paid', 'Paid'),
        ('Completed', 'Completed'), # Means the customer/s is finished using the table
        ('Cancelled', 'Cancelled'),     
        )
    fullname = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        null=True
        )
        
    table_number = models.CharField(
        max_length=20, 
        null=True
        )
    
    party_size = models.IntegerField(
        default=1, 
        validators=[MinValueValidator(1), MaxValueValidator(12)]
        )    
    
    dish_name = models.ManyToManyField(Menu)
    
    total_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True
        )
    
    table_status = models.CharField(
        max_length=200, 
        null=True, 
        choices=TABLESTATUS
        )
    
    date_created = models.DateTimeField(
        auto_now_add=True, 
        null=True
        )

    def __str__(self):
        dish_names = ", ".join(str(menu) for menu in self.dish_name.all())
        
        return f"{self.table_number} {dish_names}"
    
class ExclusiveReserveTable(models.Model):
    
    TABLESTATUS = (
        ('Downpayment', 'Downpayment paid'),
        ('Reserved', 'Reserved for 3 hours'), 
        ('Paid', 'Complete Paid'),
        ('Cancelled', 'Cancelled'),
        )
    
    fullname = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE, 
        null=True
        )
    
    party_size = models.IntegerField(
        null=True, 
        validators=[MinValueValidator(1)]
        )
    
    dish_name = models.ManyToManyField(Menu)
    
    total_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True
        )
    
    table_status = models.CharField(
        max_length=200, 
        null=True, 
        choices=TABLESTATUS
        )
    
    date_created = models.DateTimeField(
        auto_now_add=True, 
        null=True
        )
    reservation_start_time = models.TimeField()
    
    reservation_end_time = models.TimeField()    
    
    reservation_duration_hours = models.IntegerField(
        default=3, 
        validators=[MinValueValidator(1)]
        )    
    
    def clean(self):
        
        if self.reservation_end_time <= self.reservation_start_time:
            raise ValidationError("Reservation duration must be a positive integer.")
        
        start_time = datetime.combine(
            self.date_created, 
            self.reservation_start_time
            ) 
        
        end_time = datetime.combine(
            self.date_created, 
            self.reservation_end_time
            )
        
        duration_hour = (start_time - end_time).total_seconds() / 3600
        
        if duration_hour < self.reservation_duration_hours:
            raise ValidationError("Reservation duration must be greater than or equal to 3 hours.")

    def __str__(self):
        dish_names = ", ".join(str(menu) for menu in self.dish_name.all())
        return f"{dish_names}"

class Interaction(models.Model):
    
    session_id = models.CharField(
        max_length=50,
        default=uuid4,
        unique=True
        )
    
    user_message = models.TextField()
    
    bot_response = models.TextField()
    
    timestamp = models.DateTimeField(
        auto_now_add=True
        )
    
    def __str__(self) -> str:
        return f"Session {self.session_id} - Interaction on {self.timestamp} - Message: {self.user_message[:30]}..."