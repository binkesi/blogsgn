# Generated by Django 3.0.6 on 2020-07-31 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsgn', '0007_auto_20200729_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Author name'),
        ),
    ]
