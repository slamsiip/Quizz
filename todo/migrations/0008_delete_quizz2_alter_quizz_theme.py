# Generated by Django 4.0.1 on 2022-01-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_quizz2_delete_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Quizz2',
        ),
        migrations.AlterField(
            model_name='quizz',
            name='theme',
            field=models.CharField(choices=[('animaux', 'animaux'), ('musique', 'musique'), ('autres', 'autres')], max_length=100),
        ),
    ]
