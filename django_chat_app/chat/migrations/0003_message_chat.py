# Generated by Django 4.1.4 on 2022-12-11 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_message_set', to='chat.chat'),
        ),
    ]
