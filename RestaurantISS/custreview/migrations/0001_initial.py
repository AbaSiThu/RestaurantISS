# Generated by Django 2.2.2 on 2019-07-20 12:40

from django.db import migrations, models
import django.db.models.aggregates


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Catname', models.CharField(max_length=100)),
                ('Catid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('Resname', models.CharField(max_length=200)),
                ('Resid', models.IntegerField(primary_key=True, serialize=False)),
                ('Resadd', models.CharField(max_length=300)),
                ('Resimage', models.CharField(max_length=300, null=True)),
                ('Resdesc', models.CharField(max_length=300, null=True)),
                ('Catid', models.ForeignKey(db_column='Catid', on_delete=django.db.models.aggregates.Aggregate, to='custreview.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('Revname', models.CharField(max_length=200)),
                ('Revid', models.IntegerField(primary_key=True, serialize=False)),
                ('Rating', models.IntegerField(default=0)),
                ('Resid', models.ForeignKey(db_column='Resid', on_delete=django.db.models.aggregates.Aggregate, to='custreview.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('Comid', models.IntegerField(primary_key=True, serialize=False)),
                ('Ce_text', models.CharField(max_length=200)),
                ('Revid', models.ForeignKey(db_column='Revid', on_delete=django.db.models.aggregates.Aggregate, to='custreview.Review')),
            ],
        ),
    ]
