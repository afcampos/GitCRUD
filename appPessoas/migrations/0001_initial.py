# Generated by Django 4.0.6 on 2022-07-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=256)),
                ('data_nascimento', models.DateField(null=True)),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
    ]
