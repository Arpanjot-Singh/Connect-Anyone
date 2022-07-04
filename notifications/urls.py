from django.urls import path
from notifications.views import ShowNotifications,DeleteNotification

urlpatterns=[
    path('',ShowNotifications,name='show-notification'),
    path('<noti_id>/delete',DeleteNotification,name='delete-notification')
]