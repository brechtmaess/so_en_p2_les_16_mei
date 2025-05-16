from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, faculteit):
        super().__init__(naam)
        self.faculteit = faculteit

    def __str__(self):
        return f"{self.naam} (Rector: {self.faculteit})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, faculteit):
        super().__init__(kandidaat)
        self.faculteit = faculteit

    def __str__(self):
        return f"Stem op {self.kandidaat} (Rector: {self.faculteit})"
lijst_kanditaten = [
    RectorKandidaat("Jan de Vries", "Informatica"),
    RectorKandidaat("Piet   Jansen", "Wiskunde"),           
    RectorKandidaat("Klaas de Boer", "Natuurkunde"),    
]    
lijst_stemmen = [
    RectorStem(lijst_kanditaten[0], "Informatica"),
    RectorStem(lijst_kanditaten[1], "Wiskunde"),
    RectorStem(lijst_kanditaten[2], "Natuurkunde"),     
]