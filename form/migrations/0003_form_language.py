# Generated by Django 4.1.7 on 2024-03-16 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_form_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('sp', 'Spanish'), ('ch_s', 'Chinese (Simplified)'), ('ch_t', 'Chinese (Traditional)'), ('ta', 'Tagalog'), ('it', 'Italian'), ('ar', 'Arabic'), ('pu', 'Punjabi'), ('fr', 'French'), ('jp', 'Japanese'), ('kr', 'Korean'), ('ger', 'German'), ('ru', 'Russian'), ('po', 'Portuguese')], default='English', max_length=100),
        ),
    ]