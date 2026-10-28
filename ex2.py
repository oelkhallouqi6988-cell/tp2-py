
class CompteBancaire:
    def __init__(self, solde_initial=0.0):
        self.__solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
        else:
            print("Fonds insuffisants ou montant invalide.")

    def get_solde(self):
        return self.__solde


class Client:
    def __init__(self, nom):
        self.nom = nom
        self.compte = CompteBancaire()

    def afficher(self):
        print(
            f"Client : {self.nom}, "
            f"Solde : {self.compte.get_solde()}€"
        )


# Exemple d'utilisation
if __name__ == "__main__":
    cli = Client("Yassir")

    cli.compte.deposer(300)
    cli.compte.retirer(50)

    cli.afficher()
