from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('userHome', regestraionUser, name="userRegestration"),
    # path('userLogin<int:num_ques>', loginUser.as_view(), name="UserLogin"),
    path('OTP', OtpUser, name="Otp"),
    path('subscription', Subscription, name="Subscription"),
    # path('chnageQuesStra/<int:id>',chnageQuesStra,name="chnageQuesStra"),
    # path('chnageQuesStra',chnageQuesStra,name="chnageQuesStra"),
    # path("saveans",saveans,name='saveans'),
    path("question",question,name="questions")

]+static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
