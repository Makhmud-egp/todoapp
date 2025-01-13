from django.db import migrations

def reset_todoitem_id_sequence(apps, schema_editor):
    schema_editor.execute('ALTER SEQUENCE todo_app_todoitem_id_seq RESTART WITH 1;')

class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todoitem_status'),  # Update this to the correct last migration
    ]

    operations = [
        migrations.RunPython(reset_todoitem_id_sequence),
    ]
