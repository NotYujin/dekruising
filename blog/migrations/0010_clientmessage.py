# Generated by Django 5.1.4 on 2025-01-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_productlist_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('company', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Sent At')),
            ],
            options={
                'verbose_name': 'Client Message',
                'verbose_name_plural': 'Client Messages',
                'ordering': ['-sent_at'],
            },
        ),
    ]
