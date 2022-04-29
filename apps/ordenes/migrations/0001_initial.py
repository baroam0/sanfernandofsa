# Generated by Django 3.2 on 2022-04-28 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materiales', '0005_material_unidad'),
        ('obras', '0003_alter_obra_id'),
        ('capataces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('capataz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capataces.capataz')),
                ('obra', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='obras.obra')),
            ],
            options={
                'verbose_name_plural': 'Orden',
            },
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.material')),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.orden')),
            ],
            options={
                'verbose_name_plural': 'Detalles Ordenes',
            },
        ),
    ]
