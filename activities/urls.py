from django.urls import path
from activities.views import view_category, create_event,event_list,event_detail,create_category,create_participant,update_event, dashboard_event_list,search,delete_event, view_participants,view_events,dashboard


urlpatterns = [
  path('dashboard/', dashboard),
  path('view-category/', view_category, name= "view-category"), 
  path('view-participants/', view_participants, name= "view-participants"), 
  path('view-events/', view_events, name= "view-events"), 
  path('create-event/', create_event,name="create-event"),
  path("update/<int:event_id>/", update_event, name="update-event"),
  path("delete/<int:event_id>/", delete_event, name="delete-event"),
  path('create-category/', create_category,name="create-category"),
  path('create-participant/', create_participant,name="create-participant"),
  path('event_list/',event_list,name="event_list"),
  path('event/<int:event_id>/', event_detail, name='event_detail'),
  path('dashboard-event-list/', dashboard_event_list, name='dashboard-event-list'),
  path('search/', search, name='search'),
  
]
