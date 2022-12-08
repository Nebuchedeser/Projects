from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Item, Category, Subcategory, User
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth import login
from django.views.generic import FormView
from .views import RegisterView, ProfileUpdateView
from .models import Category, Item
from .models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import UserProfileForm


class RegisterView(FormView):
    # Set the form class for the view.
    form_class = UserRegistrationForm

    # Set the template for the view.
    template_name = "register.html"

    def form_valid(self, form):
        # If the form is valid, create a new user with the form data and log in the user.
        user = form.save()
        login(self.request, user)

        # Redirect the user to the home page.
        return redirect("home")

    def form_invalid(self, form):
        # If the form is invalid, render the form again with the form errors.
        return self.render_to_response(self.get_context_data(form=form))

class ProfileUpdateView(FormView):
    # Set the form class for the view.
    form_class = UserProfileForm

    # Set the template for the view.
    template_name = "profile_update.html"

    def form_valid(self, form):
        # If the form is valid, update the user's profile with the form data.
        user = self.request.user
        user.first_name = form.cleaned_data["first_name"]
        user.last_name = form.cleaned_data["last_name"]
        user.email = form.cleaned_data["email"]
        user.photo = form.cleaned_data["photo"]
        user.save()

        # Redirect the user to their profile page.
        return redirect("profile")

    def form_invalid(self, form):
        # If the form is invalid, render the form again with the form errors.
        return self.render_to_response(self.get_context_data(form=form))


def home(request):
    # Get a list of categories.
    categories = Category.objects.all()

    # Get a list of items.
    items = Item.objects.filter(public=True)

    # Render the home page with the categories and items.
    return render(request, "home.html", {"categories": categories, "items": items})

def item_list(request):
  items = get_item_list(request)
  return render(request, 'item_list.html', {'items': items})

def item_detail(request, id):
  item = Item.objects.get(id=id)
  return render(request, 'item_detail.html', {'item': item})

def category_list(request):
    # Get a list of categories.
    categories = Category.objects.all()

    # Render the category list page with the categories.
    return render(request, "category_list.html", {"categories": categories})

def subcategory_list(request, category_id):
    # Get the category with the given ID.
    category = get_object_or_404(Category, pk=category_id)

    # Get a list of subcategories for the category.
    subcategories = Subcategory.objects.filter(category=category)

    # Render the subcategory list page with the category and subcategories.
    return render(request, "subcategory_list.html", {"category": category, "subcategories": subcategories})

# Define the register view using the RegisterView class.
def register(request):
    # If the request method is GET, display the registration form.
    if request.method == "GET":
        return RegisterView.as_view()(request)

    # If the request method is POST, handle the form submission.
    elif request.method == "POST":
        # Create a new UserRegistrationForm instance with the form data.
        form = UserRegistrationForm(request.POST)

        # Validate the form.
        if form.is_valid():
            # If the form is valid, create a new user with the form data and log in the user.
            user = form.save()
            login(request, user)

            # Redirect the user to the home page.
            return redirect("home")

        else:
            # If the form is invalid, render the form again with the form errors.
            return RegisterView.as_view()(request, form=form)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      photo = form.cleaned_data['photo']
      User.objects.create_user(first_name, last_name, username, email, password, photo)
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    # Get the user's profile information.
    user = request.user

    # Render the profile page with the user's profile information.
    return render(request, "profile.html", {"user": user})

@login_required
def profile_update(request):
    # Get the user's profile.
    user = request.user

    # Check if the user is authenticated.
    if not user.is_authenticated:
        # Redirect the user to the login page.
        return redirect(reverse('login'))

    # Check if the user has submitted the form.
    if request.method == 'POST':
        # Bind the form data to the form instance.
        form = UserProfileForm(request.POST, request.FILES, instance=user)

        # Check if the form is valid.
        if form.is_valid():
            # Save the form data to the database.
            form.save()

            # Redirect the user to the profile page.
            return redirect(reverse('profile'))
    else:
        # Initialize the form with the user's profile data.
        form = UserProfileForm(instance=user)

    # Render the profile update page with the form.
    return render(request, "profile_update.html", {"form": form})

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
  return render(request, 'login.html')

def logout_view(request):
  logout(request)
  return redirect('home')

def get_item_list(request):
  items = Item.objects.filter(public=True)
  if 'search' in request.GET:
    search_query = request.GET['search']
    items = items.filter(name__icontains=search_query)
  if 'category' in request.GET:
    category_id = request.GET['category']
    items = items.filter(category=category_id)
  if 'subcategory' in request.GET:
    subcategory_id = request.GET['subcategory']
    items = items.filter(subcategory=subcategory_id)
  return items

def get_item_list(query=None, category=None, subcategory=None):
  items = Item.objects.all()

  if query:
    items = items.filter(name__icontains=query)
  if category:
    items = items.filter(category=category)
  if subcategory:
    items = items.filter(subcategory=subcategory)

  return items.order_by('name')


def get_category_list():
  return Category.objects.order_by('name')


def get_subcategory_list(category_id):
  subcategories = Subcategory.objects.filter(category=category_id)
  return subcategories

  

