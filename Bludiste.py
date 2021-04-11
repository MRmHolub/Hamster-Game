import copy
import time
import math

def odstran_n(veta:str):
    return veta.replace("\n","")


def cesta_k_portalu(krecci,MAZE,portal,bludiste_y,bludiste_x):
    krecci_2=krecci
    pracovni_krecek_index_patro = min(krecci_2.keys())  #
    pracovni_krecek_souradnice = krecci_2[pracovni_krecek_index_patro]
    _maze_=MAZE[pracovni_krecek_index_patro]
    _portal_=portal[pracovni_krecek_index_patro]
    print(_maze_,_portal_,pracovni_krecek_souradnice)

    nasel=False
    if pracovni_krecek_souradnice in _portal_:
        nasel = True
        print(f"Křeček na portalu {pracovni_krecek_souradnice} sedel od zacatku")
    CESTA = [(pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1])]
    _maze_.remove((pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1])) # odstraní z _maze_ pozici kde se nachazi krecek

    while nasel==False:
        print("Jedu nové kolo a maze je",_maze_)
        print("Pred zmenou je krecek", pracovni_krecek_souradnice)
        if (pracovni_krecek_souradnice[0]>0) and ((pracovni_krecek_souradnice[0]-1,pracovni_krecek_souradnice[1]) in _maze_):
                _maze_.remove((pracovni_krecek_souradnice[0] - 1, pracovni_krecek_souradnice[1]))
                CESTA += [(pracovni_krecek_souradnice[0] - 1, pracovni_krecek_souradnice[1])]
                pracovni_krecek_souradnice = (pracovni_krecek_souradnice[0] - 1, pracovni_krecek_souradnice[1])
                print("Jdeme nahoru", CESTA, "Křeček se nyní nachází v", pracovni_krecek_souradnice)

        elif (pracovni_krecek_souradnice[1]<(bludiste_x-1)) and ((pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1]+1) in _maze_):
                _maze_.remove((pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1] + 1))
                CESTA += [(pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1]+1)]
                pracovni_krecek_souradnice = (pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1]+1)
                print("Jdeme doprava", CESTA, "Křeček se nyní nachází v", pracovni_krecek_souradnice)


        elif (pracovni_krecek_souradnice[0] < (bludiste_y-1)) and (pracovni_krecek_souradnice[0] + 1, pracovni_krecek_souradnice[1]) in _maze_:
                _maze_.remove((pracovni_krecek_souradnice[0] + 1, pracovni_krecek_souradnice[1]))
                CESTA += [(pracovni_krecek_souradnice[0] + 1, pracovni_krecek_souradnice[1])]
                pracovni_krecek_souradnice = (pracovni_krecek_souradnice[0] + 1, pracovni_krecek_souradnice[1])
                print("Jdeme dolů", CESTA, "Křeček se nyní nachází v", pracovni_krecek_souradnice)


        elif (pracovni_krecek_souradnice[1]>0) and ((pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1]-1) in _maze_):
                _maze_.remove((pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1] - 1))
                print("Pred zmenou je krecek", pracovni_krecek_souradnice)
                CESTA += [(pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1]-1)]
                pracovni_krecek_souradnice = (pracovni_krecek_souradnice[0], pracovni_krecek_souradnice[1]-1)
                print("Jdeme doleva", CESTA, "Křeček se nyní nachází v", pracovni_krecek_souradnice)



        print("Momentalni ujita cesta je ",CESTA)
        for p in _portal_:
            if p in CESTA:
                nasel=True
                print(f"Cesta k portalu {p} je {CESTA}")
                break




def vytvor_patra(indexy_pater_sestupne,y,znaky):
    bludiste, i = {}, 0
    for index_ve_znaku in indexy_pater_sestupne:
        blok_patra=[]
        for radek in range(0,y):
            znaky[int(index_ve_znaku)*y+radek]=odstran_n(znaky[int(index_ve_znaku)*y+radek])
            blok_patra+=[znaky[int(index_ve_znaku)*y+radek]]
        bludiste[i]=blok_patra
        i+=1
    return bludiste

def rozrazeni_portalu(v,pocet_schodist):
    # vytvarime dict schodiste do ktereho davame souradnice schodiste jako hodnotu ve tvaru (y,x)a cislo schodiste jako klic
    vchod_na_schodiste, i_x, i_y, promenna = {}, [], [], []
    for jty_schod in range(pocet_schodist):
        schod = odstran_n(v.readline())
        schod = schod.split(" ")
        # prvni hodnota v danem listu udava pocet dvojic nachazejicich se v danem podlazi, zaciname od nejvyssiho podlazi
        promenna = []
        for pocet_hvezdicek_podlazi in range(1, int(schod[0]) * 2, 2):

            i_y = int(schod[pocet_hvezdicek_podlazi])
            i_x = int(schod[pocet_hvezdicek_podlazi + 1])
            promenna += [(i_y, i_x)]
        vchod_na_schodiste[jty_schod] = promenna
    return vchod_na_schodiste

def krecci_souradnice(krecek,indexy_pater_sestupne):
    vysledek, pravdive_pozice_pater, promenna = {}, [], []
    for krecci_podlazi in range(0, len(krecek), 3):
        pravdive_pozice_pater += [indexy_pater_sestupne.index(krecek[krecci_podlazi])]
        i_y = int(krecek[krecci_podlazi + 1])
        i_x = int(krecek[krecci_podlazi + 2])
        promenna += [(i_y, i_x)]
    for ppx in enumerate(promenna):
        if pravdive_pozice_pater[ppx[0]] in vysledek:
            vysledek[pravdive_pozice_pater[ppx[0]]] = (vysledek[pravdive_pozice_pater[ppx[0]]]) ,(ppx[1])
        else:
            vysledek[pravdive_pozice_pater[ppx[0]]]=(ppx[1])
    return vysledek


def make_MAZE(pocet_pater_bludiste,bludiste_y,bludiste_x,bludiste_usp,krecci):
        MAZE = {}
        krecek_patro_max = max(krecci.keys()) #je zbytecne vytvaret bludiste patra vyssiho nez je index nejvyssiho krecka
        for papapapatro in range(krecek_patro_max):
            list_maze = []
            for cislo_radku in range(0, bludiste_y):
                for index_znaku_radku in range(0, bludiste_x):
                    if bludiste_usp[papapapatro][cislo_radku][index_znaku_radku] == ".":
                        list_maze += [(cislo_radku, index_znaku_radku)]
            MAZE[papapapatro] = list_maze
        return MAZE


def kombinator_portalu(portal,krecci):
    patro_nejnizsiho_krecka=max(krecci.keys())
    portal_p = copy.deepcopy(portal)
    sub_combi, combi, = [], []
    ppp = len(portal.keys())
    loop_promena = True
    vyhozeno, vyhozeno_2 = {}, []
    while loop_promena:
        for konst in range(ppp):
            # print("KONST JE",konst) #iteruju skrze každé patro

            sub_combi += [portal_p[konst][0]]  # dodam prvni hodnotu z kazdeho patra
            # print("SUBKombi je",sub_combi)
        combi += [sub_combi]  # predam do hlavni promene kombinaci
        sub_combi = []  # vynuluju sub promenou
        vyhozeno_2 += [portal_p[ppp - 1].pop(0)]  # vyhodim nejmensi nejmensi
        # print("Kombi je",combi,"Portal je",portal_p,"Mezi vyhozene je",vyhozeno_2,"Portal puvodni",portal)

        for xxxxx in range(ppp - 1, 0, -1):
            if len(portal_p[xxxxx]) < 1:
                #print(f"Právě se chystám odsunout první hodnotu z {portal_p[xxxxx - 1]} protoze portal {xxxxx} je prazdny{portal_p[xxxxx]}")
                portal_p[xxxxx - 1].pop(0)
                      # pokud je dané patro vyprázdněné vyhodime prvni hodnotu z patra o jedno vyssiho
                portal_p[xxxxx] += portal[xxxxx]
                #print("Odted pracuji s timto dictem portalu", portal_p, "Normalni portal", portal)
                # zacinam od indexu nula, takze pokud vypotrebuji nizssi portal, odstrani to hodnotu z toho co je od jedno výš, ano ale když chci odstranit z njevyssiho portalu

        if len(portal_p[0]) < 1:
            loop_promena = False
    return combi

def __m__():
    v = open("inp.txt", "r")  # sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    bludiste = v.readline()
    bludiste = bludiste.split(" ")
    pocet_uloh = int(bludiste[0])
    pocet_pater_input = int(bludiste[1])  # puvodni, pro vypocet readlinu
    bludiste_y = int(bludiste[2])  # y rozmer podlazi
    bludiste_x = int(odstran_n(bludiste[3]))  # x rozmer podlazi

    znaky = v.readlines((
                                    bludiste_x + 1) * bludiste_y * pocet_pater_input - 1)  # Seznam teček a hastagu, nesmime zapomenout na to že "\n" zabira v pameti taky misto
    pocet_pater_bludiste = int(odstran_n(v.readline()))  # počet pater s kterymi doopravdy pracujeme
    #print(f"Počet úloh:{pocet_uloh} Dům má {pocet_pater_bludiste} pater, rozměr patra:{bludiste_y}px * {bludiste_x}px")

    indexy_pater_sestupne = v.readline()
    indexy_pater_sestupne = odstran_n(indexy_pater_sestupne)
    indexy_pater_sestupne = indexy_pater_sestupne.split(" ")  # seznam cisel urcujici poradi seznamu
    #print("Čísla pater ve správném pořadí:", indexy_pater_sestupne)

    bludiste_usp = vytvor_patra(indexy_pater_sestupne, bludiste_y, znaky)
    # mam vyrobene usporadane bludiste/patro ale
    #print(f"Nejvyssi patro {bludiste_usp[0]} má  index 0")
    # list bludiste usp je uspořádán sestupne, index 0 oznacuje nejvyssi patro, 1 potom o jedno nizsi

    pocet_portalu = int(odstran_n(v.readline()))  # pocet schodist obsahujici portal do nizsiho schodiste
    portal = rozrazeni_portalu(v, pocet_portalu)  # hvezda predstavuje portal
    #print("Portaly v nejvyssim patre najdeme na: ", portal[0])  # portal v nejvyssim patre ma index 0
    #print("Vsechny portaly:", portal)

    pocet_krecku = int(odstran_n(v.readline()))
    kr = (odstran_n(v.readline()))
    kr = kr.split(" ")  # promena kr obsahuje souradnice krecku umistenych v puvodnim sestaveni neseřazene

    if len(kr)%3!=0:
        print("Spatny input v radku krecku")
        return False

    print("Počet křečků:", pocet_krecku, "Kr je ", kr)
    krecci = krecci_souradnice(kr, indexy_pater_sestupne)  # serazene skrecky index 0 má ten co je v nejvyssim patre
    print("Krecci se spravnym indexem:", krecci)

    # 00 je vlevo nahoře!!!
    for iq, iw in enumerate(bludiste_usp):
        try:
            bludiste_usp[iw][iw] == znaky[int(indexy_pater_sestupne[iq]) * bludiste_y]
        except:
            print(
                "Zkontroluj bludiste_usp, indexy_pater_sestupne, bludiste ve vyteckovne forme(znaky) a y-rozmer bludiste(bludiste_y)")
    #print("TEST1 : Usporadane bludiste je nastavene spravne")

    MAZE=make_MAZE(pocet_pater_bludiste,bludiste_y,bludiste_x,bludiste_usp,krecci)

    print("Policka v bludisti, kudy mohou krecci chodit", MAZE)
    krecek_patro_max=max(krecci.keys())
    krecek_patro_min = min(krecci.keys())  #
    krecek_coords = krecci[krecek_patro_min]

        # nejvyssi radek ma klic nula ...  (3,1) ---> treti radek prvni sloupec
    print("Začínám krečkem v ", pocet_pater_bludiste - krecek_patro_min, " nejvyssim patre, na pozici",krecek_coords, "na indexu patra", krecek_patro_min)


    #cesta_k_portalu(krecci,MAZE,portal,bludiste_y,bludiste_x)
    print("Seznam portalu",portal)
    portal_comb=kombinator_portalu(portal,krecci)
    print("kombinace portalu",portal_comb)

    #for seznam_portalu in portal_comb:
    #    patro_index=0
    #    for portal_coords in seznam_portalu:
    #        neighbours=krecek_coords
    #        while portal_coords not in neighbours:
    #            for neighbour in neighbours:
    #                if (neighbour[0] + 1) in MAZE[patro_index]
#
    #        krecek_patro_min+=1
    #        krecek_coords=portal_coords
    #                pass

            #je zbytečné posílat křečky do patra přízemí když nejnižší křeček je např. v 5 patře, musim upravit MAZE, a kombinace portalu






    return "Hotovo"
__m__()

time.sleep(10)






