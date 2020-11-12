
from django.urls import path
from Restapp.views import Userview,Books,BookDetail,LoginView,LogoutView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('test',Userview.as_view()),
    path('books',Books.as_view()),
    path('books/<int:pk>',BookDetail.as_view()),
    path('loginrest',LoginView.as_view()),
    path('logoutrest',LogoutView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)