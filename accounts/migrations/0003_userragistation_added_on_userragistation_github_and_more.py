# Generated by Django 4.0.3 on 2022-05-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userragistation_designation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userragistation',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='userragistation',
            name='github',
            field=models.CharField(default='@github', max_length=250),
        ),
        migrations.AddField(
            model_name='userragistation',
            name='twitter',
            field=models.CharField(default='@twiter', max_length=250),
        ),
        migrations.AddField(
            model_name='userragistation',
            name='update_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
