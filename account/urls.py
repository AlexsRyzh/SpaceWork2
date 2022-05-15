from django.urls import path
from account import views

urlpatterns = [
    #Auth
    path('login/', views.loginPage, name = "login"),
    path('register/', views.registerPage , name = "register"),
    path('logout/', views.logoutUser, name = 'logout'),

    #Main-work-field
    path('', views.mainPage, name = 'main'),
    path('add_work_field/',views.addWorkFieldPage, name = 'add_work_field'),
    path('edit_work_field/<int:pk>', views.editWorkFieldPage, name = 'edite_work_field'),
    path('delete_work_field/<int:pk>', views.deleteWorkFieldPage, name = 'delete_work_field'),

    #Main_active
    path('<int:pk>', views.main_activePage, name='main_active'),

    #Main-task-field
    path('<int:pk>/add_task_field/', views.addTaskFieldPage, name = 'add_task_field'),
    path('<int:pk_work_field>/edite_task_field/<int:pk_task_field>', views.editTaskFieldPage, name = 'edite_task_field'),
    path('<int:pk_work_field>/delete_task_field/<int:pk_task_field>', views.deleteTaskFieldPage, name = 'delete_task_field'),


    #Main_task
    path('<int:pk_work_field>/add_task/<int:pk_task_field>', views.addTaskPage, name = 'add_task'),
    path('<int:pk_work_field>/task_field/<int:pk_task_field>/edit_task/<int:pk_task>',views.editTaskPage, name = 'edit_task'),
    path('<int:pk_work_field>/task_field/<int:pk_task_field>/delete_task/<int:pk_task>', views.deleteTaskPage, name = 'delete_task')
]