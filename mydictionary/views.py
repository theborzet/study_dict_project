from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

from mydictionary.models import Word
from mydictionary.forms import WordCreateForm
from common.views import TitleMixin

class IndexView(TitleMixin, TemplateView):
    template_name = 'mydictionary/welcome.html'
    title = 'My dictionary'

class WordListView(TitleMixin, ListView):
    title = 'My dictionary - Словарь'
    template_name = 'mydictionary/dict.html'
    model = Word

class WordCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    title = 'My dictionary - Редактирование'
    template_name = 'mydictionary/create.html'
    form_class = WordCreateForm
    success_message = 'Слово добавлено!'
    success_url = reverse_lazy('index')


def add_file(request):
    response = HttpResponse(content_type='text/plan')
    response['Content-Disposition'] = 'attachment; filename="words.txt"'

    data = Word.objects.all()
    with open('data.txt', 'w') as file:
        for item in data:
            file.write(f"English: {item.english}, Translate: {item.translate}\n")

    with open('data.txt', 'r') as file:
        response.write(file.read())

    return response





