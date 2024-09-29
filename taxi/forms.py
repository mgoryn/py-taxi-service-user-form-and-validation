from django import forms
from django.contrib.auth.forms import UserCreationForm
from taxi.models import Driver, Car, validate_license


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Driver
        fields = (
            UserCreationForm.Meta.fields + (
                "username",
                "first_name",
                "last_name",
                "license_number",
            )
        )

    def clean_licence_number(self):
        license_number = self.cleaned_data.get("license_number")
        validate_license(license_number)
        return license_number


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ["license_number"]

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        validate_license(license_number)
        return license_number


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["model", "manufacturer", "drivers"]
        widgets = {
            "drivers": forms.CheckboxSelectMultiple(),
        }
