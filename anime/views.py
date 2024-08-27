from django.shortcuts import render, redirect
from .models import AnimeCharacter
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

user = get_user_model()

def home(request): 
    return render(request, "index.html")


def character(request, id):
    character = AnimeCharacter.objects.get(id=id)
    return render(request, "character.html", {"character": character})


def signup(request):

    """

        CHECK IF THE FORM WAS SENT WITH THE POST METHOD AND 
        CREATE A NEW ISTANCE OF THE SignUpForm() object PASSING THE DATA FROM THE REQUEST 
        AND SAVE IT INTO THE DATABASE 

    """

    if request.user.is_authenticated == True:
        request.session["Authenticated_Message"] = "You are already authenticated! There's no need to signin again 😁"
        return redirect("index")


    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)

            login(request, user)
            request.session['Authenticated_Message'] = 'Your account has been created successfully!'
            return redirect('index')
        else:
            print("Form is not valid")
            print(form.errors)

    else:
        form = SignUpForm()

    
  
    return render(
        request, 
        "PollsApp/signup/signup.html",

        {"form": form})



def login_func(request):
    request.session['errorlogin'] = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():


            authenticated_user = authenticate(
            email = form.cleaned_data.get("email"), 
            password = form.cleaned_data.get("password")
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return render(request, 'PollsApp/home/index.html')
            else:
                request.session['errorlogin'] = "There is no matching account with this credentials!"
    else:
        form = LoginForm()

    return render(
        request, 
        "PollsApp/Login/login.html",

        { 
            "form": form,

    
        }
        )


def logout_view(request):

    logout(request)
    request.session['logout-message'] = "You have been logged out!"
    return render(request, 'PollsApp/home/index.html')
    

@login_required
def user_profile(request): 
    
    return render(request, 'PollsApp/user/user_profile.html')
    
