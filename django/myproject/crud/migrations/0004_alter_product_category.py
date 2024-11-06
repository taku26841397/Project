# Generated by Django 4.1.7 on 2024-11-05 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='crud.category'),
        ),
    ]