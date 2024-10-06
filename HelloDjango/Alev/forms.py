from cProfile import label

from django import forms
from .models import CalculationRequest, Request


class CalculationRequestForm(forms.ModelForm):
    room_type = forms.ChoiceField(choices=[
                ('Квартира', 'Квартира'),
                ('Отдельная комната', 'Отдельная комната'),
                ('Коттедж/Дом', 'Коттедж/Дом'),
                ('Коммерческое помещение', 'Коммерческое помещение')
            ], required=False,
        label = 'Тип недвижимости',
        widget=forms.Select(attrs={'class': 'formSSS'})
    )
    repair_type = forms.ChoiceField(choices=[('Черновой', 'Черновой'),
                ('Косметический', 'Косметический'),
                ('Капитальный', 'Капитальный'),
                ('Дизайнерский', 'Дизайнерский')], required=False,
        label='Тип ремонта',
        widget=forms.Select(attrs={'class': 'formSSS'})
    )
    room_count = forms.ChoiceField(choices=[('1-комната', '1 комната'),
                ('2-комната', '2 комната'),
                ('3-комната', '3 комната'),
                ('4-комната', '4 комната'),
                ('5-комната', '5 и более комнат')], required=False,
        label='Количество комнат', widget=forms.Select(attrs={'class': 'formSSS'})
    )
    area= forms.CharField(
        label='Площадь (м²)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'area'})
    )
    design_project = forms.CharField(
        label='Дизайн-проект',
        required=False,
        widget=forms.CheckboxInput()
    )
    name = forms.CharField(
        label='Ваше имя',
        required=False,
        widget=forms.TextInput(attrs={'class': 'name_phone name_text','placeholder': 'Введите ваше имя'})
    )
    phone = forms.CharField(
        label='Ваш телефон',
        required=False,
        widget=forms.TextInput(attrs={'class': 'name_phone phone_text','placeholder': 'Введите ваш телефон'})
    )

    class Meta:
        model = CalculationRequest
        fields = ['room_type', 'repair_type', 'room_count', 'area', 'design_project', 'name', 'phone']

#        widgets = {
#            'room_type': forms.Select(choices=[
#                ('Квартира', 'Квартира'),
#                ('Отдельная комната', 'Отдельная комната'),
#                ('Коттедж/Дом', 'Коттедж/Дом'),
#                ('Коммерческое помещение', 'Коммерческое помещение'),
#            ]),
#            'repair_type': forms.Select(choices=[
#                ('Черновой', 'Черновой'),
#                ('Косметический', 'Косметический'),
#                ('Капитальный', 'Капитальный'),
#                ('Дизайнерский', 'Дизайнерский'),
#            ]),
#            'room_count': forms.Select(choices=[
#                ('1-комната', '1 комната'),
#                ('2-комната', '2 комната'),
#                ('3-комната', '3 комната'),
#                ('4-комната', '4 комната'),
#                ('5-комната', '5 и более комнат'),
#            ]),
#
#            'Площадь': forms.NumberInput(attrs={'class':'area','placeholder': 'Введите площадь'}),
#            'Дизайн-проект': forms.CheckboxInput(),
#            'Имя': forms.TextInput(attrs={'class': 'name_phone','placeholder': 'Введите ваше имя'}),
#            'Телефон': forms.TextInput(attrs={'class': 'name_phone','placeholder': 'Введите ваш телефон@'}),
#        }
#        labels = {
#            'room_type': 'Тип недвижимости',
#            'repair_type': 'Тип ремонта',
#            'room_count': 'Количество комнат',
#            'area': 'Площадь (м²)',
#            'design_project': 'Нужен ли дизайн-проект?',
#            'name': 'Ваше имя',
#            'phone': 'Ваш телефон',
#        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name_text','placeholder': 'Введите ваше имя'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите ваш телефон'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Введите ваш email'}),
            'message': forms.TextInput(attrs={'placeholder': 'Введите сообщение'})
        }
        labels = {
            'name': 'Ваше имя',
            'phone': 'Ваш телефон',
            'email':'Ваш email',
            'message': 'Текст сообщения'
        }