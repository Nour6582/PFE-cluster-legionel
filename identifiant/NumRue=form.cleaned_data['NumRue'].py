 NumRue=form.cleaned_data['NumRue']
            NomRue=form.cleaned_data['NomRue']
            CodePostal=form.cleaned_data['CodePostal']
            NumBoitePostal=form.cleaned_data['NumBoitePostal']
            NumBattiment=form.cleaned_data['NumBattiment']
            NumAppartement=form.cleaned_data['NumAppartement']
            adresseWilaya=form.cleaned_data['adresseWilaya']
            adresseDaira=form.cleaned_data['adresseDaira']
            adresseCommune=form.cleaned_data['adresseCommune']
            ResidencePermanent= adresseResidence.objects.create(
                NumRue=NumRue,
                NomRue=NomRue,
                CodePostal=CodePostal,
                NumBoitePostal=NumBoitePostal,
                NumBattiment=NumBattiment,
                NumAppartement=NumAppartement,
                adresseWilaya=adresseWilaya,
                adresseDaira=adresseDaira,
                adresseCommune=adresseCommune,
            )

            Nom=form.cleaned_data['Nomp']
            NomMarital=form.cleaned_data['Nommaritalp']
            Prenom=form.cleaned_data['Prenom']
            
            #agent=lead.objects.first()
            sexe=form.cleaned_data['sexe']
            Date_naissance=form.cleaned_data['datenaissance']
            
            Tel=form.cleaned_data['Tel']
            fax=form.cleaned_data['fax']
            Email=form.cleaned_data['Email']

           

            identitePatient.objects.create(
                Nom=Nom,
                NomMarital=NomMarital,
                Prenom=Prenom,
                sexe=sexe,
                Date_naissance=Date_naissance,
                lieu_naissance=lieu_naissance,
                Tel=Tel,
                fax=fax,
                Email=Email,
                ResidencePermanent=ResidencePermanent,
            
            ) 