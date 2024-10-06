from django.db import models
from django.utils import timezone

DepositSchedule_CHOICES = (
    ('---Select one ---', '---Select one ---'),
    ('Weekly', 'Weekly'),  # Full Access
    ('Bi-Weekly', 'Bi-Weekly'),  # Can Create/Manage Susus and Add/Remove Members, Set terms of SuSu
    ('Monthly', 'Monthly'), # System Account for App Manged SuSu, can take over Susu
    ('Bi-Monthly', 'Bi-Monthly'),  # Is Memeber Role User with ability to monitor Bank and Member Payments

)

SusuLength_CHOICES = (
    ('---Select one ---', '---Select one ---'),
    ('90 Days)', '90'),  # Full Access
    ('120 Days', '120'),  # Can Create/Manage Susus and Add/Remove Members, Set terms of SuSu
    ('180 Days', '180'), # System Account for App Manged SuSu, can take over Susu
    ('240 Days', '240'),  # Is Memeber Role User with ability to monitor Bank and Member Payments
    ('365 Days', '365'),  # Is Memeber Role User with ability to monitor Bank and Member Payments

)

#  Hand Choices
# Hand_CHOICES = (
#     ('---Select one ---', '---Select one ---'),
#     ('Shared-Hand', 'Shared-Hand'),
#     ('Full-Hand', 'Full-Hand'),
#
# )


class Susutype(models.Model):
    typename = models.CharField(
        db_column='DeliveryTypeName',
        max_length=150,
        blank=True,
        null=True)
    description = models.CharField(
        db_column='DeliveryUseDescription',
        max_length=150,
        blank=True,
        null=True)
    memo1 = models.CharField(
        db_column='MemoDeliveryNote1',
        max_length=150,
        blank=True,
        null=True)

    def __str__(self):
        return self.typename


class Susume(models.Model):
    # Su Su name and Type
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    susutype = models.ForeignKey(Susutype,  on_delete=models.CASCADE, related_name='susu_types')

    # Su Su Pot, Duration, Start/End Dates
    suss_pot = models.FloatField( default='0.0')
    suss_weeks = models.FloatField( default='0.0')
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(default=timezone.now)

    # Calculation of Su Su  Rounds, Length and Hand Payments
    num_rounds = models.FloatField( default='0.0')
    hand_schedule_calc = models.CharField(max_length=150, choices=DepositSchedule_CHOICES, default='Select-One')
    default_currencytype = models.CharField(max_length=150, blank=True, null=True)
    default_pmt_per_hand = models.FloatField(default='0.0')

    #
    # workweek = models.FloatField(default='40.0')
    factor_calc = models.FloatField(default='1.0')
    createby = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class Susupmt(models.Model):
    susume = models.ForeignKey(Susume, on_delete=models.CASCADE, related_name='susu_pmts')
    payee_name = models.CharField(max_length=150, blank=True, null=True)
    pmt_id = models.CharField(max_length=150, blank=True, null=True)
    pmt_date = models.DateTimeField(default=timezone.now)
    pmt_amt_required = models.FloatField( default='0.0')
    pmt_amt = models.FloatField( default='0.0')
    pmt_due = models.FloatField( default='0.0')
    week_mum = models.IntegerField( default='0.0')



    data = {
        "amount": "50.00",
        "currency": "EUR",
        "payment_method": {
            "type": "gb_visa_card",
            "fields": {
                "number": "4111111111111111",
                "expiration_month": "12",
                "expiration_year": "27",
                "cvv": "567",
                "name": "John Doe"
            }
        }
    }

    def __str__(self):
        return self.payee_name

