import django.conf.urls
from django.urls import path, include
from django.urls import path

from allocation.views import count_cur_sim, getresponse, testApi

# urlpatterns =[
# django.conf.urls.url(r'^count_cur_sim', count_cur_sim, name="To get count of rows.") ,
# ]

urlpatterns =[
    path(r'count_cur_sim', count_cur_sim, name="To get count of rows."),
    path('getresponse', getresponse, name="To get response."),
    path('testApi', testApi, name="test api.")
]
