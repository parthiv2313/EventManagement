# Generated by Django 5.0.4 on 2024-04-22 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_event_event_picture_bookevent'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookevent',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]