# Generated by Django 4.0.5 on 2022-09-16 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование школы')),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patr', models.CharField(max_length=50, verbose_name='Отчество')),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50, verbose_name='Уровень')),
                ('name', models.CharField(max_length=100, verbose_name='Название предмета')),
                ('time', models.CharField(max_length=6, verbose_name='Время начала занятия')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.teacher')),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('patr', models.CharField(max_length=50, verbose_name='Отчество')),
                ('num_class', models.CharField(max_length=3, verbose_name='Класс')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.school')),
            ],
            options={
                'db_table': 'students',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, verbose_name='Тема')),
                ('homework', models.CharField(max_length=500, verbose_name='Домашнее задание')),
                ('date', models.CharField(max_length=10, verbose_name='Дата')),
                ('subjects', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.subject')),
            ],
            options={
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=1, verbose_name='Оценка')),
                ('lessons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.lesson')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.student')),
            ],
            options={
                'db_table': 'journal',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('semester', models.CharField(max_length=1, verbose_name='Семестр')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marks.student')),
                ('sub_first', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_first', to='marks.subject')),
                ('sub_second', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_second', to='marks.subject')),
            ],
            options={
                'db_table': 'choices',
            },
        ),
    ]
