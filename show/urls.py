from show import views
from django.conf.urls import url
from show.views import enter_list, UserRetrieveUpdateAPIView
urlpatterns = [
    url(r'^update/?$', UserRetrieveUpdateAPIView.as_view()),    
    url(r'^enter/$', 'enter_list', name='enter_list'),
]