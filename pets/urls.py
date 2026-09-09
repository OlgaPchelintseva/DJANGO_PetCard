from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    path('pet/<slug:slug>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('pet/create/', views.PetCreateView.as_view(), name='pet_create'),
    path('pet/<clug:slug>/update/', views.PetUpdateView.as_view, name='pet_update'),
    path('vet-clinics/', views.VetClinicDirectoryView.as_view(), name='vet_clinics'),
]