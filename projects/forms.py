from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        #fields = '__all__'
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tags']

        # customizeable styling
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input input--text', 'id': 'formInput#text', 'type': 'text', 'name': 'text', 'placeholder': 'Enter text'}) #add css class "input" to this field
