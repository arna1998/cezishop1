# Generated by Django 5.1.4 on 2024-12-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothing', '0003_remove_product_size_product_is_sale_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='media/upload/product/'),
        ),
    ]
