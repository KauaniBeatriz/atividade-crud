# Generated by Django 5.1.4 on 2024-12-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
