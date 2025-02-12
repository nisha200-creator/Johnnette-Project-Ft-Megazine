# Generated by Django 5.1.6 on 2025-02-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_remove_mustread_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='must_reads/images/')),
                ('link', models.URLField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
