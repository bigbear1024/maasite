# Generated by Django 4.0.4 on 2022-04-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipelines', '0006_alter_contact_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='keynote_file',
            field=models.FileField(blank=True, null=True, upload_to='media/meeting/keynote/', verbose_name='簡報上傳'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='other_file',
            field=models.FileField(blank=True, null=True, upload_to='media/meeting/other/', verbose_name='附件上傳'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='sign_file',
            field=models.FileField(blank=True, null=True, upload_to='media/meeting/sign/', verbose_name='簽到表上傳'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='minutes_file',
            field=models.FileField(blank=True, null=True, upload_to='media/meeting/file/', verbose_name='會議記錄上傳'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/meeting/photo/', verbose_name='照片上傳'),
        ),
    ]
