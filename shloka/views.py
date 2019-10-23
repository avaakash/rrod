from django.shortcuts import render, redirect
from .forms import RapperForm, AudienceForm
# Create your views here


def home(request):
    return render(request, 'home.html')


def success(request):
    if not request.session.get('form-submitted', False):
        return redirect('home')
    else:
        return render(request, 'success.html')


def round_details(request):
    return render(request, 'round-details.html')


def rapper_registration(request):
    form = RapperForm()
    if request.method == 'POST':
        form = RapperForm(request.POST)
        if form.is_valid():
            request.session['form-submitted'] = True
            user = form.save()
            pk = user.pk
            return redirect(success)
    context = {
        'form': form,
    }
    return render(request, 'registration_form_rapper.html', context)


def audience_registration(request):
    form = AudienceForm()
    if request.method == 'POST':
        form = AudienceForm(request.POST)
        if form.is_valid():
            request.session['form-submitted'] = True
            user = form.save()
            pk = user.pk
            return redirect(success)
    context = {
        'form': form,
    }
    return render(request, 'registration_form_audience.html', context)


def error404(request, exception):
    return render(request, 'error404.html')

def error500(request):
    return render(request, 'error500.html')
