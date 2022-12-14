# Generated by Django 4.0.5 on 2022-08-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_alter_recipe_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='quantity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
