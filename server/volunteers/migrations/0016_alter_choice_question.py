# Generated by Django 4.2.9 on 2024-02-07 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("volunteers", "0015_remove_question_choices_choice_question"),
    ]

    operations = [
        migrations.AlterField(
            model_name="choice",
            name="question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="choices",
                to="volunteers.question",
            ),
        ),
    ]