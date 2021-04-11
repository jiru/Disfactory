# Generated by Django 2.2.13 on 2021-02-03 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_add_document_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='display_status',
            field=models.IntegerField(choices=[(0, '已檢舉'), (1, '已排程稽查'), (2, '陳述意見期'), (3, '已勒令停工'), (4, '已發函斷電'), (5, '已排程拆除'), (6, '已拆除'), (7, '不再追蹤')], db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='document',
            name='factory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='documents', to='api.Factory'),
        ),
        migrations.AlterField(
            model_name='image',
            name='factory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.Factory'),
        ),
        migrations.AlterField(
            model_name='image',
            name='report_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.ReportRecord'),
        ),
        migrations.AlterField(
            model_name='reportrecord',
            name='factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_records', to='api.Factory'),
        ),
        migrations.AlterField(
            model_name='review',
            name='factory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Factory'),
        ),
    ]