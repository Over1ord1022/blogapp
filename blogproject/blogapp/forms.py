from django import forms
from .models import UserPreferences, Category

class PreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['theme', 'language', 'preferred_categories']
        widgets = {
            'preferred_categories': forms.CheckboxSelectMultiple,
            'theme': forms.RadioSelect(choices=[
                ('light', 'Светлая'),
                ('dark', 'Темная'),
                ('auto', 'Авто')
            ]),
            'language': forms.RadioSelect(choices=[
                ('ru', 'Русский'),
                ('en', 'English')
            ])
        }