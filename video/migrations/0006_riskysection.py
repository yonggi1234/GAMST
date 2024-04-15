# Generated by Django 5.0.3 on 2024-04-08 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_alter_caption_sentiment_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_frame', models.IntegerField()),
                ('end_frame', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video')),
            ],
        ),
    ]