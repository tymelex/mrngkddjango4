# Generated by Django 4.1.7 on 2023-03-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrngkddjango4', '0004_student_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='amount',
            field=models.IntegerField(max_length=100),
        ),
    ]
