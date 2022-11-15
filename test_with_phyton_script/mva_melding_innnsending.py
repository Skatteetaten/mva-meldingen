# import os
from Steg import hent_idporten_token, hent_altinn_token
from Steg import instans, instans_dataelement
from Steg import hent_eksempel_filer
from test_with_phyton_script import config
from Steg.validering import valider_mva_melding


# INSTILLINGER #

# Kalle valideringstjenesten før man starter innsendingen.
skal_validere_før_innsending = True

# Ferdiggjøre utfylling og sende inn
skal_sende_inn_innsending = True

# Fullføre innsendingen (Bekrefte/Signere)
skal_godkjenne_innsending = True

# Gjør ingenting akkurat nå
skal_hente_tilbakemelding = False

# Laster opp miljø fil for å definere skd-miljø. F.eks. for SIT1
skal_laste_opp_miljø_fil = False

# Laster opp et pdf vedlegg i innsendingen.
skal_laste_opp_vedlegg = False

altinn_app_miljø = config.altinn_app_miljø.tt02.value  # Trenger ikke å endre på
altinn_plattform_miljø = config.altinn_plattform_miljø.tt02.value  # Trenger ikke å endre på
skatteetaten_miljø = config.skatteetaten_miljø.ETM2.value  # Endre hvilket miljø som skal bli definert i miljø filen
altinn3_app = config.altinn3_app.ETM2.value  # Endre hvilken altinn3-applikasjon python skriptet skal gå mot

# Fil navn på MvaMeldingInnsending  ("konvolutt") mvamelding som ønskes å lastes opp.
# Må ligge i ./example_files/konvolutt/ og ./example_files/melding/
mvaMeldingInnsending_filnavn = "kompensasjon_mvakonvolutt.xml"
mvaMelding_filnavn = "kompensasjon_mvamelding.xml"

# Legg inn org_nummer du ønsker å sende inn for.
# Merk at personen som skal sende inn må ha nødvendig roller/rettigheter i altinn for å få lov til å sende inn.
org_nummer = "999999999"

print("----- INSTILLINGER -----")
print(f"Altinn Applikasjon Miljø: {altinn_app_miljø}")
print(f"Altinn Plattform Miljø: {altinn_plattform_miljø}")
print(f"Skatteetaten Miljø: {skatteetaten_miljø}")
print(f"Altinn App: {altinn3_app}")
print("-----------------------------------------------------")
print(f"skal_validere_før_innsending: {skal_validere_før_innsending}")
print(f"skal_sende_inn_innsending: {skal_sende_inn_innsending}")
print(f"skal_godkjenne_innsending: {skal_godkjenne_innsending}")
print(f"skal_laste_opp_miljø_fil: {skal_laste_opp_miljø_fil}")
print(f"skal_laste_opp_vedlegg: {skal_laste_opp_vedlegg}")
print("\n")

mva_melding_xml, konvolutt_xml = hent_eksempel_filer.hent(mvaMelding_filnavn, mvaMeldingInnsending_filnavn)

print("----- Henter ID-token -----")
header = hent_idporten_token.get_idtoken()

if skal_validere_før_innsending:
    print("----- Validerer mva-melding -----")
    validering = valider_mva_melding(altinn3_app, dict(header), xml=mva_melding_xml)

print("----- Henter altinn token -----")
altinn_token = hent_altinn_token.hent(altinn_plattform_miljø, header)

if skal_sende_inn_innsending:
    print("----- Opretter instans -----")
    instance = instans.opprett(
        altinn_app_miljø=altinn_app_miljø,
        altinn3_app=altinn3_app,
        altinn_token=altinn_token,
        org_number=org_nummer
    )
    instans_id = instance['id']
    print(f"meldingRef={instans_id}")
    path = "./Resources/instanser/" + instans_id + "/"

    print("----- Oppdaterer MvaMeldingInnsending -----")
    instans_dataelement.oppdater_konvolutt(
        altinn_app_miljø=altinn_app_miljø,
        altinn3_app=altinn3_app,
        instans_id=instans_id,
        data_element_id=instance['data'][0]['id'],
        konvolutt_xml=konvolutt_xml,
        altinn_token=altinn_token
    )

    print("----- Laster opp mva-melding -----")
    instans_dataelement.last_opp_mva_melding(
        altinn_app_miljø=altinn_app_miljø,
        altinn3_app=altinn3_app,
        instans_id=instans_id,
        melding_xml=mva_melding_xml,
        altinn_token=altinn_token
    )

    if skal_laste_opp_vedlegg:
        print("----- Laster opp vedlegg -----")
        instans_dataelement.last_opp_vedlegg(
            altinn_app_miljø=altinn_app_miljø,
            altinn3_app=altinn3_app,
            instans_id=instans_id,
            vedlegg="png-vedlegg.png",
            filnavn="pngVedlegg.png",
            content_type="image/png",
            altinn_token=altinn_token
        )

    if skal_laste_opp_miljø_fil:
        print("----- Laster opp miljø fil -----")
        instans_dataelement.last_opp_miljoefil(
            altinn_app_miljø=altinn_app_miljø,
            altinn3_app=altinn3_app,
            instans_id=instans_id,
            miljo=skatteetaten_miljø,
            altinn_token=altinn_token
        )

    print("----- Sender inn MvaMeldingInnsending -----")
    utfylling = instans.neste_prosess(
        altinn_app_miljø=altinn_app_miljø,
        altinn3_app=altinn3_app,
        instans_id=instans_id,
        altinn_token=altinn_token
    )

    if skal_godkjenne_innsending:
        print("----- Fullfører MvaMeldingInnsending -----")
        bekreftelse = instans.neste_prosess(
            altinn_app_miljø=altinn_app_miljø,
            altinn3_app=altinn3_app,
            instans_id=instans_id,
            altinn_token=altinn_token
        )

    print("----- Henter instansen -----")
    instance = instans.hent_instans(
        altinn_app_miljø=altinn_app_miljø,
        altinn3_app=altinn3_app,
        instans_id=instans_id,
        altinn_token=altinn_token
    )
