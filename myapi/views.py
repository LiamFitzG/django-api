from django.http import HttpResponseRedirect

def redirect_home(request):
    return HttpResponseRedirect("users/")