# Generated by Django 5.0.6 on 2024-06-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0002_popularproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='popularproduct',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
