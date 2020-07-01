from django.conf.urls import url 
from student import views 
 
urlpatterns = [ 
    url(r'^students/$', views.students_list),
    # url(r'^students/roll_no/(?P&lt;age&gt;[0-9]+)/$', views.students_search),
]