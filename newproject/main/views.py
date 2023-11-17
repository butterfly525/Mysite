from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import StyleCard
from .forms import StyleCardForm, SignupForm
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import views as auth_views,logout
from django.contrib.auth.decorators import login_required



def index(request):
    style_card = StyleCard.objects.all()
    # for card in style_card:
    # card.codeCSS = card.codeCSS.replace('\r', ' ').replace('\n', ' ')
    # card.codeHTML = card.codeHTML.replace('\r', ' ').replace('\n', ' ')
    return render(request, 'main/index.html', {'styles': style_card})


def index_edit(request):
    style_card = StyleCard.objects.all()
    for card in style_card:
        card.codeCSS = card.codeCSS.replace('\r', ' ').replace('\n', ' ')
        card.codeHTML = card.codeHTML.replace('\r', ' ').replace('\n', ' ')
    return render(request, 'main/edit_form.html', {'styles': style_card})


def nav_aside_item(request):
    style_card = StyleCard.values('id', 'nameStyle')
    return render(request, 'main/layout.html', {'styles': style_card})


def view_form(request):
    if request.method == 'POST':
        form = StyleCardForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StyleCardForm()
    return render(request, 'main/index.html', {'form': form})

def save_data(request, id):
    if not request.user.is_authenticated:
        print("Не авторизован")
        return redirect('login')
    if request.method == 'POST':
        data = request.POST
        instance = get_object_or_404(StyleCard, id=id)
        instance.codeHTML = data.get('codeHTML')
        instance.codeCSS = data.get('codeCSS')
        instance.codeJS = data.get('codeJS')
        instance.save()
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

   

class LoginView(auth_views.LoginView):
    template_name = 'main/login.html'


def logout_view(request):
    logout(request)
    return redirect('home')