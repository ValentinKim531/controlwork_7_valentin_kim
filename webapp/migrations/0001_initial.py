# Generated by Django 4.1.7 on 2023-02-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('mail', models.EmailField(max_length=50, verbose_name='Электронная почта')),
                ('text', models.TextField(max_length=2000, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Записи',
                'verbose_name_plural': 'Гостевая книга',
            },
        ),
    ]
