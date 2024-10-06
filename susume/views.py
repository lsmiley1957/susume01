from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class SusumeListView(generic.ListView):
    model = models.Susume
    form_class = forms.SusumeForm


class SusumeCreateView(generic.CreateView):
    model = models.Susume
    form_class = forms.SusumeForm


class SusumeDetailView(generic.DetailView):
    model = models.Susume
    form_class = forms.SusumeForm


class SusumeUpdateView(generic.UpdateView):
    model = models.Susume
    form_class = forms.SusumeForm
    pk_url_kwarg = "pk"


class SusumeDeleteView(generic.DeleteView):
    model = models.Susume
    success_url = reverse_lazy("susume_Susume_list")


class SusupmtListView(generic.ListView):
    model = models.Susupmt
    form_class = forms.SusupmtForm


class SusupmtCreateView(generic.CreateView):
    model = models.Susupmt
    form_class = forms.SusupmtForm


class SusupmtDetailView(generic.DetailView):
    model = models.Susupmt
    form_class = forms.SusupmtForm


class SusupmtUpdateView(generic.UpdateView):
    model = models.Susupmt
    form_class = forms.SusupmtForm
    pk_url_kwarg = "pk"


class SusupmtDeleteView(generic.DeleteView):
    model = models.Susupmt
    success_url = reverse_lazy("susume_Susupmt_list")


class SusutypeListView(generic.ListView):
    model = models.Susutype
    form_class = forms.SusutypeForm


class SusutypeCreateView(generic.CreateView):
    model = models.Susutype
    form_class = forms.SusutypeForm


class SusutypeDetailView(generic.DetailView):
    model = models.Susutype
    form_class = forms.SusutypeForm


class SusutypeUpdateView(generic.UpdateView):
    model = models.Susutype
    form_class = forms.SusutypeForm
    pk_url_kwarg = "pk"


class SusutypeDeleteView(generic.DeleteView):
    model = models.Susutype
    success_url = reverse_lazy("susume_Susutype_list")


from django.shortcuts import render

# Create your views here.
