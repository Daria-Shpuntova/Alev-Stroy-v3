from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import CalculationRequestForm, RequestForm
from unicodedata import category
from HelloDjango.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse


from .models import Type_Remont, Remont, Service, Kvartira, Category, Image, Price, Type_work, Surface, CalculationRequest

class BaseFormView(View):
    calc_form_class = CalculationRequestForm
    request_form_class = RequestForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context

    def send_email(self, template_name, context, subject):
        try:
            html_content = render_to_string(template_name, context)
            email = EmailMessage(subject, html_content, DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            email.content_subtype = 'html'
            email.send()
        except Exception as e:
            return HttpResponse(f'Ошибка при отправке письма: {str(e)}', content_type='text/html')

    def post(self, request, *args, **kwargs):
        print("View function called!")
        calc_form = self.calc_form_class(request.POST)
        request_form = self.request_form_class(request.POST)

        print("Calc form is valid:", calc_form.is_valid())
        print("Request form is valid:", request_form.is_valid())

        print('request_submit' in request.POST)
        print("Request POST:", request.POST)

        if 'calc_submit' in request.POST and calc_form.is_valid():
            try:
                print("Saving calc form...")
                calc_form.save()
                print("Calc form saved:", calc_form.instance.pk)
            except Exception as e:
                print("Error saving calc form:", e)
            self.send_email('Alev/send_mail.html', {'alls': calc_form.cleaned_data}, 'Запрос калькулятора')
            return JsonResponse({'status': 'success'})


        elif 'request_submit' in request.POST:
            request_form = RequestForm(request.POST)
            print("Request form is valid: 1")
            if request_form.is_valid():
                print("Request form is valid:")
                try:
                    print("Saving request form...")
                    request_form.save()
                    print("Request form saved:", request_form.instance.pk)
                except Exception as e:
                    print("Error saving request form:", e)
                self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
                return JsonResponse({'status': 'success'})

        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


#    def post(self, request, *args, **kwargs):
#        calc_form = self.calc_form_class(request.POST)
#        request_form = self.request_form_class(request.POST)
#
#        print("Calc form is valid:", calc_form.is_valid())
#        print("Request form is valid:", request_form.is_valid())
#
#        if 'calc_submit' in request.POST and calc_form.is_valid():
#            print("Saving calc form...")
#            calc_form.save()
#            self.send_email('Alev/send_mail.html', {'alls': calc_form.cleaned_data}, 'Запрос калькулятора')
#            return JsonResponse({'status': 'success'})
#
#        elif 'request_submit' in request.POST and request_form.is_valid():
#            print("Saving request form...")
#            request_form.save()
#            self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
#            return JsonResponse({'status': 'success'})
#
#        print(calc_form.errors)
#        print(request_form.errors)
#
#        return JsonResponse({'status': 'error', 'message': 'Invalid request'})


# def post(self, request, *args, **kwargs):
   #     if 'calc_submit' in request.POST:
   #         calc_form = self.calc_form_class(request.POST)
   #         if calc_form.is_valid():
   #             print("Calc form is valid!")
   #             calc_form.save()
   #             # Обработка формы калькулятора
   #             self.send_email('Alev/send_mail.html', {'alls': calc_form.cleaned_data}, 'Запрос калькулятора')
   #             return JsonResponse({'status': 'success'})
   #             return redirect('home')
   #         else:
   #             print("Calc form is not valid:", calc_form.errors)
#
   #     elif 'request_submit' in request.POST:
   #         request_form = self.request_form_class(request.POST)
   #         if request_form.is_valid():
   #             print("Request form is valid!")
   #             request_form.save()
   #             # Обработка формы калькулятора
   #             self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
   #             return JsonResponse({'status': 'success'})
   #             return redirect('home')
   #         else:
   #             print("Request form is not valid:", request_form.errors)
#

#   def post(self, request, *args, **kwargs):
#      calc_form = self.calc_form_class(request.POST)
#      request_form = self.request_form_class(request.POST)


#      if 'calc_submit' in request.POST and calc_form.is_valid():
#          # Обработка формы калькулятора
#          calc_form.save()
#          print(35)
#          self.send_email('Alev/send_mail.html', {'alls': calc_form.cleaned_data}, 'Запрос калькулятора')
#          return JsonResponse({'status': 'success'})
#     #     return redirect('home')


#      elif 'request_submit' in request.POST and request_form.is_valid():
#          # Обработка формы обратного звонка
#          request_form.save()
#          print(25)
#          self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
#          return JsonResponse({'status': 'success'})
#        #  return redirect('home')

#      return JsonResponse({'status': 'error', 'message': 'Invalid request'})
 #      return self.render_to_response(self.get_context_data(calc_form=calc_form, request_form=request_form))
#
 #       else:
 #           print(request_form.errors, 'request_form.errors')
 #           print(calc_form.errors, 'calc_form.errors')


        #        if calc_form.is_valid() and request_form.is_valid():
#            print(22)
#            calc_form.save()
#            request_form.save()
#            self.send_email('Alev/send_mail.html',  {'alls':calc_form.cleaned_data}, 'Запрос калькулятора')
#            self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
#            print(calc_form.is_valid())
#            print(request_form.is_valid())
#            return redirect('home')
#
#

 #      if calc_form.is_valid():
 #          print(33)
 #          calc_form.save()
 #          self.send_email('Alev/send_mail.html',  {'alls':calc_form.cleaned_data}, 'Запрос калькулятора')
 # #         return redirect('home')

 #      if request_form.is_valid():
 #          request_form.save()
 #          print(22)
 #          self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
 #      return redirect('home')


 #       if calc_form.is_valid():
 #           calc_form.save()
 #           # Отправка письма после успешного сохранения calc_form
 #           self.send_email('Alev/send_mail.html',  {'alls':calc_form.cleaned_data}, 'Запрос калькулятора')
 #           return redirect('home')
#
 #       elif request_form.is_valid():
 #           request_form.save()
 #           self.send_email('Alev/send_mail2.html', {'call': request_form.cleaned_data}, 'Запрос перезвонить')
 #           return redirect('home')


    #           try:
#               html_content = render_to_string('Alev/send_mail.html',
#                                               {'alls':calc_form.cleaned_data})
#               sendMail=EmailMessage(
#                   f'Запрос калькулятора',
#                   html_content,
#                   DEFAULT_FROM_EMAIL,
#                   RECIPIENTS_EMAIL
#               )
#               sendMail.content_subtype = 'html'
#               sendMail.send()
#           except Exception as e:
#               return HttpResponse(e, content_type='text/html')


 #       elif request_form.is_valid():
 #           request_form.save()
 #           self.send_email('Alev/send_mail2.html',{'call': request_form.cleaned_data}, 'Запрос перезвонить')
 #           try:
 #               html_content = render_to_string('Alev/send_mail2.html',
 #                                               {'call': request_form.cleaned_data})
 #               sendMail = EmailMessage(
 #                   f'Запрос перезвонить',
 #                   html_content,
 #                   DEFAULT_FROM_EMAIL,
 #                   RECIPIENTS_EMAIL
 #               )
 #               sendMail.content_subtype = 'html'
 #               sendMail.send()
 #           except Exception as e:
 #               return HttpResponse(e, content_type='text/html')






class Home(ListView, BaseFormView):
    model = Category
    template_name = 'Alev/home.html'

    def get_success_url(self):
        return reverse('home')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Алев-Строй'
        context['category'] = Category.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['remonts'] = Remont.objects.all()
        context['kvartira'] = Kvartira.objects.all()

        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context

#class Home(ListView, FormMixin):
#    model = Category
#    template_name = 'Alev/home.html'
#    form_class = CalculationRequestForm
#
#    def post(self, request, *args, **kwargs):
#        form = self.get_form()
#        if form.is_valid():
#            self.room_type = form.cleaned_data['room_type']
#            self.repair_type = form.cleaned_data['repair_type']
#            self.room_count = form.cleaned_data['room_count']
#            self.area = form.cleaned_data['area']
#            self.design_project = form.cleaned_data['design_project']
#            self.name = form.cleaned_data['name']
#            self.phone = form.cleaned_data['phone']
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)
#
 #   def form_valid(self, form):
 #       self.object = form.save(commit=False)
 #       self.object.room_type = self.room_type
 #       self.object.repair_type = self.repair_type
 #       self.object.room_count = self.room_count
 #       self.object.area = self.area
 #       self.object.design_project = self.design_project
 #       self.object.name = self.name
 #       self.object.phone = self.phone
 #       self.object.save()
 #       return super().form_valid(form)
#
 #   def get_success_url(self):
 #       return reverse('home')
#
 #   def get_context_data(self, *, object_list=None, **kwargs):
 #       queryset = kwargs.pop('object_list', None)
 #       if queryset is None:
 #           self.object_list = self.model.objects.all()
 #       context = super(Home, self).get_context_data(**kwargs)
  #      context['title'] = 'Алев-Строй'
  #      context['category'] = Category.objects.all()
  #      context['type_remont'] = Type_Remont.objects.all()
  #      context['remonts'] = Remont.objects.all()
  #      context['kvartira'] = Kvartira.objects.all()
  #      return context


class Services(DetailView, BaseFormView):
    model = Category
    template_name = 'Alev/service.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Services, self).get_context_data(**kwargs)
        category = Category.objects.filter(slug=self.kwargs['slug']).first()
        context['category'] = category
        print(context['category'])
      #  if category.id
        print(category.id)
        servers = Service.objects.all()
        remonts = Remont.objects.all()
        context['remonts'] = remonts
        context['servers'] = servers

        context['category2'] = Category.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['remonts2'] = Remont.objects.all()
        context['kvartira'] = Kvartira.objects.all()
        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context

class Remonts(DetailView, BaseFormView):
    model = Category
    template_name = 'Alev/remont.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Remonts, self).get_context_data(**kwargs)
        category = Category.objects.filter(slug=self.kwargs['slug']).first()
        context['category'] = category
        print(context['category'])
        #  if category.id
        print(category.id)
  #      self.rem = list(Remont.objects.filter(category_id = category).filter(remont_slug = self.kwargs['slug']).values())
 #      self.rem = list(Remont.objects.filter(category_id=category).filter(slug=self.kwargs['remont_slug']).values())
 #      print(self.rem)
 #      print(11)
 #      print(Remont.objects.filter(category_id=category).filter(slug=self.kwargs['remont_slug']).values())
 #      print(Remont.objects.filter(category_id=category).filter(slug=self.kwargs['remont_slug']))
 #       print(Remont.objects.filter(remont_slug = self.kwargs['slug']))
 #      context['rem'] = self.rem
        context['category2'] = Category.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['remonts2'] = Remont.objects.all()
        context['kvartira'] = Kvartira.objects.all()

        context['remont'] = Remont.objects.filter(category_id=category).filter(slug=self.kwargs['remont_slug']).first()
        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context


class Image(ListView, BaseFormView):
    model = Image
    template_name = 'Alev/gallery.html'
    context_object_name = 'image'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Image, self).get_context_data(**kwargs)
        context['title'] = 'Алев-Строй'

        context['category2'] = Category.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['remonts2'] = Remont.objects.all()
        context['kvartira'] = Kvartira.objects.all()
        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context

class About(ListView, BaseFormView):
    model = Category
    template_name = 'Alev/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(About, self).get_context_data(**kwargs)
        context['title'] = 'О нас'

        context['category2'] = Category.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['remonts2'] = Remont.objects.all()
        context['kvartira'] = Kvartira.objects.all()
        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context

def about(request):
    return render(request, 'Alev/about.html')

class Price(ListView, BaseFormView):
    template_name = "Alev/price.html"
    model = Price
    context_object_name = 'priceList'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        context = super(Price, self).get_context_data(**kwargs)
        context['type'] = Type_work.objects.all()
        context['surface'] = Surface.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['title'] = 'Алев-Строй'
        context['category2'] = Category.objects.all()
        context['type_remont'] = Type_Remont.objects.all()
        context['remonts2'] = Remont.objects.all()
        context['kvartira'] = Kvartira.objects.all()
        context['calc_form_class'] = self.calc_form_class()
        context['request_form_class'] = self.request_form_class()
        return context


def page_not_found_view(request, exception):
    # Получение данных из моделей
    category2 = Category.objects.all()
    type_remont = Type_Remont.objects.all()
    remonts2 = Remont.objects.all()
    kvartira = Kvartira.objects.all()

    # Создание контекста для передачи в шаблон
    context = {
        'category2': category2,
        'type_remont': type_remont,
        'remonts2': remonts2,
        'kvartira': kvartira,
    }

    return render(request, 'Alev/404.html', context=context, status=404)