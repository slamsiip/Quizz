# Generated by Django 3.1.3 on 2022-01-30 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_scored_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='image',
            field=models.ImageField(upload_to='static/todo'),
        ),
        migrations.AlterField(
            model_name='scored',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]