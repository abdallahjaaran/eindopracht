# Add your Python code here. E.g.
from microbit import *


import time


class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    

def start():
    print(style.WHITE + 'Jaar: 2005\nLand: Lebanon\nNaam: Mohammad\nLeeftijd: 20 jaar oud.')
    sleep(2000)
    print(style.BLUE + 'Je bent Mohammad in dit verhaal.')
    sleep(2000)
    print(style.YELLOW + 'Je bent een hardwerkende jongen man. Die moeilijk een toekomst kan vinden in Lebanon.')
    print(style.YELLOW + 'Het verschil tussen rijk en arm is groot en als je in een arme famillie geboren bent.')
    print(style.YELLOW + 'Is het moeilijk om naar de rijke kant te gaan.')
    print(style.YELLOW + 'Omdat je zo arm bent heb je eten en geld gestolen van rijke mensen')
    print(style.YELLOW + 'Ze hebben de politie ingeschakeld.')
    sleep(10000)
    stuk1_1()


def stuk1_1():
    print(style.WHITE + 'Je loopt op straat in lebenon, twee agenten zien je wat doe je?')
    sleep(5000)
    print(style.MAGENTA + 'A: Je drijt je om en loopt rustig weg')
    print(style.MAGENTA + 'B: Je begroet de agenten en doet jezelf voor als een ander persoon')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je bent ontkomen van de agenten')
            stuk1_goed()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'De agenten hebben je door')
            stuk1_fout()
            break

def stuk1_fout():
    print(style.WHITE + 'De agenten gaan je nu aresteren. Wat ga je doen?')
    sleep(5000)
    print(style.MAGENTA + 'A: Je gaat het gevecht met ze aan.')
    print(style.MAGENTA + 'B: Je probeerd te ontsnappen.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je bent ontsnapt')
            stuk1_middengoed()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Ze hebben je opgepakt en je hebt de dood straf gekregen.')
            break
        
def stuk1_goed():
    print(style.WHITE + 'Je wilt vluchten uit Lebanon. Je loopt nu richting je huis, onderweg zie je twee vrienden groepen.') 
    print(style.WHITE + 'De eerste groep zijn echte goede vrienden van je mij ze zijn niet zo sterk of slim als de tweede groep.') 
    print(style.WHITE + 'De tweede groep is redelijk te vertrouwen maar dus niet zo goed als de eerste vrienden groep.') 
    print(style.WHITE + 'Je gaat ze om hulp vragen maar je kan maar een vrienden groep meenemen.') 
    print(style.WHITE + 'Want anders wordt het teveel en heb je meer kans dat je gepakt wordt.')
    sleep(5000)
    print(style.MAGENTA + 'A: Eerste vrienden groep.')
    print(style.MAGENTA + 'B: Tweede vrienden groep.')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt de goede keuze gemaakt. Want vertrouwen is belangrijk.')
            stuk1_2goed()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Nu ga je vluchten met vrienden die misschien achterbaks zijn.')
            stuk1_2slecht()
            break
            
            
def stuk1_middengoed():
    print(style.WHITE + 'Je bent dus ontsnapt. Je moet nu onderschuilen voor de agenten die je hebben gezien')
    print(style.WHITE + 'Je kan onderschuilen bij twee vrienden groepen. De eerste vrienden groep zijn je echte goede vrienden.')
    print(style.WHITE + 'Maar ze zijn niet zo sterk of slim als de tweede groep.')
    print(style.WHITE + 'De tweede groep is redelijk te vertrouwen maar dus niet zo goed als de eerste vrienden groep')
    sleep(5000)
    print(style.MAGENTA + 'A: Eerste vrienden groep')
    print(style.MAGENTA + 'B: Tweede vrienden groep')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt deking gezocht bij de goede vrienden je besluit met hun te vluchten naar Nederland.')
            stuk1_2goed()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je zochenaamde vrienden gaan je dwingen om te vluchten en zo het risco te nemen dat je alles verliest.')
            stuk1_2slecht()
            break
        
        
def stuk1_2goed():
    print(style.WHITE + 'Met je vrienden ga je nu beslissen wat jullie volgende stap is.')
    sleep(5000)
    print(style.MAGENTA + 'A: Jullie pakken de auto.')
    print(style.MAGENTA + 'B: Jullie gaan met de voet.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Met je vrienden probeer je nu naar Jordanië te gaan naar het vliegveld van Amman.')
            stuk1_dereisgoed()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Jullie gaan proberen naar de dichtbijzijndse vliegveld in Lebanon te gaan.')
            stuk1_dereisslecht()
            break


def stuk1_2slecht():
    print(style.WHITE + 'Ze gaan nu beslissen wat de volgende stap is. Jij hebt er een woord in wat gaan jullie doen?')
    sleep(5000)
    print(style.MAGENTA + 'A: Jullie gaan lopend.')
    print(style.MAGENTA + 'B: Jullie gaan met de auto')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je gaat nu proberen om naar Jordanië te gaan. Je wilt het vliegveld van Amman halen.')
            stuk1_dereisgoed()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je gaat nu proberen om naar de dichtsbijzijndse vliegveld van Lebanon te gaan.')
            stuk1_dereisslecht()
            break


def stuk1_dereisgoed():
    print(style.WHITE + 'Jullie moeten een auto kiezen, je hebt een opvallende auto maar hij is wel snel.\n Of je kunt kiezen voor een slomme onopvallende auto.')
    sleep(5000)
    print(style.MAGENTA + 'A: Onopvallende auto')
    print(style.MAGENTA + 'B: Opvallende auto')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt een slomme oponvallende auto gekozen je kunt makkelijk naar Amman toe zonder dat je opvalt.')
            stuk1_aankomstvliegveld()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt voor de snelle opvallende auto gekozen. Niet alleen is die opvallend maar ook snel.\n Wat hem meer opvallend maakt.')
            stuk1_dereismiddengoedauto()
            break
        

def stuk1_dereisslecht():
    print(style.WHITE + 'Je moet nu kiezen hoe je gaat lopen, pak je de snelle maar opvallende weg. Of de slomme maar onopvallende weg.')
    sleep(5000)
    print(style.MAGENTA + 'A: Onpvallende weg')
    print(style.MAGENTA + 'B: Opvallende weg')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt gekozen voor de slomme maar onopvallende weg. Je kan makkelijk naar het vliegveld komen.\n Zonder dat je opgemerkt wordt.')
            stuk1_aankomstvliegveld()
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt gekozen voor de opvallende weg. Je kan er moeilijk doorheen want veel agenten lopen door deze weg heen.')
            stuk1_dereismiddengoedlopend()
            break
        

def stuk1_dereismiddengoedauto():
    print(style.WHITE + 'Een agent stopt jullie auto onderweg, hij vraagt voor jullie id.')
    sleep(5000)
    print(style.MAGENTA + 'A: We rijden super hard weg')
    print(style.MAGENTA + 'B: Je doet je voor als iemand die op vakantie is en de taal niet kan spreken. ')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Het is gelukt je vrienden hebben gezegd dat je je id niet bij je hebt en dat je komt uit Turkey.')
            stuk1_aankomstvliegveldamman()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Jullie zijn super hard weg gereden de agent heeft andere agenten erbij geroepen. Jullie zijn gepakt en je hebt levenslang gekregen.')
            break

def stuk1_dereismiddengoedlopend():
    print(style.WHITE + 'Je loopt door de weg een agent stopt jullie, hij vraagt om jullie id.')
    sleep(5000)
    print(style.MAGENTA + 'A: Je rent super hard weg.')
    print(style.MAGENTA + 'B: Je doet je voor als iemand die op vakantie is gekomen en die de taal niet kan spreken.')
    while True:
        if button_b.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Het is gelukt je vrienden hebben gezegd dat je je id niet bij je hebt en dat je komt uit Turkey.')
            stuk1_aankomstvliegveldlebanon()
            break
        elif button_a.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Jullie zijn hard weg gerend voor de agent. De agent heeft andere agenten erbij geroepen. Jullie zijn gepakt en je hebt levenslang gekregen.')
            break
        
        
def stuk1_aankomstvliegveldamman():
    print(style.WHITE + 'Jullie zijn nu aangekomen bij het vliegveld van Amman. Je kan alleen niet naar Nederland vliegen maar wel naar Turkey.\n Je hebt ook de optie om met de boot te gaan.')
    sleep(5000)
    print(style.MAGENTA + 'A: Turkey')
    print(style.MAGENTA + 'B: Met de boot')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je gaat naar Turkey vliegen. De reis is lang en spanned.')
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt besloten om met de boot naar Nederland proberen te gaan.')
            break
        

def stuk1_aankomstvliegveldlebanon():
    print(style.WHITE + 'Jullie zijn nu aangekomen bij het vliegveld van Lebanon. Je hebt moeite om er doorheen te gaan. Je hebt wel een fake id')
    print(style.WHITE + 'Je kan ervoor kiezen de fake id te gebruiken of met de auto naar het vliegveld van Syrië te gaan')
    sleep(5000)
    print(style.MAGENTA + 'A: Fake id gebruiken')
    print(style.MAGENTA + 'B: Vliegveld van Syrië')
    while True:
        if button_a.is_pressed():
            display.show(Image.YES)
            sleep(3000)
            print(style.GREEN + 'Je hebt gekozen voor de slomme maar onopvallende weg. Je kan makkelijk naar het vliegveld komen.\n Zonder dat je opgemerkt wordt.')
            break
        elif button_b.is_pressed():
            display.show(Image.NO)
            sleep(3000)
            print(style.RED + 'Je hebt gekozen voor de opvallende weg. Je kan er moeilijk doorheen want veel agenten lopen door deze weg heen.')
            break
        
start()