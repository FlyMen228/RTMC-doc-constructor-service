# Generated by Django 4.2.7 on 2023-11-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Сonstructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='event',
            field=models.CharField(db_column='Мероприятие', help_text='Мероприятие, к которому относится шаблон', max_length=200, verbose_name='Мероприятие'),
        ),
    ]
