# Generated by Django 4.0.2 on 2022-02-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_aloqa_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=400)),
            ],
        ),
    ]
