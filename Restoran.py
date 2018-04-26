# -*- coding: utf-8 -*-

print "Dobro došli u program za upisivanje menija."
print "_________________________________________________________________________________"

meni = {}

while True:
    jelo_ime = raw_input("Molimo Vas upišite ime jela: ")
    jelo_cijena = raw_input("Upišite cijenu za '%s': " % jelo_ime)
    #jelo_cijena = float(raw_input("Upišite cijenu za '%s': " % jelo_ime))
    meni[jelo_ime] = jelo_cijena

    new = raw_input("Da li želite upisati novo jelo? (da/ne) ")

    if new.lower() == "ne":
        break

print "Meni: %s" % meni

with open("meni.txt", "w+") as meni_file:  # otvara datoteku i piše unutra
    for jelo in meni:
        meni_file.write("%s, %s EUR\n" % (jelo, meni[jelo]))  # piše i dodaje novi red

print "Hvala Vam!"
print "Do sljedećeg upisivanja.. Doviđenja!!"