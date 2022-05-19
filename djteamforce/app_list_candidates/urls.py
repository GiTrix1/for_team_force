from django.urls import path
from .views import (MainView, AnotherLoginView, AnotherLogoutView,
                    PersonalAccountView, RegisterView, AddSkillsView,
                    DeleteSkillView)


urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('user/register/', RegisterView.as_view(), name="register"),
    path('user/login/', AnotherLoginView.as_view(), name='login'),
    path('user/logout/', AnotherLogoutView.as_view(), name='logout'),
    path('user/personal-account/', PersonalAccountView.as_view(), name='personal_account'),
    path('user/add-skills/', AddSkillsView.as_view(), name='add_skills'),
    path('user/delete-skills/', DeleteSkillView.as_view(), name='delete_skills'),
]
