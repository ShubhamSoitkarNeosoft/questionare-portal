# Generated by Django 4.1 on 2022-09-01 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_assesment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interviewee",
            name="category_name",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.category",
            ),
        ),
        migrations.AlterField(
            model_name="interviewee",
            name="interview_date",
            field=models.DateField(default=None, max_length=255),
        ),
    ]
