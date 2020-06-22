from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/create', views.addPage), #create page
    path('shows/new', views.Create_Show), #process the page
    path('shows/<int:show_Val>', views.letShow), 
    path('shows/<int:my_Val>/edit', views.EditShow), #make edits
    path('shows/<int:my_Val>/edits/process', views.letEdit), #process the edits
    path('shows/<int:got_Val>/delete/', views.deleteShow)

]