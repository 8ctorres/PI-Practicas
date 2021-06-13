# Generated by Django 2.2.24 on 2021-06-12 23:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleIndicatorChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='Spain', max_length=100)),
                ('indicators', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SingleIndicatorChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.CharField(default='Life expectancy', max_length=100)),
                ('countries', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiple_indicators', models.ManyToManyField(to='user_management.MultipleIndicatorChart')),
                ('single_indicator', models.ManyToManyField(to='user_management.SingleIndicatorChart')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]