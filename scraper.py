import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://www.fsdm.usmba.ac.ma"
LOGIN_URL = f"{BASE_URL}/Student/login"
NOTES_URL = f"{BASE_URL}/Student/Notes"

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

students = [
    {"cne": "N135035397", "cin": "CD973522", "email": "amina.aamrani@usmba.ac.ma"},
    {"cne": "S139155212", "cin": "ZH18787", "email": "adnane.abdli@usmba.ac.ma"},
    {"cne": "N146071341", "cin": "CD945451", "email": "sohayb.aboudar@usmba.ac.ma"},
    {"cne": "N120044685", "cin": "CD629131", "email": "fatimazahra.abrouq@usmba.ac.ma"},
    {"cne": "N135277218", "cin": "CD784545", "email": "youssef.achbar@usmba.ac.ma"},
    {"cne": "S133260695", "cin": "ZT315416", "email": "reda.alalach@usmba.ac.ma"},
    {"cne": "S147054072", "cin": "CD965404", "email": "chadia.alami@usmba.ac.ma"},
    {"cne": "N148065379", "cin": "CD965559", "email": "adam.anouar@usmba.ac.ma"},
    {"cne": "N130042376", "cin": "CD787319", "email": "mohamed.belfakih@usmba.ac.ma"},
    {"cne": "N139362813", "cin": "CD619128", "email": "ghita.bouanane@usmba.ac.ma"},
    {"cne": "N136036981", "cin": "CD445648", "email": "ahmed.bourqia@usmba.ac.ma"},
    {"cne": "N134376647", "cin": "CD446587", "email": "sara.chakir@usmba.ac.ma"},
    {"cne": "N139081707", "cin": "CD797809", "email": "hajar.charbak@usmba.ac.ma"},
    {"cne": "N136032694", "cin": "CD960773", "email": "ali.chliyah@usmba.ac.ma"},
    {"cne": "N120081254", "cin": "CD499476", "email": "youness.chouika@usmba.ac.ma"},
    {"cne": "N133372735", "cin": "CD359184", "email": "mohammed.dani@usmba.ac.ma"},
    {"cne": "S132057001", "cin": "Z663740", "email": "saida.dine@usmba.ac.ma"},
    {"cne": "USMBA22130", "cin": "A03209892", "email": "khoudiedji.drame@usmba.ac.ma"},
    {"cne": "S133294504", "cin": "ZT350799", "email": "nabila.echriti@usmba.ac.ma"},
    {"cne": "N130005118", "cin": "ZT350799", "email": "radouane.eddaouy@usmba.ac.ma"},
    {"cne": "N143058131", "cin": "CD618446", "email": "nada.elbakhiri@usmba.ac.ma"},
    {"cne": "N139102630", "cin": "CN60604", "email": "mouslime.elbouknify@usmba.ac.ma"},
    {"cne": "N135189887", "cin": "CD244674", "email": "widad.elbourkadi@usmba.ac.ma"},
    {"cne": "N120079068", "cin": "CD629810", "email": "nada.elfarssi@usmba.ac.ma"},
    {"cne": "N145042260", "cin": "CD959659", "email": "yassine.elgadi@usmba.ac.ma"},
    {"cne": "N140027001", "cin": "CD959659", "email": "sara.elhadrachi@usmba.ac.ma"},
    {"cne": "S135231117", "cin": "ZH8356", "email": "wiam.elhaigoun@usmba.ac.ma"},
    {"cne": "S132092726", "cin": "RC54903", "email": "mohamed.elhaik@usmba.ac.ma"},
    {"cne": "N120048222", "cin": "CD167953", "email": "houria.elhayani@usmba.ac.ma"},
    {"cne": "S134270394", "cin": "ZT327407", "email": "hicham.elkhamlichi@usmba.ac.ma"},
    {"cne": "N136360011", "cin": "CD927638", "email": "ilyas.elmaqhor@usmba.ac.ma"},
    {"cne": "N120007192", "cin": "CD707308", "email": "hafsa.elmeskin@usmba.ac.ma"},
    {"cne": "N133089257", "cin": "CD669870", "email": "oumayma.elmeskini@usmba.ac.ma"},
    {"cne": "N133144834", "cin": "CD669870", "email": "ikram.elmghari@usmba.ac.ma"},
    {"cne": "N137064393", "cin": "CN59429", "email": "hamza.elomari@usmba.ac.ma"},
    {"cne": "N147010242", "cin": "CD617806", "email": "abderrahmane.elqayedy@usmba.ac.ma"},
    {"cne": "N141068837", "cin": "CD617806", "email": "mohamed.elyousfi@usmba.ac.ma"},
    {"cne": "N134283830", "cin": "CD617806", "email": "youssef.elaji@usmba.ac.ma"},
    {"cne": "S148043113", "cin": "ZT318989", "email": "abdelhakim.elasfar@usmba.ac.ma"},
    {"cne": "S131359101", "cin": "ZT327449", "email": "omar.elbransi@usmba.ac.ma"},
    {"cne": "N134248320", "cin": "ZT327449", "email": "hamza.elouazzani@usmba.ac.ma"},
    {"cne": "N149023122", "cin": "CD960484", "email": "abdelmonim.elqoraychy@usmba.ac.ma"},
    {"cne": "N138064466", "cin": "CD960484", "email": "imane.essalmi@usmba.ac.ma"},
    {"cne": "N120061774", "cin": "CD749318", "email": "adil.fadloullah@usmba.ac.ma"},
    {"cne": "N139360105", "cin": "CD793222", "email": "amina.fouass@usmba.ac.ma"},
    {"cne": "USMBA22040", "cin": "CD793222", "email": "saifalislam.hamanibourema@usmba.ac.ma"},
    {"cne": "S148034747", "cin": "CD799871", "email": "bilal.hanini@usmba.ac.ma"},
    {"cne": "N142066015", "cin": "CD757534", "email": "hibatallah.hassani@usmba.ac.ma"},
    {"cne": "S130200657", "cin": "CD757534", "email": "mohamed.hmamouchi@usmba.ac.ma"},
    {"cne": "N133359687", "cin": "CD960601", "email": "aya.hommani@usmba.ac.ma"},
    {"cne": "N131312492", "cin": "CD787216", "email": "badreddine.issaouballah@usmba.ac.ma"},
    {"cne": "S135194496", "cin": "ZT327304", "email": "anoir.jgouta@usmba.ac.ma"},
    {"cne": "S139297392", "cin": "ZT317159", "email": "sabir.kaddouri@usmba.ac.ma"},
    {"cne": "N135362922", "cin": "CD958515", "email": "imane.kassimi@usmba.ac.ma"},
    {"cne": "USMBA22030", "cin": "CD958515", "email": "aboubacar.keita@usmba.ac.ma"},
    {"cne": "N134112058", "cin": "CD447138", "email": "omar.lebrimchi@usmba.ac.ma"},
    {"cne": "N130206596", "cin": "CD356623", "email": "fatimazahrae.maghraoui@usmba.ac.ma"},
    {"cne": "N131086085", "cin": "CD356623", "email": "ihssane.maghraoui@usmba.ac.ma"},
    {"cne": "N138126200", "cin": "CD706649", "email": "wissal.magouri@usmba.ac.ma"},
    {"cne": "N147022667", "cin": "CD797707", "email": "souad.mamouni@usmba.ac.ma"},
    {"cne": "N134380780", "cin": "CD935079", "email": "saad.mouncif@usmba.ac.ma"},
    {"cne": "F110037827", "cin": "W463362", "email": "khaoula.najjari@usmba.ac.ma"},
    {"cne": "N120012429", "cin": "CD967761", "email": "hajar.nhily@usmba.ac.ma"},
    {"cne": "N145039437", "cin": "CD963251", "email": "ghita.niame@usmba.ac.ma"},
    {"cne": "N133200547", "cin": "CD457574", "email": "ibtissam.ouardi@usmba.ac.ma"},
    {"cne": "N148039813", "cin": "CD796644", "email": "brahim.salih@usmba.ac.ma"},
    {"cne": "USMBA22111", "cin": "G3465698", "email": "mohammed.salisu@usmba.ac.ma"},
    {"cne": "USMBA22015", "cin": "RZ9491915", "email": "hassanabdelaziz.sanoussi@usmba.ac.ma"},
    {"cne": "USMBA22168", "cin": "B02617548", "email": "yacine.sidahmedely@usmba.ac.ma"},
    {"cne": "N120004911", "cin": "CD793514", "email": "marouane.souabni@usmba.ac.ma"},
    {"cne": "N142031896", "cin": "CD792255", "email": "mehdi.tazihnyine@usmba.ac.ma"},
    {"cne": "USMBA23156", "cin": "EB749787", "email": "yendouboamelouise.yentchabre@usmba.ac.ma"},
    {"cne": "N146040910", "cin": "CD443669", "email": "chaymae.zabraoui@usmba.ac.ma"},
    {"cne": "N146055848", "cin": "CD443669", "email": "mohammed.zaim@usmba.ac.ma"},
    {"cne": "N120054379", "cin": "CD968646", "email": "abdelhamid.zdih@usmba.ac.ma"},
]

def login(session, cne, cin):
    r = session.get(LOGIN_URL, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    token_el = soup.find('input', {'name': '_token'})
    if not token_el:
        return False
    token = token_el['value']
    r2 = session.post(LOGIN_URL, data={
        '_token': token,
        'email': cne,
        'password': cin,
        'remember': 'on'
    }, allow_redirects=True, timeout=15)
    return 'logout' in r2.text or 'Student' in r2.url

def get_student_name(session):
    r = session.get(NOTES_URL, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    dropdown = soup.select_one('li.dropdown a.dropdown-toggle')
    if dropdown:
        return dropdown.get_text(strip=True).replace('▼','').strip()
    return ""

def get_notes(session):
    r = session.get(NOTES_URL, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    notes = []
    for row in soup.select('table tbody tr'):
        cols = row.select('td')
        if len(cols) >= 3:
            etat_tag = cols[3].find('span') if len(cols) > 3 else None
            notes.append({
                "module": cols[0].get_text(strip=True),
                "semestre": cols[1].get_text(strip=True),
                "moyenne": cols[2].get_text(strip=True),
                "etat": etat_tag.get_text(strip=True) if etat_tag else ''
            })
    return notes

def scrape_all():
    results = []
    total = len(students)
    for i, student in enumerate(students):
        cne, cin, email = student['cne'], student['cin'], student['email']
        if cin == "N/A":
            print(f"[{i+1}/{total}] SKIP {cne} - no CIN")
            continue
        session = requests.Session()
        session.headers.update(HEADERS)
        try:
            if not login(session, cne, cin):
                print(f"[{i+1}/{total}] FAIL {cne}")
                results.append({"cne": cne, "cin": cin, "email": email, "nom": "", "photo": f"{BASE_URL}/Docs/Students/Cartes/2022/{cne}.jpg", "notes": [], "error": "login_failed"})
            else:
                nom = get_student_name(session)
                notes = get_notes(session)
                print(f"[{i+1}/{total}] OK {cne} - {nom} - {len(notes)} notes")
                results.append({"cne": cne, "cin": cin, "email": email, "nom": nom, "photo": f"{BASE_URL}/Docs/Students/Cartes/2022/{cne}.jpg", "notes": notes})
                session.get(f"{BASE_URL}/Student/logout", timeout=10)
        except Exception as e:
            print(f"[{i+1}/{total}] ERROR {cne}: {e}")
            results.append({"cne": cne, "cin": cin, "email": email, "nom": "", "photo": f"{BASE_URL}/Docs/Students/Cartes/2022/{cne}.jpg", "notes": [], "error": str(e)})
        time.sleep(1.5)

    with open("students_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Done! {len(results)} students saved to students_data.json")

if __name__ == "__main__":
    scrape_all()
