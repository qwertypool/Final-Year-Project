from django.urls import path
from work import views

urlpatterns = [
    path('', views.work_view, name='work'),
    path('lostcard/', views.lost_view, name='lostcard'),
    path('foundcard/', views.found_view, name='foundcard'),
    # path('notifications/', views.notification_view, name='notification'),
    path('recorddelete/<int:uid>', views.recorddelete_view, name='deleterecord'),
]