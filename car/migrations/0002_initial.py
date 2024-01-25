# Generated by Django 5.0.1 on 2024-01-25 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_cars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='modeli',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_model', to='car.car_model'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ManyToManyField(related_name='Car_photo', to='car.image'),
        ),
        migrations.AddField(
            model_name='car',
            name='kuzov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Car_kuzov', to='car.kuzov'),
        ),
        migrations.AddField(
            model_name='car',
            name='manzil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_location', to='car.locations'),
        ),
        migrations.AddField(
            model_name='car',
            name='uzatish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_qutisi', to='car.uzatish'),
        ),
        migrations.AddField(
            model_name='car',
            name='uzatma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_qutisi', to='car.uzatma'),
        ),
        migrations.AddField(
            model_name='car',
            name='yoqilgi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Car_yoqilgisi', to='car.yoqilgi'),
        ),
    ]