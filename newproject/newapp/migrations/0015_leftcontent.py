# Generated by Django 5.1.6 on 2025-02-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0014_featuredpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeftContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_desc', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
                ('link', models.URLField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
