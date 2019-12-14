import xml.etree.ElementTree as ET
from GortzTools import simple_get, simple_insert, simple_createstatement, get_redirect_url, simple_update_or_create
import datetime
import mysql.connector
import os

mydb = mysql.connector.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    passwd=os.environ['DB_PASSWORD'],
    port=os.environ['DB_PORT'],
    database="systembolaget",
    charset='utf8',
    use_unicode=True
)

endTable="artiklar"
root = ET.parse('data.xml').getroot()
now = datetime.datetime.now()

for artikel in root.iter('artikel'):
    val = {}
    val["nr"] = artikel.find("nr").text
    val["artikel_id"] = artikel.find("Artikelid").text
    val["argang"] = artikel.find("Argang").text
    if artikel.find("Pant") is not None:
        val["pant"] = artikel.find("Pant").text
    val["varnummer"] = artikel.find("Varnummer").text
    val["namn"] = artikel.find("Namn").text
    val["namn2"] = artikel.find("Namn2").text
    val["prisinklmoms"] = artikel.find("Prisinklmoms").text
    val["volymiml"] = artikel.find("Volymiml").text
    val["pris_per_liter"] =  artikel.find("PrisPerLiter").text
    val["saljstart"] = artikel.find("Saljstart").text
    val["utgatt"] = artikel.find("Utgått").text
    val["varugrupp"] = artikel.find("Varugrupp").text
    val["typ"] = artikel.find("Typ").text
    val["stil"] = artikel.find("Stil").text
    val["forpackning"] = artikel.find("Forpackning").text
    val["forslutning"] = artikel.find("Forslutning").text
    val["ursprung"] = artikel.find("Ursprung").text
    val["ursprunglandnamn"] = artikel.find("Ursprunglandnamn").text
    if artikel.find("Producent") is not None:
        val["producent"] = artikel.find("Producent").text
    val["leverantor"] = artikel.find("Leverantor").text
    val["provadargang"] = artikel.find("Provadargang").text
    val["alkoholhalt"] = artikel.find("Alkoholhalt").text
    val["sortiment"] = artikel.find("Sortiment").text
    val["sortiment_text"] = artikel.find("SortimentText").text
    val["ekologisk"] = artikel.find("Ekologisk").text
    val["etiskt"] = artikel.find("Etiskt").text
    if artikel.find("EtisktEtikett") is not None:
        val["etiskt_etikett"] = artikel.find("EtisktEtikett").text
    val["koscher"] = artikel.find("Koscher").text
    if artikel.find("RavarorBeskrivning") is not None:
        val["ravaror_beskrivning"] = artikel.find("RavarorBeskrivning").text
    val["date"] = str(now.year) + "-" + str(now.month)
    #print(val)
    simple_insert(mydb, 'replace', endTable, val)

