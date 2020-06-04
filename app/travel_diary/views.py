from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from .models import Diary
from .forms import DiaryForm

class DiaryListView(LoginRequiredMixin, ListView):

    model = Diary
    paginate_by = 20
    template_name = "travel_diary/index.html"

class DiaryDetailView(LoginRequiredMixin, DetailView):

    model = Diary

class DiaryCreateView(LoginRequiredMixin, CreateView):

    model = Diary
    form_class = DiaryForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
