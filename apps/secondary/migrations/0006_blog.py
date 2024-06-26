# Generated by Django 5.0.6 on 2024-05-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0005_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo/', verbose_name='фото')),
                ('data', models.DateField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Навзание')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блог',
            },
        ),
    ]
