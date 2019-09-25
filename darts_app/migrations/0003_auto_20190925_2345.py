# Generated by Django 2.2.5 on 2019-09-25 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darts_app', '0002_score_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
        migrations.AddField(
            model_name='score',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='darts_app.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]