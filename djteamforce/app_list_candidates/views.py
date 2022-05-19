from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.views.generic.edit import FormView
from .forms import CreationForm, SkillsForm
from .models import Profile, Skills


# Create your views here.
class RegisterView(FormView):
    form_class = CreationForm
    success_url = "/"
    template_name = "user/register.html"

    def form_valid(self, form):
        user = form.save()
        first_name = form.cleaned_data.get('first_name')
        middle_name = form.cleaned_data.get('middle_name')
        last_name = form.cleaned_data.get('last_name')
        skills = form.cleaned_data.get('skills')
        language = form.cleaned_data.get('language')
        hobbies = form.cleaned_data.get('hobbies')
        Profile.objects.create(
            user=user,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            skills=skills,
            language=language,
            hobbies=hobbies,
        )
        Skills.objects.create(skill=skills)
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)


class AnotherLoginView(LoginView):
    template_name = 'user/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'user/logout.html'


class MainView(View):
    template_name = 'main.html'

    def get(self, request):
        profiles_obj = Profile.objects.all()
        profiles = []
        for profile in profiles_obj:
            profiles.append(profile)
        return render(request, 'main.html', {'profiles': profiles})


class PersonalAccountView(View):
    template_name = 'users/personal_account.html'

    def get(self, request):
        profiles_obj = Profile.objects.all()
        profiles = []
        for profile in profiles_obj:
            profiles.append(profile)
        return render(request, 'user/personal_account.html', {'profiles': profiles})


class AddSkillsView(View):
    def get(self, request):
        skill_form = SkillsForm()
        skills_obj = Skills.objects.all()
        skills = []
        if len(skills_obj) > 1:
            for skill in skills_obj:
                if skill.pk == 1:
                    skills.append(skill.skill)
                else:
                    skills.append(f", {skill.skill}")
        return render(request, 'user/add_skill.html', context={'skill_form': skill_form, 'skills': skills})

    def post(self, request):
        skill_form = SkillsForm(request.POST)
        all_skills = Skills.objects.all()
        list_skill = ''
        if skill_form.is_valid():
            user = Profile.objects.get(user=request.user)
            if len(user.skills) > 0:
                user.skills = f"{user.skills}, {skill_form.cleaned_data['skills']}"
            else:
                user.skills = f"{user.skills} {skill_form.cleaned_data['skills']}"
            for skill in all_skills:
                list_skill += skill.skill
            if skill_form.cleaned_data['skills'] not in list_skill:
                Skills.objects.create(skill=skill_form.cleaned_data['skills'])
            user.save()
            return HttpResponseRedirect('/user/personal-account/')
        return render(request, 'user/add_news.html', context={'skill_form': skill_form})


class DeleteSkillView(View):

    def get(self, request):
        skill_form = SkillsForm()
        user = Profile.objects.get(user=request.user)
        return render(request, 'user/delete_skill.html', context={'skill_form': skill_form, 'skills_user': user.skills})

    def post(self, request):
        skill_form = SkillsForm(request.POST)
        if skill_form.is_valid():
            user = Profile.objects.get(user=request.user)
            user.skills = user.skills.replace(' ', '').split(',')
            user.skills.remove(skill_form.cleaned_data['skills'])
            user.skills = ' '.join(user.skills).replace(' ', ', ')
            user.save()
            return HttpResponseRedirect('/user/personal-account/')
        return render(request, 'user/delete_skill.html', context={'skill_form': skill_form})
