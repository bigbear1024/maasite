# Generated by Django 4.0.4 on 2022-04-27 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0014_project_alter_company_options_alter_contact_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='里程碑名稱')),
                ('completion_date', models.DateField(default=datetime.date.today, verbose_name='完成日期')),
            ],
            options={
                'verbose_name': '重要里程碑',
                'verbose_name_plural': 'D.重要里程碑',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('number',), 'verbose_name': '通訊錄', 'verbose_name_plural': 'G.通訊錄'},
        ),
        migrations.AlterModelOptions(
            name='road',
            options={'verbose_name': '道路清單', 'verbose_name_plural': 'E.道路清單'},
        ),
        migrations.AlterModelOptions(
            name='websitelink',
            options={'verbose_name': '網站連結', 'verbose_name_plural': 'F.網站連結'},
        ),
    ]
