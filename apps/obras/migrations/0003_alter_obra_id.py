<<<<<<< HEAD
# Generated by Django 3.2 on 2022-04-16 20:48
=======
# Generated by Django 3.2 on 2022-04-26 00:07
>>>>>>> 011c1136b6cac864ccb0deff78b40c50555b83bf

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obras', '0002_auto_20210116_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
