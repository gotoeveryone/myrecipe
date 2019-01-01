# Generated by Django 2.0.9 on 2019-01-01 17:18

import json
import os
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from recipe.core.models import Classification


def migrate_str_to_relational_id(apps, schema_editor):
    # Fixture のデータを投入
    data = json.loads(open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', 'fixtures', 'classifications.json')).read())
    for d in data:
        Classification.objects.create(**d['fields'])

    Cuisine = apps.get_model('core.Cuisine')
    for c in Cuisine.objects.all():
        print(c.classification_str)
        classification = Classification.objects.filter(
            name=c.classification_str).first()
        c.classification_id = classification.id
        c.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180710_0541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('created_by', models.CharField(max_length=10)),
                ('modified_by', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('sort_order', models.IntegerField(validators=[django.core.validators.MinValueValidator(
                    1), django.core.validators.MaxValueValidator(999)], verbose_name='並び順')),
            ],
            options={
                'verbose_name': '調理分類',
                'verbose_name_plural': '調理分類',
                'db_table': 'classifications',
            },
        ),

        # 旧カラムをリネームして値を退避
        migrations.RenameField(
            model_name='cuisine',
            old_name='classification',
            new_name='classification_str',
        ),
        # 新カラムを追加（この時点ではNULL可とする）
        migrations.AddField(
            model_name='cuisine',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='cuisine', to='core.Classification'),
        ),
        # データの変換を実施
        migrations.RunPython(migrate_str_to_relational_id),
        # 新カラムをNULL不可に
        migrations.AlterField(
            model_name='cuisine',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                    related_name='cuisine', to='core.Classification'),
        ),
        # 旧カラムを削除
        migrations.RemoveField(
            model_name='cuisine',
            name='classification_str',
        ),
    ]
