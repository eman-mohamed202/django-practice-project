# Generated by Django 4.0.6 on 2022-08-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumb',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
