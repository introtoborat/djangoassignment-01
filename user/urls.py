from django.urls import path
from user.views import sign_up, sign_in, sign_out, activate_user, admin_dashboard,assign_role, group_list, create_group

urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-out/', sign_out, name='logout'),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin/<int:user_id>/assign-role/', assign_role, name='assign-role'),
    path('admin/group-list/', group_list, name='group-list'),
    path('admin/create-group/', create_group, name='create-group'),

]