# Generated by Django 3.0.6 on 2020-08-04 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsgn', '0009_auto_20200804_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='nation',
            field=models.CharField(choices=[('CH', 'China'), ('US', 'America'), ('UK', 'England'), ('GE', 'German'), ('CA', 'Canada')], max_length=80, verbose_name='Nationality'),
        ),
    ]
