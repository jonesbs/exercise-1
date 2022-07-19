from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("book_id", models.IntegerField()),
                ("review", models.CharField(max_length=255)),
                ("rate", models.IntegerField()),
            ],
        ),
    ]
