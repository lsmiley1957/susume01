from django import forms
from . import models


class SusumeForm(forms.ModelForm):
    class Meta:
        model = models.Susume
        fields = [
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


class SusupmtForm(forms.ModelForm):
    class Meta:
        model = models.Susupmt
        fields = [
            "payee_name",
            "pmt_id",
            "pmt_date",
            "pmt_amt_required",
            "pmt_amt",
            "pmt_due",
            "week_mum",
        ]


class SusutypeForm(forms.ModelForm):
    class Meta:
        model = models.Susutype
        fields = []