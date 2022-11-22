def hent(mva_melding_filnavn, konvolutt_filnavn, skal_printes_ut=False):
    with open("./files/melding/" + mva_melding_filnavn, "r") as file:
        mva_melding_xml = file.read()

        if skal_printes_ut:
            print(mva_melding_xml, "\n")

        mva_melding_xml = mva_melding_xml.replace("\n", "")

    file.close()

    with open("./files/konvolutt/" + konvolutt_filnavn, "r") as file:
        konvolutt_xml = file.read()

        if skal_printes_ut:
            print(konvolutt_xml, "\n")

        konvolutt_xml = konvolutt_xml.replace("\n", "")

    file.close()

    return mva_melding_xml, konvolutt_xml
