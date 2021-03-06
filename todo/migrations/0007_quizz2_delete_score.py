# Generated by Django 4.0.1 on 2022-01-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_delete_musique_delete_nourriture_quizz_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(choices=[('animaux', 'animaux'), ('musique', 'musique'), ('autres', 'autres')], max_length=100)),
                ('question', models.CharField(max_length=200, null=True)),
                ('op1', models.CharField(max_length=200, null=True)),
                ('op2', models.CharField(max_length=200, null=True)),
                ('op3', models.CharField(max_length=200, null=True)),
                ('op4', models.CharField(max_length=200, null=True)),
                ('ans', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
