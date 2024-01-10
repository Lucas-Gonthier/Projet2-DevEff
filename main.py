# ==================================================================
# ============================= DATA IN ============================
# ==================================================================

def GetCalcul():
    calcul = str(input("Entrez un calcul (séparer les éléments par des espaces): "))
    return SplitCalcul(calcul)

def SplitCalcul(calcul):
    liste = calcul.split(" ")
    return liste

def CheckErrors(liste):
    if ErrorSizeStart(liste) == 0:
        return 0
    if ErrorType(liste) == 0:
        return 0
    return 1

def ErrorType(liste):
    ComptOperande = 0
    ComptOperateur = 0
    for element in liste:
        if element.isdigit():
            ComptOperande += 1
        elif element in ("+", "-", "*", "/"):
            ComptOperateur += 1
        else:
            print("Erreur: un des éléments n'est pas un nombre ou un opérateur.")
            return 0
    return ErrorOperandeOperateur(liste, ComptOperande, ComptOperateur)

def ErrorSizeStart(liste):
    if len(liste) < 3:
        print("Erreur: il faut au moins 3 éléments.")
        return 0
    if liste[0] in ("+", "-", "*", "/") or liste[1] in ("+", "-", "*", "/"):
        print("Erreur: les 2 premiers éléments ne peuvent pas être des opérateurs.")
        return 0
    return 1

def ErrorOperandeOperateur(ComptOperande, ComptOperateur):
    if ComptOperande != ComptOperateur + 1:
        print("Erreur: le nombre d'opérandes et d'opérateurs ne correspond pas.")
        return 0
    return 1

# ==================================================================
# =========================== DATA PROCESS =========================
# ==================================================================

def IsOperator(element):
    if element in ("+", "-", "*", "/"):
        return True
    return False

def DoCalcul(liste):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    while len(liste) > 1:
        for element in liste:
            if IsOperator(element):
                index = liste.index(element)
                resultat = ops[element](int(liste[index - 2]), int(liste[index - 1]))
                liste[index - 2] = str(resultat)
                del liste[index - 1]
                del liste[index - 1]
                PrintStep(liste)
    return liste

def PrintStep(liste):
    for element in liste:
        print(element, end=" ")
    print()

def DisplayMenu(choix = 0):
    while choix != 2:
        choix = int(input("1. Entrer un calcul\n" + "2. Quitter\n" + "Votre choix: "))
        if choix == 1:
            Calcul = GetCalcul()
            while CheckErrors(Calcul) == 0:
                Calcul = GetCalcul()
            DoCalcul(Calcul)
        elif choix == 2:
            break
        else:
            print("Erreur: votre choix n'est pas valide.")

DisplayMenu()
