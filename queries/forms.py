from django import forms
# from django.forms import ModelForm
from queries.models import QueryQuestion, QuerySolution

class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control rounded-pill p-4",
                'type': "text",
                'placeholder': "Query Title"
            }),
        label=False,
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-4",
                'type': "text",
                'placeholder': "Problem Statement",
                'rows':3
            }),
        label=False,
    )
    example = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-4",
                'type': "text",
                'placeholder': "Test Case Eg: Sum(3+2)->5",
                'rows':2
            }),
        label=False,
    )

    class Meta:
        model = QueryQuestion
        fields = ('title','catego','content','example')

        widgets = {
            'catego': forms.Select(attrs={'class': "form-control rounded-pill",'type': "text",'placeholder': "Categories"}),
          }

class SolutionForm(forms.ModelForm):
    class Meta:
        model = QuerySolution
        fields = ['solution']

        widgets = {
            'solution': forms.Textarea(attrs={'class': "form-control",'type': "text",'placeholder': "Problem Statement", 'rows':3}),
            }
