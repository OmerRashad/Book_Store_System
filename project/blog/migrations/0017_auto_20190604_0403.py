# Generated by Django 2.2.1 on 2019-06-04 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190604_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='roleid',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Role'),
        ),
    ]
