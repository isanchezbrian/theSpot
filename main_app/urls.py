from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
  # path('admin/', admin.site.urls),
  path('', views.home, name='home'),

  path('cities/', views.cities, name='cities'),
  path('cities/<int:city_id>/', views.city_index, name='city_index'),

  path('posts/', views.posts, name='posts'),
  path('posts/<int:post_id>/', views.post_index, name='post_index'),

  path('accounts/signup', views.signup, name='signup'),
  path('profile/<int:user_id>/', views.profile, name='profile'),
  path('accounts/', include('django.contrib.auth.urls')),
        # this line7 adds the following links for us to use 
            # accounts/login/ [name='login']
            # accounts/logout/ [name='logout']
            # accounts/password_change/ [name='password_change']
            # accounts/password_change/done/ [name='password_change_done']
            # accounts/password_reset/ [name='password_reset']
            # accounts/password_reset/done/ [name='password_reset_done']
            # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
            # accounts/reset/done/ [name='password_reset_complete']
]