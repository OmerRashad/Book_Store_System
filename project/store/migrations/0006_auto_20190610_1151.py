# Generated by Django 2.2.1 on 2019-06-10 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190610_1151'),
        ('store', '0005_accountbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='data',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='is_orderd',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='store.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='order',
            name='ref_code',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='date_ordered',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='is_ordered',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Book'),
        ),
        migrations.AlterField(
            model_name='accountbook',
            name='bookid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Book'),
        ),
        migrations.AlterField(
            model_name='book_profile',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Book'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='amount',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
