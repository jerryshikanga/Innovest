from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.RequestProfile.as_view(), name='profile_logged_in'),
    path('profile/<slug:username>/<int:pk>/', views.Profile.as_view(), name='profile_user_id'),
    path('update/<int:pk>/', views.ProfileEdit.as_view(), name='profile_update'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('deposit/visa/', views.depositVisa, name='deposit_visa'),
]
