# Generated by Django 2.2.8 on 2020-02-12 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_change_old_data_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='report_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='images', to='api.ReportRecord'),
        ),
        migrations.AlterField(
            model_name='reportrecord',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='report_records', to='api.Factory'),
        ),
    ]