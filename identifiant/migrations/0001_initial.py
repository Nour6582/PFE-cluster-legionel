# Generated by Django 4.0.4 on 2022-05-30 11:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
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
            name='User',
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
                ('is_introducteur', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
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
            name='adresseResidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumRue', models.IntegerField(verbose_name='Numero de la Rue')),
                ('NomRue', models.CharField(max_length=100, verbose_name='Nom de la Rue')),
                ('CodePostal', models.IntegerField(verbose_name='Code Postal')),
                ('NumBoitePostal', models.IntegerField(verbose_name='Numero de la Boite Postal')),
                ('NumBattiment', models.IntegerField(verbose_name='Numero du Battiment')),
                ('NumAppartement', models.IntegerField(verbose_name="Numero de l'appartement")),
                ('adressewilaya', models.CharField(max_length=100)),
                ('adresseDaira', models.CharField(max_length=100)),
                ('adresseCommune', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='formulaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Introduction', models.DateField()),
                ('patientvu', models.CharField(choices=[('hospitalisation', 'Hospitalisation'), ('HDJ', 'Hdj'), ('Consultation en dehors de CPU', 'Consultation'), ('PU', 'Pu')], max_length=45, verbose_name='Patient Vu')),
                ('patient', models.BooleanField()),
                ('intro', models.BooleanField()),
                ('etatDuPatient', models.CharField(choices=[('Guéri', 'Gueri'), ('Malade', 'Malade'), ('Décédé', 'Decede')], max_length=45, verbose_name='Etat du patient')),
                ('DiagnosticDepathologiChronique', models.CharField(max_length=1000, verbose_name='Diagnostic de pathologie chronique')),
                ('SipathologieChroniqueAso', models.CharField(blank=True, max_length=4005, verbose_name='Si Pathologie chronique associée ')),
            ],
        ),
        migrations.CreateModel(
            name='lieu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wilaya', models.CharField(max_length=100)),
                ('Daira', models.CharField(max_length=100)),
                ('Commune', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='localisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientvu', models.CharField(choices=[('hospitalisation', 'Hospitalisation'), ('HDJ', 'Hdj'), ('Consultation en dehors de CPU', 'Consultation'), ('PU', 'Pu')], max_length=45, verbose_name='Patient Vu')),
                ('Date_Introduction', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='introducteur',
            fields=[
                ('tel', models.IntegerField(verbose_name='telephone ligne  directe ou le standard avec le numéro de poste')),
                ('Nom', models.CharField(max_length=30)),
                ('Prenom', models.CharField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('telephone', models.CharField(max_length=10)),
                ('fax', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='identitePatient',
            fields=[
                ('Nom', models.CharField(max_length=30)),
                ('NomMarital', models.CharField(blank=True, max_length=30)),
                ('Prenom', models.CharField(blank=True, max_length=30, primary_key=True, serialize=False)),
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=8)),
                ('Date_naissance', models.DateField(blank=True, verbose_name='Date de naissance')),
                ('Tel', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('ResidencePermanent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.adresseresidence')),
                ('lieu_naissance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.lieu')),
            ],
        ),
    ]