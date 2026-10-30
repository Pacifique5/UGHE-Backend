from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="footer_background_color",
            field=models.CharField(default="#C22226", max_length=20),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="footer_heading",
            field=models.CharField(default="Connect With Us", max_length=80),
        ),
        migrations.AddField(
            model_name="sitesettings",
            name="footer_text_color",
            field=models.CharField(default="#FFFFFF", max_length=20),
        ),
        migrations.AddField(
            model_name="stat",
            name="count_duration_ms",
            field=models.PositiveIntegerField(default=2000),
        ),
        migrations.AddField(
            model_name="stat",
            name="count_suffix",
            field=models.CharField(
                blank=True,
                help_text="Appended after the animated number, for example TH.",
                max_length=12,
            ),
        ),
        migrations.AddField(
            model_name="stat",
            name="count_to",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Number the homepage animates toward. Leave empty to show the label immediately.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="stat",
            name="use_grouping",
            field=models.BooleanField(
                default=True,
                help_text="Insert thousands separators while the number counts up.",
            ),
        ),
        migrations.AlterField(
            model_name="stat",
            name="background_color",
            field=models.CharField(default="#C42127", max_length=20),
        ),
        migrations.AlterField(
            model_name="stat",
            name="display_value",
            field=models.CharField(
                help_text="Final label, for example 1,260 or 4TH. The page counts up to it.",
                max_length=40,
            ),
        ),
        migrations.CreateModel(
            name="FooterOffice",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("body", models.TextField(help_text="Line breaks are kept on the page.")),
                ("position", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "Footer offices",
                "ordering": ["position", "id"],
            },
        ),
        migrations.CreateModel(
            name="LandingBlock",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("promo", "Promo"),
                            ("feature", "Feature"),
                            ("news", "News heading"),
                            ("impact", "Impact"),
                        ],
                        default="feature",
                        max_length=16,
                    ),
                ),
                ("title", models.CharField(max_length=180)),
                ("body", models.TextField(blank=True)),
                ("button_label", models.CharField(blank=True, max_length=120)),
                ("button_url", models.URLField(blank=True, max_length=500)),
                ("image_file", models.ImageField(blank=True, upload_to="landing/")),
                (
                    "image_url",
                    models.URLField(
                        blank=True,
                        help_text="Image URL, or a YouTube link for a promo band.",
                        max_length=500,
                    ),
                ),
                ("background_color", models.CharField(default="#000000", max_length=20)),
                ("overlay_color", models.CharField(default="#00000099", max_length=20)),
                ("text_color", models.CharField(default="#FFFFFF", max_length=20)),
                ("button_color", models.CharField(default="#FFFFFF", max_length=20)),
                ("button_text_color", models.CharField(default="#C42127", max_length=20)),
                (
                    "group_key",
                    models.CharField(
                        blank=True,
                        help_text="Feature columns with the same key share one background.",
                        max_length=40,
                    ),
                ),
                ("position", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["position", "id"],
            },
        ),
        migrations.CreateModel(
            name="NewsStory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=220)),
                ("url", models.URLField(max_length=500)),
                ("image_file", models.ImageField(blank=True, upload_to="news/")),
                ("image_url", models.URLField(blank=True, max_length=500)),
                ("category", models.CharField(blank=True, max_length=160)),
                ("category_url", models.URLField(blank=True, max_length=500)),
                ("position", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "News stories",
                "ordering": ["position", "id"],
            },
        ),
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("label", models.CharField(max_length=40)),
                ("url", models.URLField()),
                ("position", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["position", "id"],
            },
        ),
    ]
