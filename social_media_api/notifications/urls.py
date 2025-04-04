from django.urls import path
from .views import NotificationListView, MarkNotificationsAsReadView

urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('notifications/read/', MarkNotificationsAsReadView.as_view(), name='read_notifications'),
]