# Generated by Django 4.0.6 on 2022-08-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=255, unique=True)),
                ('hall_capacity', models.IntegerField()),
                ('projector', models.BooleanField()),
            ],
        ),
    ]
