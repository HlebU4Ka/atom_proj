# Generated by Django 4.2.7 on 2023-11-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habit_related_habit_alter_habit_time_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='telegram_chat_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]