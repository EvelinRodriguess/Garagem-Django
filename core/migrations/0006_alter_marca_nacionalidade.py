# Generated by Django 5.0.2 on 2024-04-10 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_marca"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marca",
            name="nacionalidade",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
