# Generated by Django 4.1.1 on 2022-09-27 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_member_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]