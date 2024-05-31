from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from . models import Customer, Menu, ReserveTable, ExclusiveReserveTable
from .forms import AdminRegisterForm, CustomerForm, MenuForm, ReservationForm, ExclusiveReservationForm

def test(request):
    return render(request, "test.html")

# View to render user navigation bar
def user_navbar(request):
    return render(request, "user_navbar.html", {'user': request.user})

# View to render home page
def home(request):
    return render(request, "home.html")
    
# View to render menu page
def Full_Menu(request):
    return render(request, "Menu/Full Menu.html")


# ANTIPASTI
def Antipasti(request):
    return render(request, "Menu/Antipasti.html")

def Spinach_Trifolate(request):
    return render(request, "Menu/Antipasti/Spinach Trifolate.html")

def Cozze_Ubriachi_Bianco(request):
    return render(request, "Menu/Antipasti/Cozze Ubriachi Bianco.html")

def Parmigiana_Di_Melanzane(request):
    return render(request, "Menu/Antipasti/Parmigiana Di Melanzane.html")

def Prosciutto_Farcito(request):
    return render(request, "Menu/Antipasti/Prosciutto Farcito.html")

def Dita_Di_Pollo_Caprese(request):
    return render(request, "Menu/Antipasti/Dita Di Pollo Caprese.html")

def Molluschi(request):
    return render(request, "Menu/Antipasti/Molluschi.html")

def Prosciutto_Di_Parma_Con_Mango(request):
    return render(request, "Menu/Antipasti/Prosciutto Di Parma Con Mango.html")

def Gamberi_Alla_Griglia(request):
    return render(request, "Menu/Antipasti/Gamberi Alla Griglia.html")

def Salmone_Affucimato(request):
    return render(request, "Menu/Antipasti/Salmone Affucimato.html")

def Calamari_Fritti(request):
    return render(request, "Menu/Antipasti/Calamari Fritti.html")

def Sicilian(request):
    return render(request, "Menu/Antipasti/Sicilian.html")

def Bruschetta_Di_Parma(request):
    return render(request, "Menu/Antipasti/Bruschetta Di Parma.html")

def Bruschetta_Al_Fungo(request):
    return render(request, "Menu/Antipasti/Bruschetta Al Fungo.html")

def Funghi_Ripieni(request):
    return render(request, "Menu/Antipasti/Funghi Ripieni.html")


# INSALATA
def Insalata(request):
    return render(request, "Menu/Insalata.html")

def Caesar(request):
    return render(request, "Menu/Insalata/Caesar.html")

def Mista(request):
    return render(request, "Menu/Insalata/Mista.html")

def Greca(request):
    return render(request, "Menu/Insalata/Greca.html")

def Caprese(request):
    return render(request, "Menu/Insalata/Caprese.html")

def Piccante(request):
    return render(request, "Menu/Insalata/Piccante.html")

def Mare(request):
    return render(request, "Menu/Insalata/Mare.html")


# ZUPPA
def Zuppa(request):
    return render(request, "Menu/Zuppa.html")

def Cippole(request):
    return render(request, "Menu/Zuppa/Cippole.html")

def Vongole(request):
    return render(request, "Menu/Zuppa/Vongole.html")

def Brodetto_Di_Mare(request):
    return render(request, "Menu/Zuppa/Brodetto Di Mare.html")

def Funghi(request):
    return render(request, "Menu/Zuppa/Funghi.html")

def Minestrone_Di_Verdure(request):
    return render(request, "Menu/Zuppa/Minestrone Di Verdure.html")


# PANINI
def Panini(request):
    return render(request, "Menu/Panini.html")

def Rustica(request):
    return render(request, "Menu/Panini/Rustica.html")

def Mortadella(request):
    return render(request, "Menu/Panini/Mortadella.html")

def Pollo(request):
    return render(request, "Menu/Panini/Pollo.html")

def Al_Tono(request):
    return render(request, "Menu/Panini/Al Tono.html")

def Pesce_Filetto(request):
    return render(request, "Menu/Panini/Pesce Filetto.html")


# RISOTTO
def Risotto(request):
    return render(request, "Menu/Risotto.html")

def Porcini(request):
    return render(request, "Menu/Risotto/Porcini.html")

def Marinara(request):
    return render(request, "Menu/Risotto/Marinara.html")

def Colorata(request):
    return render(request, "Menu/Risotto/Colorata.html")


# PIZZA
def Pizza(request):
    return render(request, "Menu/Pizza.html")

def Quattro_Formaggi(request):
    return render(request, "Menu/Pizza/Quattro Formaggi.html")

def Due_Gusti(request):
    return render(request, "Menu/Pizza/Due Gusti.html")

def Margherita(request):
    return render(request, "Menu/Pizza/Margherita.html")

def Pepperoni(request):
    return render(request, "Menu/Pizza/Pepperoni.html")

def La_Loca(request):
    return render(request, "Menu/Pizza/La Loca.html")

def Frutti_Di_Mare(request):
    return render(request, "Menu/Pizza/Frutti Di Mare.html")

def Cacciatora(request):
    return render(request, "Menu/Pizza/Cacciatora.html")

def La_Nuova(request):
    return render(request, "Menu/Pizza/La Nuova.html")

def Tropicale(request):
    return render(request, "Menu/Pizza/Tropicale.html")

def Calzone_Siciliana(request):
    return render(request, "Menu/Pizza/Calzone Siciliana.html") 



# PASTA
def Pasta(request):
    return render(request, "Menu/Pasta.html")

# OLIVE OIL - PASTA
def Vongole_Al_Vino_Bianco(request):
    return render(request, "Menu/Pasta/Olive Oil/Vongole Al Vino Bianco.html")

def Gamberi(request):
    return render(request, "Menu/Pasta/Olive Oil/Gamberi.html")

def Salsiccia(request):
    return render(request, "Menu/Pasta/Olive Oil/Salsiccia.html")

def Misto_De_Pesce(request):
    return render(request, "Menu/Pasta/Olive Oil/Misto De Pesce.html")

def Nera(request):
    return render(request, "Menu/Pasta/Olive Oil/Nera.html")

def Primavera(request):
    return render(request, "Menu/Pasta/Olive Oil/Primavera.html")

def Angulas(request):
    return render(request, "Menu/Pasta/Olive Oil/Angulas.html")

# CREAM - PASTA
def Profumo_Di_Tartufo(request):
    return render(request, "Menu/Pasta/Cream/Profumo Di Tartufo.html")

def Carbonara(request):
    return render(request, "Menu/Pasta/Cream/Carbonara.html")

def Salmone(request):
    return render(request, "Menu/Pasta/Cream/Salmone.html")

def Capesante(request):
    return render(request, "Menu/Pasta/Cream/Capesante.html")

def Chicken_Alfredo(request):
    return render(request, "Menu/Pasta/Cream/Chicken Alfredo.html")

def Ravioli_Funghi(request):
    return render(request, "Menu/Pasta/Cream/Ravioli Funghi.html")

# TOMATO - PASTA
def Bolognese(request):
    return render(request, "Menu/Pasta/Tomato/Bolognese.html")

def Puttanesca(request):
    return render(request, "Menu/Pasta/Tomato/Puttanesca.html")

def Arrabiata(request):
    return render(request, "Menu/Pasta/Tomato/Arrabiata.html")

def Pescatora(request):
    return render(request, "Menu/Pasta/Tomato/Pescatora.html")

def Ravioli_Verde(request):
    return render(request, "Menu/Pasta/Tomato/Ravioli Verde.html")

# PESTO - PASTA
def Conn_Aglio_Olio(request):
    return render(request, "Menu/Pasta/Pesto/Conn Aglio Olio.html")

def Nina(request):
    return render(request, "Menu/Pasta/Pesto/Nina.html")

def Di_Mare(request):
    return render(request, "Menu/Pasta/Pesto/Di Mare.html")

def La_Nuova(request):
    return render(request, "Menu/Pasta/Pesto/La Nuova.html")

def Chorizo(request):
    return render(request, "Menu/Pasta/Pesto/Chorizo.html")

# SECONDI
def Secondi(request):
    return render(request, "Menu/Secondi.html")

# PESCE/FISH
def Al_Forno(request):
    return render(request, "Menu/Secondi/Pesce/Al Forno.html")

def Filetto_Mugnaia(request):
    return render(request, "Menu/Secondi/Pesce/Filetto Mugnaia.html")

def Filetto_Di_Salmon(request):
    return render(request, "Menu/Secondi/Pesce/Filetto Di Salmon.html")

def Grigilia_Di_Pesce(request):
    return render(request, "Menu/Secondi/Pesce/Grigilia Di Pesce.html")

def Cacciuco_Alla_Livornese(request):
    return render(request, "Menu/Secondi/Pesce/Cacciuco Alla Livornese.html")

# POLLO/CHICKEN
def Petto_Funghi(request):
    return render(request, "Menu/Secondi/Pollo/Petto Funghi.html")

def Petto_Asparagi(request):
    return render(request, "Menu/Secondi/Pollo/Petto Asparagi.html")

def Petto_Alexi(request):
    return render(request, "Menu/Secondi/Pollo/Petto Alexi.html")

def Accrotolato(request):
    return render(request, "Menu/Secondi/Pollo/Accrotolato.html")

def Petto_Diavola(request):
    return render(request, "Menu/Secondi/Pollo/Petto Diavola.html")

# MANZO/BEEF
def Filetto_Di_Manzo_Ai_Funghi(request):
    return render(request, "Menu/Secondi/Manzo/Filetto Di Manzo Ai Funghi.html")

def Agnello_Alla_Scottadito(request):
    return render(request, "Menu/Secondi/Manzo/Agnello Alla Scottadito.html")

def La_Bistecca(request):
    return render(request, "Menu/Secondi/Manzo/La Bistecca.html")

def Vitello_Alla_Milanese(request):
    return render(request, "Menu/Secondi/Manzo/Vitello Alla Milanese.html")

def Vitello_Al_Marsala(request):
    return render(request, "Menu/Secondi/Manzo/Vitello Al Marsala.html")

def Vitello_Ai_Funghi(request):
    return render(request, "Menu/Secondi/Manzo/Vitello Ai Funghi.html")


# CAFFE
def Caffe(request):
    return render(request, "Menu/Caffe.html")

def Bevande(request):
    return render(request, "Menu/Bevande.html")

def Ice_Cream(request):
    return render(request, "Menu/Ice Cream.html")

def Cake(request):
    return render(request, "Menu/Cake.html")

def Wine(request):
    return render(request, "Menu/Wine.html")

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

# def chatbot(request):
#     return render(request, "chatbot.html")  

# View for admin login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.cookie_name = settings.SESSION_COOKIE_NAME
            return redirect('admin_dashboard')  # Redirect to admin dashboard if authentication is successful       
        else:
            messages.error(request, 'Invalid username or password.')
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
    if request.user.is_authenticated:
        return render(request, "Admin/admin_dashboard.html")
    else:
        messages.error(request, "You are not logged in!")
        return redirect('admin_login')
    
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
        messages.error(request, "You are not logged in!")
        return redirect('admin_login')

# View to display specific customer record
def customer_record(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, "Admin/Customer/customer_record.html", {'customer': customer_record})
    else:
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
        return redirect(request, 'admin_login')
    
# View to render admin menu page
def admin_menu(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        menu = Menu.objects.all().order_by('id')        
        return render(request, "Admin/admin_menu.html", {'menu': menu})
    else:
        messages.error(request, "You are not logged in!")
        return redirect('admin_login')

# View to display a specific menu record
def menu_record(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        menu_record = Menu.objects.get(id=pk)
        return render(request, "Admin/Menu/menu_record.html", {'menu_record': menu_record})
    else:
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
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
            return redirect('menu_record', pk=pk)
        return render(request, "Admin/Menu/update_menu.html", {"form": form})
    else:
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
        return redirect(request, 'admin_login')

# View to render admin reservation page
def admin_reservation(request):
    if request.user.is_authenticated:
        reservation = ReserveTable.objects.all()
        return render(request, "Admin/admin_reservation.html", {'reservation': reservation})
    else:
        messages.error(request, "You are not logged in!")
        return redirect("admin_login")

# View to display a specific reservation record
def reservation_record(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ReserveTable.objects.get(id=pk)
        return render(request, "Admin/Reservation/reservation_record.html", {'reservation_record': reservation_record})
    else:
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
        return redirect(request, 'admin_login')


def admin_exclusivereservation(request):
    if request.user.is_authenticated:
        exclusive = ExclusiveReserveTable.objects.all()
        return render(request, "Admin/admin_exclusivereservation.html", {'exclusive': exclusive})
    else:
        messages.error(request, "You are not logged in!")
        return redirect("admin_login")


def exclusivereservation_record(request):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ExclusiveReserveTable.objects.all()
        return render(request, "Admin/Exclusive/exclusive_record.html", {'reservation_record': reservation_record})
    else:
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
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
        messages.error(request, "You are not logged in!")
        return redirect(request, 'admin_login')
    
def delete_exclusivereservation(request, pk):
    # Check if the user is logged in
    if request.user.is_authenticated:
        reservation_record = ExclusiveReserveTable.objects.get(id=pk)
        reservation_record.delete()
        messages.success(request, "Record Deleted Successfully...")
        return redirect ('admin_exclusivereservation')
    else:
        messages.error(request, "You are not logged in!")
        return redirect(request, 'admin_login')