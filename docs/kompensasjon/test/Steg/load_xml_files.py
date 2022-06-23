def get(VatReturnSubmission_filename, VatReturn_filename):
    with open("./eksempler/melding/" + VatReturn_filename, "r") as file:
        message_xml = file.read()
        print(message_xml, "\n")
        message_xml = message_xml.replace("\n", "")

    with open("./eksempler/konvolutt/" + VatReturnSubmission_filename, "r") as file:
        envelope_xml = file.read()
        print(envelope_xml, "\n")
        envelope_xml = envelope_xml.replace("\n", "")

        return message_xml, envelope_xml
