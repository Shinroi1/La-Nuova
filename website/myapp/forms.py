from django import forms
from . models import Customer, Menu, ReserveTable, ExclusiveReserveTable
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django_select2.forms import Select2MultipleWidget

class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=65)
    last_name = forms.CharField(max_length=65)
        
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','password1', 'password2')
        
class CustomerForm(forms.ModelForm):
    
    fullname = forms.CharField(required=True ,max_length=65)
    address = forms.CharField(required=True, max_length=65)
    phone = forms.CharField(required=True, max_length=11)
    
    class Meta:
        model = Customer
        fields = ('fullname', 'address' , 'phone')
        
class MenuForm(forms.ModelForm):
    
    dish_name = forms.CharField(required=True ,max_length=65)
    category = forms.CharField(required=True, max_length=65)
    sub_category = forms.CharField(required=True, max_length=65)
    ingredients = forms.CharField(required=True, max_length=200)
    price = forms.DecimalField(required=True, decimal_places=2, max_digits=10)
    
    class Meta:
        model = Menu
        fields = ('dish_name', 'category', 'sub_category' ,'ingredients', 'price')
        
class ReservationForm(forms.ModelForm):
    fullname = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    table_number = forms.CharField(required=True, max_length=20, help_text="Maximum of tables are 11")  
    party_size = forms.IntegerField(required=True, validators=[MinValueValidator(1), MaxValueValidator(12)], help_text="Maximum of 12 party size")
    dish_name = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        widget=Select2MultipleWidget,  # Use Select2MultipleWidget here
        required=False
    )
    total_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)    
    table_status = forms.ChoiceField(choices=ReserveTable.TABLESTATUS, required=True)
    
    def clean(self):
        cleaned_data = super().clean()
        dish_names = cleaned_data.get('dish_name')

        # Calculate total price if dishes are selected
        if dish_names:
            total_price = sum(menu.price for menu in dish_names)
        else:
            total_price = 0

        cleaned_data['total_price'] = total_price

        return cleaned_data

    class Meta:
        model = ReserveTable
        fields = ('fullname', 'table_number', 'party_size', 'dish_name', 'table_status', 'total_price')
        
class ExclusiveReservationForm(forms.ModelForm):
    fullname = forms.ModelChoiceField(queryset=Customer.objects.all(), required=True)
    party_size = forms.IntegerField(required=True, validators=[MinValueValidator(1), MaxValueValidator(12)], help_text="Maximum of 12 party size")
    dish_name = forms.ModelMultipleChoiceField(
        queryset=Menu.objects.all(),
        widget=Select2MultipleWidget,  # Use Select2MultipleWidget here
        required=False
    )
    total_price = forms.DecimalField(max_digits=10, decimal_places=2, required=False)    
    table_status = forms.ChoiceField(choices=ReserveTable.TABLESTATUS, required=True)
    reservation_start_time = forms.TimeField(input_formats=["%I:%M%p"], required=True)
    reservation_end_time = forms.TimeField(input_formats=["%I:%M%p"], required=True)
    reservation_duration_hours = forms.IntegerField(required=True, validators=[MinValueValidator(1)], help_text="Maximum of 3 hours")

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("reservation_start_time")
        end_time = cleaned_data.get("reservation_end_time")

        if start_time and end_time:
            cleaned_data["time_range"] = f"{start_time.strftime('%I:%M%p')}-{end_time.strftime('%I:%M%p')}"

    def clean(self):
        cleaned_data = super().clean()
        dish_names = cleaned_data.get('dish_name')

        # Calculate total price if dishes are selected
        if dish_names:
            total_price = sum(menu.price for menu in dish_names)
        else:
            total_price = 0

        cleaned_data['total_price'] = total_price

        return cleaned_data
    
    class Meta:
        model = ExclusiveReserveTable
        fields = ('fullname','party_size', 'dish_name', 'total_price','table_status', 'reservation_start_time', 'reservation_end_time','reservation_duration_hours')