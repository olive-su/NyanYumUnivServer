# Generated by Django 4.0.1 on 2022-04-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_admin', '0002_delete_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menualias', models.CharField(blank=True, db_column='menuAlias', max_length=50, null=True)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('commentid', models.CharField(blank=True, db_column='commentId', max_length=50, null=True)),
                ('score', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
    ]