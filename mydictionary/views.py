from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

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
    success_url = reverse_lazy('words_list')




