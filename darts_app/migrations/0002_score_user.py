# Generated by Django 2.2.5 on 2019-09-25 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darts_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0)),
                ('user_id', models.PositiveIntegerField(default=0)),
                ('register_date', models.DateTimeField(verbose_name='date registered')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('register_date', models.DateTimeField(verbose_name='date registered')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darts_app.Score')),
            ],
        ),
    ]
