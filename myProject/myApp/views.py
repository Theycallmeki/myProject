from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request,'myApp/home.html',context)

def contact(request):
    context={}

    return render(request, 'components/contact.html')
def main(request):
    context={}

    return render(request, 'myApp/main.html', context)

def create(request):
    context={}

    return render(request, 'myApp/create.html')

def navbar(request):
    context={}

    return render(request, 'components/navbar.html')

    



from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to a home page after registration
    else:
        form = RegistrationForm()
    return render(request, 'myApp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')  # Redirect to a home page after login
    else:
        form = LoginForm()
    return render(request, 'myApp/login.html', {'form': form})

def user_logout(request):
    logout(request)  # Log out the user
    return redirect('home') 



from django.shortcuts import render, redirect
from .forms import PortfolioForm, PortfolioElementForm
from .models import Portfolio

from django.shortcuts import render, redirect
from .forms import PortfolioForm  # Ensure PortfolioForm has an ImageField
from django.http import JsonResponse

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio_instance = form.save()  # Save the portfolio instance
            
            # Handle the creation of PortfolioElement if there are files
            media_files = request.FILES.getlist('media')  # Adjust the name as needed
            for media in media_files:
                Portfolio.objects.create(
                    portfolio=portfolio_instance,
                    media=media,
                    # Set other attributes as needed
                )

            return redirect('portfolio_list')  # Redirect after successful save
    else:
        form = PortfolioForm()

    return render(request, 'myApp/create_portfolio.html', {'form': form})

def edit_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, 'myApp/edit_portfolio.html', {'form': form})

def portfolio_list(request):
    portfolios = Portfolio.objects.all()  # Retrieve all Portfolio instances
    return render(request, 'myApp/portfolio_list.html', {'portfolios': portfolios})




from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

@csrf_exempt  # Remove in production and use CSRF tokens
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        return JsonResponse({'uploaded': True, 'url': file_url})
    return JsonResponse({'uploaded': False, 'error': 'File upload failed.'})
