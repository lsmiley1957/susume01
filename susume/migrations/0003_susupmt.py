# Generated by Django 4.2.15 on 2024-09-22 19:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('susume', '0002_rename_susutype_susume_susutype_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Susupmt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payee_name', models.CharField(blank=True, max_length=150, null=True)),
                ('pmt_id', models.CharField(blank=True, max_length=150, null=True)),
                ('pmt_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pmt_amt_required', models.FloatField(default='0.0')),
                ('pmt_amt', models.FloatField(default='0.0')),
                ('pmt_due', models.FloatField(default='0.0')),
                ('week_mum', models.IntegerField(default='0.0')),
                ('susume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='susu_pmts', to='susume.susume')),
            ],
        ),
    ]
