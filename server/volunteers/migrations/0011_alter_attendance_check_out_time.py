# Generated by Django 4.2.9 on 2024-02-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("volunteers", "0010_alter_event_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="check_out_time",
            field=models.DateTimeField(null=True),
        ),
    ]
