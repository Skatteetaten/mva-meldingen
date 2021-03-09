def hent():
    with open("./eksempler/melding/mvakode3.xml", "r") as file:
        melding_xml = file.read()
        print(melding_xml, "\n")
        melding_xml = melding_xml.replace("\n", "")

    with open("./eksempler/konvolutt/mvakonvolutt1.xml", "r") as file:
        konvolutt_xml = file.read()
        print(konvolutt_xml, "\n")
        konvolutt_xml = konvolutt_xml.replace("\n", "")

        return melding_xml, konvolutt_xml
