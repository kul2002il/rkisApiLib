# Generated by Django 3.1.3 on 2020-11-30 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201130_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.category', unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.publisher', unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='title',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Жанр'),
        ),
    ]
