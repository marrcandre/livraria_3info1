# Generated by Django 5.0.2 on 2024-08-02 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_remove_livro_coautor_remove_livro_autor_livro_autor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livro",
            name="autor",
            field=models.ManyToManyField(related_name="livros", to="core.autor"),
        ),
    ]
