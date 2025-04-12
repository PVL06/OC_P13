from django.db import migrations

def transfer_data(apps, schema_editors):
    
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    OldAddress = apps.get_model('oc_lettings_site', 'Address')

    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')

    for old_address in OldAddress.objects.all():
        new_address = NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

        old_letting = OldLetting.objects.filter(address=old_address).first()
        if old_letting:
            NewLetting.objects.create(
                title=old_letting.title,
                address=new_address,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
