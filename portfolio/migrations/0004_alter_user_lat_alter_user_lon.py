# Generated by Django 4.1.1 on 2022-09-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0003_alter_user_location"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="lat",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="lon",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]