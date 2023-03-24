from django.urls import path
from . import views


urlpatterns = [
 path('set/',views.setsession),
 path('get/',views.getsession),
 path('delete/',views.deletesession),

#  test cookie url

path('tset/',views.settestcookie),
path('ttest/',views.testcookieworked),
path('tdelete/',views.deletetestcookie),

]
