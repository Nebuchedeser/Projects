# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from supermarket_app.models import User


from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    # Define a custom password field that will be used to collect the user's password.
    # This field will be used instead of the default password field on the User model.
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        max_length=64,
        required=True,
        help_text="Enter a password that is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one number."
    )

    class Meta:
        # Set the model and fields for the form.
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "photo"]

    def __init__(self, *args, **kwargs):
        # Call the parent's __init__ method to initialize the form.
        super().__init__(*args, **kwargs)

        # Set the label and help text for each form field.
        self.fields["first_name"].label = "First Name"
        self.fields["first_name"].help_text = "Enter your first name."
        self.fields["last_name"].label = "Last Name"
        self.fields["last_name"].help_text = "Enter your last name."
        self.fields["username"].label = "Username"
        self.fields["username"].help_text = "Enter a unique username that will be used to log in to the application."
        self.fields["email"].label = "Email"
        self.fields["email"].help_text = "Enter your email address."
        self.fields["password"].label = "Password"
        self.fields["photo"].label = "Photo"
        self.fields["photo"].help_text = "Upload a photo of yourself. This photo will be displayed on your profile."

    # Customize the behavior of the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Login name"
        self.fields["email"].label = "Email address"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm password"


class UserProfileForm(forms.ModelForm):
    class Meta:
        # Set the model and fields for the form.
        model = User
        fields = ["first_name", "last_name", "email", "photo"]

    def __init__(self, *args, **kwargs):
        # Call the parent's __init__ method to initialize the form.
        super().__init__(*args, **kwargs)

        # Set the label and help text for each form field.
        self.fields["first_name"].label = "First Name"
        self.fields["first_name"].help_text = "Enter your first name."
        self.fields["last_name"].label = "Last Name"
        self.fields["last_name"].help_text = "Enter your last name."
        self.fields["email"].label = "Email"
        self.fields["email"].help_text = "Enter your email address."
        self.fields["photo"].label = "Photo"
        self.fields["photo"].help_text = "Upload a photo of yourself. This photo will be displayed on your profile."

