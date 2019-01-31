# Generated by Django 2.1.4 on 2019-01-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indice_transparencia', '0010_auto_20190116_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Nombre')),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='declared_intention_to_transparent',
        ),
        migrations.RemoveField(
            model_name='person',
            name='period',
        ),
        migrations.RemoveField(
            model_name='person',
            name='reelection',
        ),
        migrations.AddField(
            model_name='person',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='person_set', to='indice_transparencia.Topic', verbose_name='Por favor indique los tres temas o problemáticas en las que le gustaría enfocarse durante su gestión (2019-2024). Debes mantener presionada la tecla "Control" o "Command" (en Mac) para seleccionar más de una opción.'),
        ),
    ]
