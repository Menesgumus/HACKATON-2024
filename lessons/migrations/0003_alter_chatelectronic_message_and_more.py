# Generated by Django 5.1.2 on 2024-11-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_chatelectronic_delete_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatelectronic',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chatelectronic',
            name='sender',
            field=models.CharField(max_length=10),
        ),
    ]
