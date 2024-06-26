from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('footer/', views.footer, name="footer"),
    path('reservations/', views.reservations, name = "reservations"),         
    path('user_navbar/', views.user_navbar, name="user_navbar"),
    
    # CHATBOT
    #path('chatbot/', views.chatbot, name="chatbot"),
    path('test/', views.test, name="test"),

    
    # MENU
    path('Menu/Full Menu/', views.Full_Menu, name = "Full Menu"),    
    
    # ANTIPASTI/PASTA
    path('Menu/Antipasti/', views.Antipasti, name = "Antipasti"),    
    path('Menu/Antipasti/Spinach Trifolate/', views.Spinach_Trifolate, name="Spinach Trifolate"),
    path('Menu/Antipasti/Cozze Ubriachi Bianco/', views.Cozze_Ubriachi_Bianco, name="Cozze Ubriachi Bianco"),
    path('Menu/Antipasti/Parmigiana Di Melanzane/', views.Parmigiana_Di_Melanzane, name="Parmigiana Di Melanzane"),
    path('Menu/Antipasti/Prosciutto Farcito/', views.Prosciutto_Farcito, name="Prosciutto Farcito"),
    path('Menu/Antipasti/Gamberi Alla Griglia/', views.Gamberi_Alla_Griglia, name="Gamberi Alla Griglia"),
    path('Menu/Antipasti/Bruschetta Di Parma/', views.Bruschetta_Di_Parma, name="Bruschetta Di Parma"),
    path('Menu/Antipasti/Bruschetta Al Fungo/', views.Bruschetta_Al_Fungo, name="Bruschetta Al Fungo"),
    path('Menu/Antipasti/Funghi Ripieni/', views.Funghi_Ripieni, name="Funghi Ripieni"),
    path('Menu/Antipasti/Dita di Pollo Caprese/', views.Dita_Di_Pollo_Caprese, name="Dita Di Pollo Caprese"),
    path('Menu/Antipasti/Molluschi/', views.Molluschi, name="Molluschi"),
    path('Menu/Antipasti/Prosciutto Di Parma Con Mango/', views.Prosciutto_Di_Parma_Con_Mango, name="Prosciutto Di Parma Con Mango"),
    path('Menu/Antipasti/Salmone Affucimato/', views.Salmone_Affucimato, name="Salmone Affucimato"),
    path('Menu/Antipasti/Calamari Fritti/', views.Calamari_Fritti, name="Calamari Fritti"),
    path('Menu/Antipasti/Sicilian/', views.Sicilian, name="Sicilian"),
    
    # INSALATA/SALAD
    path('Menu/Insalata/', views.Insalata, name = "Insalata"),  
    path('Menu/Insalata/Caesar/', views.Caesar, name="Caesar"),
    path('Menu/Insalata/Mista/', views.Mista, name="Mista"),
    path('Menu/Insalata/Greca/', views.Greca, name="Greca"),
    path('Menu/Insalata/Caprese/', views.Caprese, name="Caprese"),
    path('Menu/Insalata/Piccante/', views.Piccante, name="Piccante"),
    path('Menu/Insalata/Mare/', views.Mare, name="Mare"),
        
    # ZUPPA/SOUP
    path('Menu/Zuppa/', views.Zuppa, name = "Zuppa"),
    path('Menu/Zuppa/Cippole/', views.Cippole, name="Cippole"),
    path('Menu/Zuppa/Vongole/', views.Vongole, name="Vongole"),
    path('Menu/Zuppa/Brodetto Di Mare/', views.Brodetto_Di_Mare, name="Brodetto Di Mare"),
    path('Menu/Zuppa/Funghi/', views.Funghi, name="Funghi"),
    path('Menu/Zuppa/Minestrone Di Verdure/', views.Minestrone_Di_Verdure, name="Minestrone Di Verdure"),

    # PANINI/SANDWICHES
    path('Menu/Panini/', views.Panini, name = "Panini"),
    path('Menu/Panini/Pollo/', views.Pollo, name="Pollo"),
    path('Menu/Panini/Al Tono/', views.Al_Tono, name="Al Tono"),
    path('Menu/Panini/Pesce Filetto/', views.Pesce_Filetto, name="Pesce Filetto"),
    path('Menu/Panini/Rustica/', views.Rustica, name="Rustica"),
    path('Menu/Panini/Mortadella/', views.Mortadella, name="Mortadella"),
    
    # RISOTTO
    path('Menu/Risotto/', views.Risotto, name = "Risotto"),
    path('Menu/Risotto/Porcini/', views.Porcini, name="Porcini"),
    path('Menu/Risotto/Marinara/', views.Marinara, name="Marinara"),
    path('Menu/Risotto/Colorata/', views.Colorata, name="Colorata"),

    # PIZZA
    path('Menu/Pizza/', views.Pizza, name = "Pizza"),
    path('Menu/Pizza/Quattro Formaggi/', views.Quattro_Formaggi, name="Quattro Formaggi"),
    path('Menu/Pizza/Due Gusti/', views.Due_Gusti, name="Due Gusti"),
    path('Menu/Pizza/La Loca/', views.La_Loca, name="La Loca"),
    path('Menu/Pizza/Margherita/', views.Margherita, name="Margherita"),
    path('Menu/Pizza/Pepperoni/', views.Pepperoni, name="Pepperoni"),
    path('Menu/Pizza/Frutti Di Mare/', views.Frutti_Di_Mare, name="Frutti Di Mare"),
    path('Menu/Pizza/Cacciatora/', views.Cacciatora, name="Cacciatora"),
    path('Menu/Pizza/La Nuova/', views.La_Nuova, name="La Nuova"),
    path('Menu/Pizza/Tropicale/', views.Tropicale, name="Tropicale"),
    path('Menu/Pizza/Calzone Siciliana/', views.Calzone_Siciliana, name="Calzone Siciliana"),
    
    # PASTA
    path('Menu/Pasta/', views.Pasta, name = "Pasta"),    
    
    # OLIVE OIL
    path('Menu/Pasta/Olive Oil/Vongole Al Vino Bianco/', views.Vongole_Al_Vino_Bianco, name="Vongole Al Vino Bianco"),
    path('Menu/Pasta/Olive Oil/Gamberi/', views.Gamberi, name="Gamberi"),
    path('Menu/Pasta/Olive Oil/Salsiccia/', views.Salsiccia, name="Salsiccia"),
    path('Menu/Pasta/Olive Oil/Misto De Pesce/', views.Misto_De_Pesce, name="Misto De Pesce"),
    path('Menu/Pasta/Olive Oil/Nera/', views.Nera, name="Nera"),
    path('Menu/Pasta/Olive Oil/Primavera/', views.Primavera, name="Primavera"),
    path('Menu/Pasta/Olive Oil/Angulas/', views.Angulas, name="Angulas"),
    
    # CREAM
    path('Menu/Pasta/Cream/Profumo Di Tartufo/', views.Profumo_Di_Tartufo, name="Profumo Di Tartufo"),
    path('Menu/Pasta/Cream/Carbonara/', views.Carbonara, name="Carbonara"),
    path('Menu/Pasta/Cream/Salmone/', views.Salmone, name="Salmone"),
    path('Menu/Pasta/Cream/Capesante/', views.Capesante, name="Capesante"),
    path('Menu/Pasta/Cream/Chicken Alfredo/', views.Chicken_Alfredo, name="Chicken Alfredo"),
    path('Menu/Pasta/Cream/Ravioli Funghi/', views.Ravioli_Funghi, name="Ravioli Funghi"),
    
    # TOMATO
    path('Menu/Pasta/Tomato/Puttanesca/', views.Puttanesca, name="Puttanesca"),
    path('Menu/Pasta/Tomato/Arrabiata/', views.Arrabiata, name="Arrabiata"),
    path('Menu/Pasta/Tomato/Pescatora/', views.Pescatora, name="Pescatora"),
    path('Menu/Pasta/Tomato/Ravioli Verde/', views.Ravioli_Verde, name="Ravioli Verde"),
    path('Menu/Pasta/Tomato/Bolognese/', views.Bolognese, name="Bolognese"),

    # PESTO
    path('Menu/Pasta/Pesto/Conn Aglio Olio/', views.Conn_Aglio_Olio, name="Conn Aglio Olio"),
    path('Menu/Pasta/Pesto/Nina/', views.Nina, name="Nina"),
    path('Menu/Pasta/Pesto/Di Mare/', views.Di_Mare, name="Di Mare"),
    path('Menu/Pasta/Pesto/La Nuova/', views.La_Nuova, name="La Nuova"),
    path('Menu/Pasta/Pesto/Chorizo/', views.Chorizo, name="Chorizo"),

    # SECONDI
    path('Menu/Secondi/', views.Secondi, name = "Secondi"),
    
    # PESCE
    path('Menu/Secondi/Pesce/Al Forno/', views.Al_Forno, name="Al Forno"),
    path('Menu/Secondi/Pesce/Filetto Mugnaia/', views.Filetto_Mugnaia, name="Filetto Mugnaia"),
    path('Menu/Secondi/Pesce/Filetto Di Salmon/', views.Filetto_Di_Salmon, name="Filetto Di Salmon"),
    path('Menu/Secondi/Pesce/Grigilia Di Pesce/', views.Grigilia_Di_Pesce, name="Grigilia Di Pesce"),
    path('Menu/Secondi/Pesce/Cacciuco Alla Livornese/', views.Cacciuco_Alla_Livornese, name="Cacciuco Alla Livornese"),
    
    # POLLO
    path('Menu/Secondi/Pollo/Petto Funghi/', views.Petto_Funghi, name="Petto Funghi"),
    path('Menu/Secondi/Pollo/Petto Asparagi/', views.Petto_Asparagi, name="Petto Asparagi"),
    path('Menu/Secondi/Pollo/Petto Alexi/', views.Petto_Alexi, name="Petto Alexi"),
    path('Menu/Secondi/Pollo/Accrotolato/', views.Accrotolato, name="Accrotolato"),
    path('Menu/Secondi/Pollo/Petto Diavola/', views.Petto_Diavola, name="Petto Diavola"),
    
    # MANZO
    path('Menu/Secondi/Manzo/Filetto Di Manzo Ai Funghi/', views.Filetto_Di_Manzo_Ai_Funghi, name="Filetto Di Manzo Ai Funghi"),
    path('Menu/Secondi/Manzo/Agnello Alla Scottadito/', views.Agnello_Alla_Scottadito, name="Agnello Alla Scottadito"),
    path('Menu/Secondi/Manzo/La Bistecca/', views.La_Bistecca, name="La Bistecca"),
    path('Menu/Secondi/Manzo/Vitello Alla Milanese/', views.Vitello_Alla_Milanese, name="Vitello Alla Milanese"),
    path('Menu/Secondi/Manzo/Vitello Al Marsala/', views.Vitello_Al_Marsala, name="Vitello Al Marsala"),
    path('Menu/Secondi/Manzo/Vitello Ai Funghi/', views.Vitello_Ai_Funghi, name="Vitello Ai Funghi"),

    
    # CAFFE        
    path('Menu/Caffe/', views.Caffe, name = "Caffe"),
    
    # BEVERAGES
    path('Menu/Bevande/', views.Bevande, name = "Bevande"),
    path('Menu/Ice Cream/', views.Ice_Cream, name = "Ice Cream"),
    path('Menu/Cake/', views.Cake, name = "Cake"),
    path('Menu/Wine/', views.Wine, name = "Wine"),
    
    
    
    # CUSTOMER MANAGEMENT
    path('Admin/admin_customers/', views.admin_customers, name="admin_customers"),    
    path('Admin/Customer/customer_record/<int:pk>', views.customer_record, name="customer_record"),
    path('delete_customer/<int:pk>', views.delete_customer, name="delete_customer"),
    path('Admin/Customer/add_customer/', views.add_customer, name="add_customer"),
    path('Admin/Customer/update_customer/<int:pk>', views.update_customer, name="update_customer"),
    
    # MENU MANAGEMENT
    path('Admin/admin_menu/', views.admin_menu, name="admin_menu"),   
    path('Admin/Menu/menu_record/<int:pk>', views.menu_record, name="menu_record"),
    path('delete_menu/<int:pk>', views.delete_menu, name="delete_menu"),
    path('Admin/Menu/add_menu/', views.add_menu, name="add_menu"),
    path('Admin/Menu/update_menu/<int:pk>', views.update_menu, name="update_menu"),
    
    # RESERVATION MANAGEMENT
    path('Admin/admin_reservation/', views.admin_reservation, name="admin_reservation"),
    path('Admin/Reservation/reservation_record/<int:pk>', views.reservation_record, name="reservation_record"),
    path('delete_reservation/<int:pk>', views.delete_reservation, name="delete_reservation"),
    path('Admin/Reservation/add_reservation/', views.add_reservation, name="add_reservation"),
    path('Admin/Reservation/update_reservation/<int:pk>', views.update_reservation, name="update_reservation"),
    
    # EXCLUSIVE RESERVATION MANAGEMENT
    path('Admin/admin_exclusivereservation/', views.admin_exclusivereservation, name="admin_exclusivereservation"),
    path('Admin/Exclusive/exclusivereservation_record/<int:pk>', views.exclusivereservation_record, name="exclusivereservation_record"),
    path('delete_exclusivereservation/<int:pk>', views.delete_exclusivereservation, name="delete_exclusivereservation"),
    path('Admin/Exclusive/add_exclusivereservation/', views.add_exclusivereservation, name="add_exclusivereservation"),
    path('Admin/Exclusive/update_exclusivereservation/<int:pk>', views.update_exclusivereservation, name="update_exclusivereservation"),

    # ADMIN
    path('Admin/admin_dashboard/', views.admin_dashboard, name="admin_dashboard"), 
    path('Admin/admin_register/', views.admin_register, name="admin_register"),
    path('Admin/admin_login/', views.admin_login, name="admin_login"),
    path('logout/', views.logout_user,  name ="logout"),
    path('Admin/admin_main/', views.admin_main, name="admin_main"),    
    path('Admin/admin_navbar/', views.admin_navbar, name="admin_navbar"),    
]