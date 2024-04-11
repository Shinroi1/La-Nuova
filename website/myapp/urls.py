from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('footer/', views.footer, name="footer"),
    path('menu/', views.menu, name = "menu"),    
    path('menu_choice/', views.menu_choice, name = "menu_choices"),    
    path('reservations/', views.reservations, name = "reservations"),         
    path('user_navbar/', views.user_navbar, name="user_navbar"),
    
    # CHATBOT
    path('chatbot/', views.chatbot, name="chatbot"),
    
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