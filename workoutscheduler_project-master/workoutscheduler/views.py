from django.views.generic.base import RedirectView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class HomeView(RedirectView):
    pattern_name = 'todolist:today_workout_list'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:  # should check via request, not like User.is_authenticated
            return super(HomeView, self).get_redirect_url(*args, **kwargs)
        else:
            return 'accounts/login' # Homeview Redirects to given url, do not use redirect()


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = "/"  # redirect to main page after creation (This goes to login page because user is not logged in)

