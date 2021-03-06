# Generated by Django 3.2.5 on 2021-08-01 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField()),
                ('category', models.CharField(choices=[('pol', 'politics'), ('sprt', 'sports'), ('eco', 'economics'), ('cul', 'cultural'), ('soc', 'social')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Q',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('category', models.CharField(choices=[('pol', 'politics'), ('sprt', 'sports'), ('eco', 'economics'), ('cul', 'cultural'), ('soc', 'social')], max_length=4)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizmaker.a')),
            ],
        ),
    ]
