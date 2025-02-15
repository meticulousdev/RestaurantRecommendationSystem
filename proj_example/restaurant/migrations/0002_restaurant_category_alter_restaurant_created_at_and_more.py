# Generated by Django 5.1.3 on 2025-01-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(db_index=True, max_length=50, verbose_name='이름'),
        ),
    ]
