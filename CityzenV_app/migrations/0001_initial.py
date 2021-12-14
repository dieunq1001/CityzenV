# Generated by Django 4.0 on 2021-12-14 13:53

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='A1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home_town', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='A2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home_town', models.TextField()),
                ('a1_control_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CityzenV_app.a1')),
            ],
        ),
        migrations.CreateModel(
            name='A3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home_town', models.TextField()),
                ('a2_control_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CityzenV_app.a2')),
            ],
        ),
        migrations.CreateModel(
            name='B1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home_town', models.TextField()),
                ('a3_control_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CityzenV_app.a3')),
            ],
        ),
        migrations.CreateModel(
            name='CongDan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identity_id', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('home_town', models.TextField()),
                ('permanent_address', models.TextField()),
                ('temporary_address', models.TextField()),
                ('religion', models.CharField(max_length=255)),
                ('educational_level', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'Admin'), (2, 'A1'), (3, 'A2'), (4, 'A3'), (5, 'B1'), (6, 'B2')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='B2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home_town', models.TextField()),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CityzenV_app.customuser')),
                ('b1_control_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='CityzenV_app.b1')),
            ],
        ),
        migrations.AddField(
            model_name='b1',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CityzenV_app.customuser'),
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CityzenV_app.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='a3',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CityzenV_app.customuser'),
        ),
        migrations.AddField(
            model_name='a2',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CityzenV_app.customuser'),
        ),
        migrations.AddField(
            model_name='a1',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='CityzenV_app.customuser'),
        ),
    ]
