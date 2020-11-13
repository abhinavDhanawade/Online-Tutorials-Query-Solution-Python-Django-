from django import forms
from services.models import ContactUs ,Purchase, Tutorial, Userprofile
from django.contrib.auth.models import User

class TutorialForm(forms.ModelForm):
    
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control rounded-pill p-4 my-4",
                'type': "text",
                'placeholder': "Tutorial Title"
            }),
        label=False,
    )

    desc = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-4",
                'type': "text",
                'placeholder': "Tutorial Description",
                'rows':2
            }),
        label=False,
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': "form-control p-4 rounded-pill",
                'placeholder': "Price"
            }),
        label=False,
    )
    imagefile = forms.ImageField(
        label=('Tutorial Card Image'),
    )
    class Meta:
        model = Tutorial
        fields = ('title','catego','desc','imagefile','videofile','price')

        widgets = {
            'catego': forms.Select(attrs={'class': "form-control rounded-pill",'type': "text",'placeholder': "Categories"}),
          }

class ContactUsForm(forms.ModelForm):

    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control rounded-pill p-4 my-4",
                'type': "text",
                'placeholder': "Full Name"
            }),
        label=False,
    )

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control rounded-pill p-4 my-4",
            'type': "text",
            'placeholder': "Phone Number"
        }),
        label=False,
    )
    email_ad = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': "form-control rounded-pill p-4 my-4",
            'type': "email",
            'placeholder': "Email"
        }),
        label=False,
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-4",
                'type': "text",
                'placeholder': "Message",
                'rows':2
            }),
        label=False,
    )

    class Meta:
        model = ContactUs
        fields = '__all__'


    
class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control rounded-pill p-4 my-4",
            'type': "text",
            'placeholder': "First Name"
        }))
    last_name = forms.CharField(max_length=30, label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control rounded-pill p-4 my-4",
            'type': "text",
            'placeholder': "Last Name"
        }))
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name','Username', 'email', 'password1', 'password2')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class PurchaseForm(forms.ModelForm):
    fullname = forms.CharField(max_length=30, label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control rounded-pill p-4 my-4",
            'type': "text",
            'placeholder': "Fullname"
        }))
    class Meta:
        model = Purchase
        fields = ('fullname',)





class UserprofileForm(forms.ModelForm):
    profession = forms.CharField(label=False,widget=forms.TextInput(
        attrs={
            'class': "form-control rounded-pill p-4 my-4",
            'type': "text",
            'placeholder': "Profession"
        }))
    image = forms.ImageField(
        label=('Profile Picture'),
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': "form-control p-4",
                'type': "text",
                'placeholder': "Bio",
                'rows':2
            }),
        label=False,
    )

    class Meta:
        model = Userprofile
        fields = ('profession','image','bio')