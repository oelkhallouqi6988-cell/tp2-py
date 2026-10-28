
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        if solde_initial < 0:
            raise ValueError("Le solde initial ne peut pas être négatif.")

        self._titulaire = titulaire
        self.__solde = solde_initial
        self._operations = []

    def deposer(self, montant):
        if montant <= 0:
            print("Montant invalide : le dépôt doit être positif.")
            return

        self.__solde += montant
        self._operations.append(f"Dépôt : +{montant} €")

    def retirer(self, montant):
        if montant <= 0:
            print("Le montant doit être positif.")
            return

        if montant > self.__solde:
            print("Fonds insuffisants.")
            return

        self.__solde -= montant
        self._operations.append(f"Retrait : -{montant} €")

    @property
    def solde(self):
        return self.__solde

    @property
    def operations(self):
        return self._operations.copy()

    def __str__(self):
        return (
            f"Titulaire : {self._titulaire}, "
            f"Solde : {self.solde} €"
        )


class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0,
                 taux_interet=0.03):
        super().__init__(titulaire, solde_initial)

        if taux_interet < 0:
            raise ValueError("Le taux ne peut pas être négatif.")

        self.__taux_interet = taux_interet

    def calculer_interet(self):
        interet = self.solde * self.__taux_interet
        self.deposer(interet)
        return interet


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)

    compte.deposer(200)
    compte.retirer(150)

    print(compte)
    print("Solde accessible :", compte.solde, "€")
    print("Historique :", compte.operations)

    # Tentative de modification directe du solde
    try:
        compte.solde = 500
    except AttributeError as erreur:
        print("Erreur :", erreur)

    # Test du compte épargne
    epargne = CompteEpargne("Sara", 2000, 0.05)
    interet = epargne.calculer_interet()

    print(f"Intérêts calculés : {interet:.2f} €")
    print(epargne)
