# Generated by Django 4.2.9 on 2024-02-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        (
            "volunteers",
            "0004_remove_anonymoususer_name_anonymoususer_last_login_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Participant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("username", models.CharField(max_length=255, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True, related_name="participant_groups", to="auth.group"
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="participant_permissions",
                        to="auth.permission",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.DeleteModel(name="AnonymousUser",),
    ]
