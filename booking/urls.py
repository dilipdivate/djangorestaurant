from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter

urlpatterns = [
    path('', views.BookingList.as_view(), name="bookings"),
    path('<int:pk>/', views.BookingDetail.as_view(), name="bookingitem"),
]


urlpatterns = format_suffix_patterns(urlpatterns)


# router = SimpleRouter()
# router.register("subscribers", SubscriberViewSet)

# urlpatterns = router.urls