---
icon: "cloud"
title: "Test"
description: ""
---

På denne siden vil det etter hvert komme informasjon om hvordan du kan gjennomføre test av den nye valideringstjenesten og innsendingsløpet inkludert å få kvittering tilbake.

For de tidlige testene hvor et fåtall av systemleverandørene er involvert, vil informasjon om test og testgjennomføring tas direkte med de involverte.

Resultatet av de tidlige testene vil dokumenteres og informasjon om dette vil være tilgjengelig for alle som ønsker å følge med underveis.

# Testplan

Testplanen onder viser når det vi være mulig å teste integrasjonene mot Skatteetaten sine nye løsninger.

<table align=center>
  <tr><th align=center>Hva</th><th align=center>Når</th><th align=center>Innhold</th></tr>
  <tr><td>Dokumentasjon XSD</td><td>28.09.2020</td><td><ul><li>Oppdatert xsd etter tilbakemeldinger i møte 14.9</li></ul></td></tr>
  <tr><td>Test 1 – teknisk verifikasjon</td><td>nov.20</td><td><ul><li>Valideringstjeneste -"Dummy"  (Ping fra SBS)</li></ul></td></tr> 
  <tr><td>Test 2 – syltynn valideringstjeneste og teknisk verifikasjon av innsendingstjenesten</td><td>jan.21</td>
  <td> 
  <ul>
	<li>Valideringstjeneste </li>
	<li>Helt enkel tjeneste med en eller få enkle valideringe </li>
    <li>Innsendingstjeneste - "Dummy"  (Ping fra SBS)</li>
  </ul>
  </td></tr>
  <tr><td>Test 3 - noe rikere valideringstjeneste og en enkel innsendingstjeneste</td><td>mar.21</td><td>Content c3</td></tr>
  <tr><td>Content a3</td><td>Content b3</td>
  <td>
  <ul>
	<li>Valideringstjeneste - Valideringstjeneste som inneholder mange av de valideringene som skal brukes</li>
	<li>Innsendingstjeneste - Enkel innsendingstjeneste som skal verifisere innsendingen og gi kvittering tilbake</li>
	<li></li>
	<li></li>
	<li></li>
  </ul>
  </td></tr>
  <tr><td>Test 4 – hovedtest før pilot</td><td>mai.21</td><td>
  <ul>
	<li>Valideringstjeneste - Komplett tjeneste, sånn den skal være til pilot, er på plass</li>
	<li>Innsendingstjeneste - Komplett tjeneste, sånn den skal være til pilot, er på plass</li>
	<li></li>
	<li></li>
	<li></li>
  </ul>
  </td></tr>
  <tr><td>Test 5 - hovedtest</td><td>aug. 21</td><td></td></tr>
  <tr><td>Pilot</td><td>aug. 21</td><td></td></tr>
  <tr><td>Produksjon</td><td>01.01.2022</td><td></td></tr>  
</table>

![Testplan](Testplan.png)
