# Generated by Django 3.2 on 2022-04-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_alter_material_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='unidad',
            field=models.CharField(choices=[('UN', 'Unidad'), ('KG', 'Kilo'), ('M2', 'Metro Cuadrado'), ('M3', 'Metro Cubico'), ('TN', 'Tonelada')], default='UN', max_length=2),
        ),
    ]