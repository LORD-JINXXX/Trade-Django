from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('',views.inbox,name='inbox'),
    path('<int:con_pk>/',views.open,name='open'),
    path('inbox/<int:item_pk>/',views.new_conversation,name='new_conversation')
]
