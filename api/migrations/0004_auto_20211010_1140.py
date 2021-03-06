# Generated by Django 3.2 on 2021-10-10 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_product_category_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kategori', to='api.category'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('category_id', 'id')},
        ),
    ]
