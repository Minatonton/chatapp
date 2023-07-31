from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls. static import static

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.signup_view, name='signup_view'),
    path('login', views.login_view, name='login_view'),
    path('friends', views.lists, name='friends'),
    path('talk_room/<int:CustomUser_id>/', views.talk_room, name='talk_room'),
    path('setting', views.setting, name='setting'),
    path('signup',views.UserCreateView.as_view(), name='signup_user'),
    path('rogin',views.User_Confirmation.as_view(), name='rogin'),
    path('logout',views.User_Logout.as_view(),name="logout"),
    path('passwordchange',views.User_PasswordChangeView.as_view(),name='passwordchange'),
    path('passwordchangedone',views.User_PasswordChangeViewDoneView.as_view(),name='passwordchangedone'),
    path('namechange',views.namechange,name='namechange'),
    path('namechangedone',views.namechangedone,name='namechangedone'),
    path('emailchange',views.emailchange,name='emailchange'),
    path('emailchangedone',views.emailchangedone,name='emailchangedone'),
    path('imgchange',views.imgchange,name='imgchange'),
    path('imgchangedone',views.imgchangedone,name='imgchangedone')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
