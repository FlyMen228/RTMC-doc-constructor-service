# Generated by Django 5.0.2 on 2024-05-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0003_template_fullname_textbox_height_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='fullname_textbox_height',
            field=models.FloatField(default=0, help_text='Определяется автоматически при загрузке шаблона', verbose_name='Высота текстового поля ФИО'),
        ),
        migrations.AlterField(
            model_name='template',
            name='fullname_textbox_width',
            field=models.FloatField(default=0, help_text='Определяется автоматически при загрузке шаблона', verbose_name='Ширина текстового поля ФИО'),
        ),
        migrations.AlterField(
            model_name='template',
            name='fullname_x_coordinate',
            field=models.FloatField(default=0, help_text='Определяется автоматически при загрузке шаблона', verbose_name='Х координата текстового поля ФИО'),
        ),
        migrations.AlterField(
            model_name='template',
            name='fullname_y_coordinate',
            field=models.FloatField(default=0, help_text='Определяется автоматически при загрузке шаблона', verbose_name='Y координата текстового поля ФИО'),
        ),
        migrations.AlterField(
            model_name='template',
            name='organization_textbox_height',
            field=models.FloatField(help_text='Определяется автоматически при загрузке шаблона', null=True, verbose_name='Высота текстового поля названия организации'),
        ),
        migrations.AlterField(
            model_name='template',
            name='organization_textbox_width',
            field=models.FloatField(help_text='Определяется автоматически при загрузке шаблона', null=True, verbose_name='Ширина текстового поля названия организации'),
        ),
        migrations.AlterField(
            model_name='template',
            name='organization_x_coordinate',
            field=models.FloatField(help_text='Определяется автоматически при загрузке шаблона', null=True, verbose_name='Х координата текстового поля названия организации'),
        ),
        migrations.AlterField(
            model_name='template',
            name='organization_y_coordinate',
            field=models.FloatField(help_text='Определяется автоматически при загрузке шаблона', null=True, verbose_name='Y координата текстового поля названия организации'),
        ),
    ]