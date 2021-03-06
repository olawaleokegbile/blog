# Generated by Django 3.2.8 on 2021-11-24 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_comment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='date_added',
            new_name='date',
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
