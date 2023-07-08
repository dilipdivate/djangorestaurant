from django.urls import path, include
from .views import UserList, UserCreate, LoginView, LoginView2, UserUsList
from rest_framework.authtoken import views

urlpatterns = [
    # path('login/', views.loginUser, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerUser, name="register"),

    # path('', views.profiles, name="profiles"),
    path('', UserCreate.as_view(), name="user_create"),
    # path('login/', views.obtain_auth_token, name="login"),
    path('login/', LoginView2.as_view(), name="login"),
    path('logus/', UserUsList.as_view(), name="login"),

    # path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    # path('account/', views.userAccount, name="account"),

    # path('edit-account/', views.editAccount, name="edit-account"),

    # path('create-skill/', views.createSkill, name="create-skill"),
    # path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    # path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),


    # path('inbox/', views.inbox, name="inbox"),
    # path('message/<str:pk>/', views.viewMessage, name="message"),
    # path('create-message/<str:pk>/', views.createMessage, name="create-message"),



]

# urlpatterns = [
#     path('', views.Transactions.as_view(), name="transactions"),
#     path('/<str:pk>/', views.Transactions.as_view(), name="transactionitem"),
# ]
