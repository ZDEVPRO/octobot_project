# Generated by Django 4.0.2 on 2022-02-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLogoMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/FooterLogo/', verbose_name='Logotip')),
                ('description', models.TextField(max_length=300, verbose_name=' Kompaniya haqida')),
                ('instagram', models.CharField(max_length=100)),
                ('telegram', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
            },
        ),
    ]