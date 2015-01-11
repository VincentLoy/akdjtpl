# vim: fileencoding=utf-8 tw=100 expandtab ts=4 sw=4 :
#
# {{ project_name }}
# (c) 2014 ActivKonnect

from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import django.utils.timezone
import uuid_upload_path.storage


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID',
                                        primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login',
                                                    default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(
                    help_text='Designates that this user has all permissions without explicitly '
                              'assigning them.',
                    verbose_name='superuser status', default=False)),
                ('email', models.EmailField(verbose_name='email', max_length=75, unique=True)),
                ('first_name', models.CharField(verbose_name='firstname', max_length=100)),
                ('last_name', models.CharField(verbose_name='lastname', max_length=100)),
                ('is_staff', models.BooleanField(verbose_name='is staff', default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True,
                                                     verbose_name='date joined')),
                ('picture', sorl.thumbnail.fields.ImageField(
                    help_text='Please upload a picture of at least 200x200px',
                    verbose_name='picture', upload_to=uuid_upload_path.storage.upload_to, null=True,
                    blank=True)),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups',
                                                  help_text='The groups this user belongs to. A '
                                                            'user will get all permissions granted '
                                                            'to each of his/her group.',
                                                  related_query_name='user', blank=True,
                                                  to='auth.Group')),
                ('user_permissions',
                 models.ManyToManyField(related_name='user_set', verbose_name='user permissions',
                                        help_text='Specific permissions for this user.',
                                        related_query_name='user', blank=True,
                                        to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
