# Generated by Django 4.0.4 on 2022-06-07 02:21

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
                ('telPortable', models.IntegerField(blank=True, null=True, verbose_name='Tel portable')),
                ('fax', models.IntegerField(blank=True, null=True)),
                ('nomUser', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('is_attente', models.BooleanField(default=True)),
                ('is_Medecin', models.BooleanField(default=False)),
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
            ],
        ),
        migrations.CreateModel(
            name='facteurRisque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GreffedeMoelleosseuse', models.CharField(blank=True, max_length=100)),
                ('Greffederein', models.CharField(blank=True, max_length=100)),
                ('Splenectomie', models.CharField(blank=True, max_length=100)),
                ('Tabac', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InfoBiologique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CRP', models.IntegerField()),
                ('Pro_calcitonine', models.IntegerField()),
                ('Albuminémie', models.IntegerField()),
                ('Ferritine', models.IntegerField()),
                ('Sélenium', models.IntegerField()),
                ('Phosphorémie', models.IntegerField()),
                ('Pao2', models.IntegerField()),
                ('LDH', models.IntegerField()),
                ('Tx_de_Globules_blancs', models.IntegerField(verbose_name='Tx de Globules blancs')),
                ('Tx_de_plaquettes', models.IntegerField(verbose_name='Tx de plaquettes ')),
                ('Tx_de_lymphocytes', models.IntegerField(verbose_name='Tx de lymphocytes ')),
                ('SGPT', models.IntegerField()),
                ('SGOT', models.IntegerField()),
                ('Bilirubine', models.IntegerField()),
                ('Phosphatases_alcalines', models.IntegerField(verbose_name='Phosphatases alcalines')),
                ('Urée', models.IntegerField()),
                ('Créatinémie', models.IntegerField()),
                ('Natrémie', models.IntegerField()),
                ('Kaliémie', models.IntegerField()),
                ('Proteinurie', models.IntegerField()),
                ('Hématurie', models.IntegerField()),
                ('CPK', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InfoClinique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fievre', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Fièvre à Préciser ')),
                ('Lethargie', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Léthargie')),
                ('Myalgies_arthralgies', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Myalgies arthralgies')),
                ('Cephalees', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Céphalées')),
                ('Tachycardie', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Tachycardie (>ou=100/mn)')),
                ('Polypnee', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Polypnée (>ou=30/mn)')),
                ('TouxSeche', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Toux seche')),
                ('TouxProductive', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Toux productive')),
                ('TouxPurulente', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Toux purulente')),
                ('DouleurThoracique', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Douleur Thoracique')),
                ('Dyspnee', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Dyspnée')),
                ('DefaillanceRespiratoire', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Défaillance respiratoire')),
                ('Confusion', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Confusion')),
                ('Diarrhees', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Diarrhées')),
                ('Vomissements', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Vomissements')),
                ('Douleurs_abdominales', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Douleurs abdominales ')),
                ('Epanchement_pleuralClinique', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name=' Epanchement pleural')),
                ('AutreInfoClinique', models.CharField(blank=True, max_length=999999999)),
            ],
        ),
        migrations.CreateModel(
            name='InfoRadiologique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Opacités_nodulaires_pseudo_tumorales', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=80, verbose_name='Opacités nodulaires pseudo- tumorales')),
                ('Atteinte_pulmonaire_unilatérale_Droite', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Atteinte pulmonaire unilatérale  Droite')),
                ('Atteinte_pulmonaire_unilatérale_Gauche', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Atteinte pulmonaire unilatérale  Gauche')),
                ('Alvéolaire', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Atteinte pulmonaire bilatérale non systématisée, asymétrique, alvéolaire')),
                ('alveol_interstitielle', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Atteinte pulmonaire bilatérale non systématisée, asymétrique, alveol interstitielle')),
                ('Epanchement_pleuralRadiologique', models.CharField(choices=[('oui', 'Oui'), ('Je ne sais pas', 'Jenesaispas')], max_length=50, verbose_name='Epanchement pleural')),
                ('AutreInfoRadiologigue', models.CharField(blank=True, max_length=9999, verbose_name='Autre Information Radiologigue (Preciser)')),
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
            name='QuestionAvecPrelevement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Liquide_de_ponction_pleurale', models.DateField(blank=True, verbose_name='Date de prelevement du Liquide de ponction pleurale')),
                ('Crachats', models.DateField(blank=True, verbose_name='Date de prelevement du  Crachats')),
                ('Liquides_d_aspirations', models.DateField(blank=True, verbose_name='Date de prelevement du  Liquides d’aspirations')),
                ('Lavage_broncho_pulmonaires', models.DateField(blank=True, verbose_name='Date de prelevement du  Lavage broncho-pulmonaires')),
                ('Urines', models.DateField(blank=True, verbose_name="Date de prelevement d'urines")),
                ('Sang', models.DateField(blank=True, verbose_name='Date de prelevement du  Sang')),
                ('AutrePrelevement', models.CharField(blank=True, max_length=999999, verbose_name='Autre prelevement ')),
            ],
        ),
        migrations.CreateModel(
            name='Therapieimmunosuppressiveencours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chimiothérapie', models.CharField(blank=True, max_length=100)),
                ('anti_TNFalpha', models.CharField(blank=True, max_length=100)),
                ('Corticothérapie', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='traitementRecu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traitementEncours', models.CharField(blank=True, max_length=8484)),
                ('traitementAvantConsultation', models.CharField(blank=True, max_length=8484)),
                ('AutreTraitementimmunosuppresseur', models.CharField(blank=True, max_length=8484)),
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
            name='identitePatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=30)),
                ('NomMarital', models.CharField(blank=True, max_length=30)),
                ('Prenom', models.CharField(blank=True, max_length=30)),
                ('sexe', models.CharField(blank=True, choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=8)),
                ('Date_naissance', models.DateField(blank=True, verbose_name='Date de naissance')),
                ('Tel', models.IntegerField()),
                ('fax', models.IntegerField()),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('ResidencePermanent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.adresseresidence')),
                ('lieu_naissance', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.lieu')),
            ],
        ),
        migrations.CreateModel(
            name='formulaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Introduction', models.DateField()),
                ('patientvu', models.CharField(choices=[('hospitalisation', 'Hospitalisation'), ('HDJ', 'Hdj'), ('Consultation en dehors de CPU', 'Consultation'), ('PU', 'Pu')], max_length=45, verbose_name='Patient Vu')),
                ('etatDuPatient', models.CharField(choices=[('Guéri', 'Gueri'), ('Malade', 'Malade'), ('Décédé', 'Decede')], max_length=45, verbose_name='Etat du patient')),
                ('DiagnosticDepathologiChronique', models.CharField(max_length=1000, verbose_name='Diagnostic de pathologie chronique')),
                ('SipathologieChroniqueAso', models.CharField(blank=True, max_length=4005, verbose_name='Si Pathologie chronique associée ')),
                ('InfoSupDunEntourage', models.CharField(blank=True, max_length=995555)),
                ('InfoBiologique', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.infobiologique')),
                ('InfoClinique', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.infoclinique')),
                ('InfoRadiologique', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.inforadiologique')),
                ('QuestionAvecPrelevement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.questionavecprelevement')),
                ('Therapieimmunosuppressiveencours', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.therapieimmunosuppressiveencours')),
                ('facteurRisque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.facteurrisque')),
                ('identitePatient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='identifiant.identitepatient')),
                ('medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('traitementRecu', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.traitementrecu')),
            ],
        ),
        migrations.AddField(
            model_name='adresseresidence',
            name='adresse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='identifiant.lieu'),
        ),
    ]
