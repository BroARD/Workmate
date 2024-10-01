# Generated by Django 5.1.1 on 2024-09-30 07:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Breed title')),
            ],
        ),
        migrations.CreateModel(
            name='Kitten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=64, verbose_name='Kitten color')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Kitten age')),
                ('description', models.TextField(verbose_name='Kitten description')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kittens.breed')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
