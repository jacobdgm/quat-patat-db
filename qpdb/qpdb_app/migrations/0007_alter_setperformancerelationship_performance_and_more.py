# Generated by Django 4.2.16 on 2024-11-07 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qpdb_app', '0006_setperformancerelationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setperformancerelationship',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qpdb_app.performance'),
        ),
        migrations.AlterField(
            model_name='setperformancerelationship',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qpdb_app.set'),
        ),
        migrations.AlterField(
            model_name='tunesetrelationship',
            name='set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qpdb_app.set'),
        ),
        migrations.AlterField(
            model_name='tunesetrelationship',
            name='tune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='qpdb_app.tune'),
        ),
    ]
