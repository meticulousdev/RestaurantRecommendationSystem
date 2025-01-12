# Generated by Django 5.1.3 on 2025-01-12 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_restaurant_keywords_delete_restaurantcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '키워드',
                'verbose_name_plural': '키워드',
            },
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['-rating'], 'verbose_name': '가게', 'verbose_name_plural': '가게'},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='end_time',
            field=models.TimeField(blank=True, null=True, verbose_name='영업 종료 시간'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating_count',
            field=models.PositiveIntegerField(null=True, verbose_name='별정 개수'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='영업 시작 시간'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.DecimalField(db_index=True, decimal_places=6, max_digits=9, verbose_name='위도'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.DecimalField(db_index=True, decimal_places=6, max_digits=9, verbose_name='경도'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='rating',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=3, verbose_name='별점'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='restaurant.keyword'),
        ),
        migrations.CreateModel(
            name='RestaurantStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
            ],
            options={
                'verbose_name': '가게 통계',
                'verbose_name_plural': '가게 통계',
            },
        ),
    ]
