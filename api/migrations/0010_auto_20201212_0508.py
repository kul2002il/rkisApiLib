# Generated by Django 3.1.3 on 2020-12-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201211_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='', verbose_name='Обложка книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='api.Author', verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='api.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.book', verbose_name='Книга'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='text',
            field=models.TextField(verbose_name='Текст главы'),
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together={('book', 'number')},
        ),
    ]