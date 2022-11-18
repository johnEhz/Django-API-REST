# Generated by Django 4.1.3 on 2022-11-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_cliente_medicamento_pedido_delete_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='tipo',
            field=models.CharField(choices=[('Analgésico', 'Analgésico'), ('Anestésico', 'Anestésico'), ('Antibiótico', 'Antibiótico'), ('Anticonceptivo', 'Anticonceptivo'), ('Ansiolítico', 'Ansiolítico')], max_length=50),
        ),
    ]