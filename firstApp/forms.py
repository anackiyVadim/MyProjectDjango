from django import forms
import telegram
from django.contrib.auth.models import User

from .models import FeaturedProducts, Product, Shipping, Payment, Comment


# FeedbackForm ========================================================
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=12)
    message = forms.CharField(widget=forms.Textarea)

    async def send_message(self):
        bot_token = '6509764574:AAHh5VRUaka14LuoFav-DLmrNyADFp7K9N4'
        chat_id = -1002124719444
        # chat_id = -768487653
        bot = telegram.Bot(token=bot_token)
        message_text = f"Name: {self.cleaned_data['name']}\nPhone: {self.cleaned_data['phone']}\nMessage: {self.cleaned_data['message']}"
        await bot.send_message(chat_id=chat_id, text=message_text)

# FeedbackForm ========================================================

# RegisterForm ========================================================
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'reg__input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'phone')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


# RegisterForm ========================================================


# FavoriteForm=========================================================
class FavoriteForm(forms.ModelForm):
    # featuredProducts_User = forms
    class Meta:
        model = FeaturedProducts
        fields = ['featuredProducts_User', 'featuredProducts_Product']
        widgets = {
            'featuredProducts_User': forms.HiddenInput(),
            'featuredProducts_Product': forms.HiddenInput(),
        }


# FavoriteForm=========================================================



# upload user form ====================================================
class CombinedForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    address = forms.CharField()
    preferredPaymentMethod = forms.ModelChoiceField(queryset=Payment.objects.all(), required=False)
    phone = forms.IntegerField()
    preferredShippingMethod = forms.ModelChoiceField(queryset=Shipping.objects.all(), required=False)
    city = forms.CharField()
    avatar = forms.ImageField()
    mail_index = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(CombinedForm, self).__init__(*args, **kwargs)
        self.fields['address'].initial = self.instance.profile.address
        self.fields['preferredPaymentMethod'].initial = self.instance.profile.preferredPaymentMethod
        self.fields['phone'].initial = self.instance.profile.phone
        self.fields['preferredShippingMethod'].initial = self.instance.profile.preferredShippingMethod
        self.fields['city'].initial = self.instance.profile.city
        self.fields['avatar'].initial = self.instance.profile.avatar
        self.fields['mail_index'].initial = self.instance.profile.mail_index

    def save(self, commit=True):
        user = super(CombinedForm, self).save(commit=False)
        profile = user.profile
        profile.address = self.cleaned_data['address']
        profile.preferredPaymentMethod = self.cleaned_data['preferredPaymentMethod']
        profile.phone = self.cleaned_data['phone']
        profile.preferredShippingMethod = self.cleaned_data['preferredShippingMethod']
        profile.city = self.cleaned_data['city']
        profile.avatar = self.cleaned_data['avatar']
        profile.mail_index = self.cleaned_data['mail_index']
        if commit:
            user.save()
            profile.save()
        return user


# upload user form ====================================================


# upload password form ================================================
class Re_Password(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_NewPassword = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password_NewPassword2 = forms.CharField(label='Repeat New password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('password', 'password_NewPassword', 'password_NewPassword2')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password_NewPassword'] != cd['password_NewPassword2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password_NewPassword2']

    def save(self, user):
        user_to_update = User.objects.get(id=user.id)
        user_to_update.set_password(self.cleaned_data['password_NewPassword2'])
        user_to_update.save()
        return user_to_update
# upload password form ================================================

# CommentForm =========================================================
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'published_date', 'product')
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
# CommentForm =========================================================
