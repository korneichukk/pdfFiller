from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        max_length=100,
        required=True,
        initial="",
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        required=True,
        initial="",
    )


class NewClientForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    dob = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(
            attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            }
        ),
    )
    ssn = forms.CharField(label="SSN", max_length=11)
    phone = forms.CharField(label="Phone", max_length=15)
    email = forms.EmailField(label="Email")
    address = forms.CharField(label="Address", widget=forms.Textarea)
    city = forms.CharField(label="City", max_length=100)
    state = forms.CharField(label="State", max_length=100)
    zip_code = forms.CharField(label="Zip Code", max_length=10)

    company_name = forms.CharField(label="Company Name", max_length=100)
    company_address = forms.CharField(label="Company Address", widget=forms.Textarea)
    company_city = forms.CharField(label="Company City", max_length=100)
    company_state = forms.CharField(label="Company State", max_length=100)
    company_zip = forms.CharField(label="Company Zip Code", max_length=10)
    ein = forms.CharField(label="EIN", max_length=20)
    date_of_incorporation = forms.DateField(
        label="Date of Incorporation",
        widget=forms.DateInput(
            attrs={
                "class": "w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(NewClientForm, self).__init__(*args, **kwargs)
        # Add CSS classes to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                }
            )
