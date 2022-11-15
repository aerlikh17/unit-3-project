from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('clientExercise/<int:user_id>', views.loglist, name='log'),
  path('clientExercise/add/<int:user_id>/<int:exercise_ids>', views.logAdd, name='logAdd'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]