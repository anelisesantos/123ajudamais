# Generated by Django 4.2.3 on 2023-07-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CentroPsicossocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('abrangencia', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('contatos', models.CharField(max_length=200)),
                ('ramais', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]