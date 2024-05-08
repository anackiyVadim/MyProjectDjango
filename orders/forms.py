import telegram
from django import forms
from .models import Order, OrderUser


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

    async def send_message(self):
        bot_token = '6509764574:AAHh5VRUaka14LuoFav-DLmrNyADFp7K9N4'
        chat_id = -1002124719444
        # chat_id = -768487653
        bot = telegram.Bot(token=bot_token)
        message_text = f"""Имя: {self.cleaned_data['first_name']}
        Фамилия: {self.cleaned_data['last_name']}
        Почта: {self.cleaned_data['email']}
        Адрес: {self.cleaned_data['address']}
        Почтовый индекс: {self.cleaned_data['postal_code']}
        Город: {self.cleaned_data['city']}
        """
        await bot.send_message(chat_id=chat_id, text=message_text)

class OrderUserCreateForm(forms.ModelForm):
    class Meta:
        model = OrderUser
        fields = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['user'].initial = user

#     async def send_message_user(self):
#         bot_token = '6509764574:AAHh5VRUaka14LuoFav-DLmrNyADFp7K9N4'
#         chat_id = -1002124719444
#         # chat_id = -768487653
#         bot = telegram.Bot(token=bot_token)
#         message_text = f"""------------------
#         Пользователь: {self.cleaned_data['user']}
# ------------------"""
#         await bot.send_message_user(chat_id=chat_id, text=message_text)
