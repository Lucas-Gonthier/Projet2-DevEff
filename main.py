import operator

# ==================================================================
# ============================= DATA IN ============================
# ==================================================================

def GetCalcul():
    """
    Demande à l'utilisateur d'entrer un calcul mathématique séparé par des espaces.

    Returns:
        list: Une liste d'éléments résultante après le traitement par SplitCalcul.
    """
    calcul = str(input("Entrez un calcul (séparer les éléments par des espaces): "))
    return SplitCalcul(calcul)


def SplitCalcul(calcul):
    """
    Prend une chaîne de caractères représentant un calcul mathématique, la divise en une
    liste d'éléments, et la renvoie.

    Args:
        calcul (str): La chaîne de caractères représentant le calcul.

    Returns:
        list: Une liste d'éléments résultante du découpage.
    """
    liste = calcul.split(" ")
    return liste


def CheckErrors(liste):
    """
    Vérifie s'il y a des erreurs dans la liste d'éléments et retourne 0 en cas d'erreurs,
    sinon retourne 1.

    Args:
        liste (list): La liste d'éléments à vérifier.

    Returns:
        int: 0 en cas d'erreurs, 1 sinon.
    """
    if ErrorSizeStart(liste) == 0:
        return 0
    if ErrorType(liste) == 0:
        return 0
    return 1


def ErrorType(liste):
    """
    Vérifie si les éléments de la liste sont des nombres ou des opérateurs valides,
    retourne 0 et affiche un message d'erreur en cas d'élément invalide, sinon appelle
    ErrorOperandeOperateur et retourne son résultat.

    Args:
        liste (list): La liste d'éléments à vérifier.

    Returns:
        int: 0 en cas d'erreur, le résultat de ErrorOperandeOperateur sinon.
    """
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
    return ErrorOperandeOperateur(ComptOperande, ComptOperateur)


def ErrorSizeStart(liste):
    """
    Vérifie si la taille de la liste est appropriée et si les deux premiers éléments ne sont
    pas des opérateurs, retourne 0 et affiche un message d'erreur si les conditions ne sont pas
    remplies, sinon retourne 1.

    Args:
        liste (list): La liste d'éléments à vérifier.

    Returns:
        int: 0 en cas d'erreurs, 1 sinon.
    """
    if len(liste) < 3:
        print("Erreur: il faut au moins 3 éléments.")
        return 0
    if liste[0] in ("+", "-", "*", "/") or liste[1] in ("+", "-", "*", "/"):
        print("Erreur: les 2 premiers éléments ne peuvent pas être des opérateurs.")
        return 0
    return 1


def ErrorOperandeOperateur(ComptOperande, ComptOperateur):
    """
    Vérifie si le nombre d'opérandes et d'opérateurs dans la liste de calcul correspond à une
    expression mathématique valide, retourne 0 et affiche un message d'erreur si les conditions
    ne sont pas remplies, sinon retourne 1.

    Args:
        ComptOperande (int): Le nombre d'opérandes dans la liste.
        ComptOperateur (int): Le nombre d'opérateurs dans la liste.

    Returns:
        int: 0 en cas d'erreur, 1 sinon.
    """
    if ComptOperande != ComptOperateur + 1:
        print("Erreur: le nombre d'opérandes et d'opérateurs ne correspond pas.")
        return 0
    return 1


# ==================================================================
# =========================== DATA PROCESS =========================
# ==================================================================

def IsOperator(element):
    """
    Vérifie si l'élément donné est un opérateur mathématique (+, -, *, /),
    retourne True s'il l'est, sinon retourne False.

    Args:
        element (str): L'élément à vérifier.

    Returns:
        bool: True si l'élément est un opérateur, False sinon.
    """
    if element in ("+", "-", "*", "/"):
        return True
    return False


def DoCalcul(liste):
    """
    Effectue le calcul mathématique en se basant sur la liste d'éléments,
    utilise les opérateurs définis dans le dictionnaire ops, et retourne le résultat final.

    Args:
        liste (list): La liste d'éléments représentant le calcul.

    Returns:
        list: La liste résultante après les étapes de calcul.
    """
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
    """
    Affiche l'état actuel de la liste pendant le processus de calcul étape par étape.

    Args:
        liste (list): La liste d'éléments à afficher.
    """
    for element in liste:
        print(element, end=" ")
    print()


def DisplayMenu(choix=0):
    """
    Affiche un menu permettant à l'utilisateur d'entrer un calcul ou de quitter.
    Continue de demander à l'utilisateur jusqu'à ce que l'option de sortie soit sélectionnée.

    Args:
        choix (int): Le choix de l'utilisateur.
    """
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
