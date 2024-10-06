from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse
from django.views import generic
from django.template import Template, RequestContext
from django.template.response import TemplateResponse

from . import models
from . import forms


class HTMXSusumeListView(generic.ListView):
    model = models.Susume
    form_class = forms.SusumeForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request, 'htmx/list.html', context)


class HTMXSusumeCreateView(generic.CreateView):
    model = models.Susume
    form_class = forms.SusumeForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXSusumeDeleteView(generic.DeleteView):
    model = models.Susume
    success_url = reverse_lazy("susume_Susume_htmx_list")

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXSusupmtListView(generic.ListView):
    model = models.Susupmt
    form_class = forms.SusupmtForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request, 'htmx/list.html', context)


class HTMXSusupmtCreateView(generic.CreateView):
    model = models.Susupmt
    form_class = forms.SusupmtForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXSusupmtDeleteView(generic.DeleteView):
    model = models.Susupmt
    success_url = reverse_lazy("susume_Susupmt_htmx_list")

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()


class HTMXSusutypeListView(generic.ListView):
    model = models.Susutype
    form_class = forms.SusutypeForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "objects": self.get_queryset()
        }
        return TemplateResponse(request, 'htmx/list.html', context)


class HTMXSusutypeCreateView(generic.CreateView):
    model = models.Susutype
    form_class = forms.SusutypeForm

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(request, 'htmx/form.html', context)

    def form_valid(self, form):
        super().form_valid(form)
        context = {
            "model_id": self.model._meta.verbose_name_raw,
            "object": self.object,
            "form": form
        }
        return TemplateResponse(self.request, 'htmx/create.html', context)

    def form_invalid(self, form):
        super().form_invalid(form)
        context = {
            "create_url": self.model.get_htmx_create_url(),
            "form": self.get_form()
        }
        return TemplateResponse(self.request, 'htmx/form.html', context)


class HTMXSusutypeDeleteView(generic.DeleteView):
    model = models.Susutype
    success_url = reverse_lazy("susume_Susutype_htmx_list")

    def form_valid(self, form):
        super().form_valid(form)
        return HttpResponse()