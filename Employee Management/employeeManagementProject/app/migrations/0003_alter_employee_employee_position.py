# Generated by Django 4.2.14 on 2024-07-27 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_employee_employee_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Employee_position',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
