# Generated by Django 5.0.6 on 2024-06-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_task', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='to_do',
            name='new_task',
            field=models.CharField(max_length=50),
        ),
    ]
