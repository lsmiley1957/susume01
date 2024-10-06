from rest_framework import serializers

from . import models


class SusumeSerializer(serializers.ModelSerializer):

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

class SusupmtSerializer(serializers.ModelSerializer):

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

class SusutypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Susutype
        fields = [
        ]