from django import forms
from .models import Book

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:
            raise forms.ValidationError("Invalid input detected!")
        return title

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if "<script>" in summary:
            raise forms.ValidationError("Invalid input detected!")
        return summary


# ExampleForm for demonstration purposes
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name cannot contain numbers.")
        return name

