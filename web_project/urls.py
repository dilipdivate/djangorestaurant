"""
URL configuration for web_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from rest_framework_jwt.views import obtain_jwt_token
# register viewset with router
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('api.urls')),
    path('menus/', include('menu.urls')),
    path('users/', include('user.urls')),
    path('orders/', include('order.urls')),
    path('bookings/', include('booking.urls')),
    path('recipes/', include('recipe.urls')),
    path('ingredients/', include('ingredient.urls')),
    path('tabletop/', include('table_top.urls')),
    path('item/', include('item.urls')),
    path('itemChef/', include('item_chef.urls')),

    path('transactions/', include('transaction.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', obtain_auth_token),
    path('admin/', admin.site.urls),

    # path('jwt-auth/', obtain_jwt_token),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
