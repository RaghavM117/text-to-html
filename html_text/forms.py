from django import forms
from ckeditor.widgets import CKEditorWidget

class CForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget(), label='')
    