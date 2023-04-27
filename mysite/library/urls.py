from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('loginservices/', views.loginservices, name='loginservices'),
    path('camps/', views.camps, name='camps'),
    path('calendar/', views.calendar, name='calendar'),
    path('camps/<int:camp_id>', views.camp_detail, name='camp'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('profilis/', views.profilis, name='profilis'),
    path('reserve/', views.reserve_campsite, name='reserve-campsite'),
    path('myreservation/', views.reservation_list, name='my-reservation'),
    path('score/', views.score_view, name='score_view'),
    path('score_results/', views.score_results, name='score_results'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('success/<str:name>/<str:email>/<str:subject>/<str:message>/', views.success_view, name='success'),
    path('contacts/', views.view_contacts, name='view_contacts'),
   
    # --------------------
    path('childrencamps/', views.children_camp_list, name='childrencamps'),
    path('children-camps/<int:camp_id>/', views.children_camp_detail, name='children-camp-detail'),
    path('register_children/', views.register_children, name='register_children'),
    path('success_children_registration/', views.registration_success, name='registration_success'),
    path('list_of_registrations', views.registration_list, name='registration_list'),
    
    path('adultcamps/', views.adult_camp_list, name='adultcamps'),
    path('adult-camps/<int:camp_id>/', views.adult_camp_detail, name='adult-camp-detail'),
    path('adult_registration_list/', views.adult_registration_list, name='adult_registration_list'),
    path('register_adult/', views.register_adult, name='register_adult'),
    path('adult_registration_success/', views.adult_registration_success, name='adult_registration_success'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    
]