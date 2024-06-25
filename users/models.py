from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


Role_CHOICES = (
    ('---Select one ---', '---Select one ---'),
    ('Administrator', 'Administrator'),  # Full Access
    ('Banker', 'Banker'),  # Can Create/Manage Susus and Add/Remove Members, Set terms of SuSu
    ('App_Banker', 'App_Banker'), # System Account for App Manged SuSu, can take over Susu
    ('Auditor1', 'Auditor1'),  # Is Memeber Role User with ability to monitor Bank and Member Payments
    ('Auditor2', 'Auditor2'),  # Is Memeber Role User with ability to monitor Bank and Member Payments
    ('Collector1', 'Collector1'),  # Member can collect and Pay other Member SuSu
    ('Collector2', 'Collector2'),  # Member can collect and Pay other Member Susu
    ('Member', 'Member'),  # Normal SuSu Member..This is the Role most SuSu memebrs will have..,
    ('viewer', 'viewer'),  # Role Granted to Financial Institution, IRS, Legal, Etc.
    ('Blocked', 'Blocked'),  # All Roles/Rights Revoked and or as a Placeholder for new Member, Can Only See SuSu name and Member List
)

#  Hand Choices
Hand_CHOICES = (
    ('---Select one ---', '---Select one ---'),
    ('Shared-Hand', 'Shared-Hand'),
    ('Full-Hand', 'Full-Hand'),

)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    full_name = models.CharField(max_length=5, blank=True, null=True)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    whatsapp_no = models.CharField(max_length=10, blank=True, null=True)
    hand_type = models.CharField(max_length=150, choices=Hand_CHOICES, default='Select-One')
    role = models.CharField(max_length=150, choices=Role_CHOICES, default='Select-One')
    profile_pic = models.ImageField(upload_to='profile_images/', default='default.jpg')

    bank1_name = models.CharField(max_length=30,blank=True)
    bank1_routing_num = models.CharField(max_length=30, blank=True)
    bank1_account_num = models.CharField(max_length=30, blank=True)
    bank1_is_default = models.BooleanField(default=False)

    bank2_name = models.CharField(max_length=30,blank=True)
    bank2_routing_num = models.CharField(max_length=30, blank=True)
    bank2_account_num = models.CharField(max_length=30, blank=True)
    bank2_is_default = models.BooleanField(default=False)

    num_active_susu = models.CharField(max_length=2, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email