# Generated by Django 3.2.4 on 2022-04-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0019_product_minorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='wholesaleproduct',
            name='minorder',
            field=models.TextField(default='some'),
        ),
        migrations.AlterField(
            model_name='product',
            name='minorder',
            field=models.TextField(default='some'),
        ),
    ]
