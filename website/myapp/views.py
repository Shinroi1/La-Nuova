from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . models import Customer, Menu, ReserveTable, ExclusiveReserveTable
from .forms import AdminRegisterForm, CustomerForm, MenuForm, ReservationForm, ExclusiveReservationForm

# View to render user navigation bar
def user_navbar(request):
    return render(request, "user_navbar.html", {'user': request.user})

# View to render home page
def home(request):
    return render(request, "home.html")
    
# View to render menu page
def menu(request):
    return render(request, "menu.html")

# View to render about page
def about(request):
    return render(request, "about.html")

# View to render menu choice page
def menu_choice(request):
    return render(request, "menu_choice.html")

# View to render reservations page
def reservations(request):
    return render(request, "reservations.html")

# View to render contact page
def contact(request):
    return render(request, "contact.html")

# View to render footer
def footer(request):
    return render(request, "footer.html")

def chatbot(request):
    return render(request, "chatbot.html")  

# View for admin login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']        
        password = request.POST['password']
        user = authenticate(request, username=username, email=email ,password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to admin dashboard if authentication is successful
        else:
            return render(request, 'Admin/admin_login.html')  # Render login page with error message if authentication fails
    else:
        return render(request, 'Admin/admin_login.html')

# View for admin registration
def admin_register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('admin_login.html')
    else:
        form = AdminRegisterForm()
        return render(request, 'Admin/admin_register.html', {'form': form})
    
    return render(request, 'Admin/admin_register.html', {'form': form})

# View to handle user logout
def logout_user(request):
    logout(request)
    messages.success(request, "You Logged Out...")
    return redirect('admin_login')

# View to render admin dashboard
def admin_dashboard(request):
    return render(request, "Admin/admin_dashboard.html")

# View to render admin main page
def admin_main(request):
    return render(request, "Admin/admin_main.html")

# View to render admin navigation bar
def admin_navbar(request):
    return render(request, "Admin/admin_navbar.html")

# View to display admin customers
def admin_customers(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        customers = Customer.objects.all()  
        return render(request, "Admin/admin_customers.html", {'customers': customers})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')

# View to display specific customer record
def customer_record(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, "Admin/Customer/customer_record.html", {'customer': customer_record})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')
    
# View to add a customer record
def add_customer(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        form = CustomerForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                    form.save()
                    messages.success(request, "Record Added Successfully...")
                    return redirect('admin_customers')
        else:
            messages.error(request, "Invalid form data.")
        return render(request, "Admin/Customer/add_customer.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')

# View to update a customer record
def update_customer(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        current_record = Customer.objects.get(id=pk)
        form = CustomerForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully...")
            return HttpResponseRedirect(reverse('admin_customers'))
        return render(request, "Admin/Customer/update_customer.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')
    
# View to delete a customer record
def delete_customer(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect ('admin_customers')
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')
    
# View to render admin menu page
def admin_menu(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        menu = Menu.objects.all().order_by('id')        
        return render(request, "Admin/admin_menu.html", {'menu': menu})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')

# View to display a specific menu record
def menu_record(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        menu_record = Menu.objects.get(id=pk)
        return render(request, "Admin/Menu/menu_record.html", {'menu_record': menu_record})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')
    
# View to add a menu record
def add_menu(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        form = MenuForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect('admin_customers')
        else:
            messages.error(request, "Invalid form data.")
        return render(request, "Admin/Menu/add_menu.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')

# View to update a menu record
def update_menu(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        current_record = Menu.objects.get(id=pk)
        form = MenuForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully...")
            return redirect('admin_menu')
        return render(request, "Admin/Menu/update_menu.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')
    
# View to delete a menu record
def delete_menu(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        menu_record = Menu.objects.get(id=pk)
        menu_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect ('admin_menu')
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')

# View to render admin reservation page
def admin_reservation(request):
    if request.user.is_authenticated:
        reservation = ReserveTable.objects.all()
        return render(request, "Admin/admin_reservation.html", {'reservation': reservation})
    else:
        messages.success(request, "You are not logged in!")
        return redirect("admin_login")

# View to display a specific reservation record
def reservation_record(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ReserveTable.objects.get(id=pk)
        return render(request, "Admin/Reservation/reservation_record.html", {'reservation_record': reservation_record})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')
    
# View to add a reservation record
def add_reservation(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        form = ReservationForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect('admin_reservation')
        else:
            messages.error(request, "Invalid form data.")
        return render(request, "Admin/Reservation/add_reservation.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')


# View to update a specific reservation record
def update_reservation(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        current_record = ReserveTable.objects.get(id=pk)
        form = ReservationForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully...")
            return redirect('admin_reservation')
        return render(request, "Admin/Reservation/update_reservation.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')

# View to delete a specific reservation record
def delete_reservation(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ReserveTable.objects.get(id=pk)
        reservation_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect ('admin_reservation')
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')


def admin_exclusivereservation(request):
    if request.user.is_authenticated:
        exclusive = ExclusiveReserveTable.objects.all()
        return render(request, "Admin/admin_exclusivereservation.html", {'exclusive': exclusive})
    else:
        messages.success(request, "You are not logged in!")
        return redirect("admin_login")


def exclusivereservation_record(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ExclusiveReserveTable.objects.all()
        return render(request, "Admin/Exclusive/exclusive_record.html", {'reservation_record': reservation_record})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')    

def add_exclusivereservation(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        form = ExclusiveReservationForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully...")
                return redirect('admin_exclusivereservation')
        else:
            messages.error(request, "Invalid form data.")
        return render(request, "Admin/Exclusive/add_exclusivereservation.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect('admin_login')
    
    
def update_exclusivereservation(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        current_record = ExclusiveReserveTable.objects.get(id=pk)
        form = ExclusiveReservationForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully...")
            return redirect('admin_exclusivereservation')
        return render(request, "Admin/Exclusive/update_exclusivereservation.html", {"form": form})
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')
    
def delete_exclusivereservation(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ExclusiveReserveTable.objects.get(id=pk)
        reservation_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect ('admin_exclusivereservation')
    else:
        messages.success(request, "You are not logged in!")
        return redirect(request, 'admin_login')