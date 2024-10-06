from django.contrib import admin
from django import forms

from . import models


class SusumeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Susume
        fields = "__all__"


class SusumeAdmin(admin.ModelAdmin):
    form = SusumeAdminForm
    list_display = [
        "name",
        "description",
        "suss_pot",
        "suss_weeks",
        "date_start",
        "date_end",
        "num_rounds",
        "hand_schedule_calc",
        "default_currencytype",
        "default_pmt_per_hand",
        "factor_calc",
        "createby",
    ]
    readonly_fields = [
        "name",
        "description",
        "suss_pot",
        "suss_weeks",
        "date_start",
        "date_end",
        "num_rounds",
        "hand_schedule_calc",
        "default_currencytype",
        "default_pmt_per_hand",
        "factor_calc",
        "createby",
    ]


class SusupmtAdminForm(forms.ModelForm):

    class Meta:
        model = models.Susupmt
        fields = "__all__"


class SusupmtAdmin(admin.ModelAdmin):
    form = SusupmtAdminForm
    list_display = [
        "payee_name",
        "pmt_id",
        "pmt_date",
        "pmt_amt_required",
        "pmt_amt",
        "pmt_due",
        "week_mum",
    ]
    readonly_fields = [
        "payee_name",
        "pmt_id",
        "pmt_date",
        "pmt_amt_required",
        "pmt_amt",
        "pmt_due",
        "week_mum",
    ]


class SusutypeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Susutype
        fields = "__all__"


class SusutypeAdmin(admin.ModelAdmin):
    form = SusutypeAdminForm
    list_display = [
    ]
    readonly_fields = [
    ]


admin.site.register(models.Susume, SusumeAdmin)
admin.site.register(models.Susupmt, SusupmtAdmin)
admin.site.register(models.Susutype, SusutypeAdmin)