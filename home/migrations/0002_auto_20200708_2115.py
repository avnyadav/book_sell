
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='pickuplocation',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.CharField(default='', max_length=200),
      
      
      
        ),
    ]




