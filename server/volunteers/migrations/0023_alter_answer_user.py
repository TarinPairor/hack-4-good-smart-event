# Generated by Django 4.2.9 on 2024-02-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volunteers", "0022_alter_answer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer", name="user", field=models.CharField(max_length=200),
        ),
    ]
