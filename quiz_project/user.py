import json

class User:
    def __init__(self, fichier):
        self.fichier = fichier
        self.scores = self.charger_scores()

    def charger_scores(self): # charge les scores depuis un fichier JSON
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def enregistrer_score(self, score):
        nom = input("Entrez votre nom : ").strip()
        if nom:
            self.scores[nom] = self.scores.get(nom, []) + [score]
            with open(self.fichier, "w", encoding="utf-8") as f:
                json.dump(self.scores, f, indent=4)
            print("Score enregistré !")

    def afficher_scores(self):
        print("\n=== Scores ===")
        for nom, scores in self.scores.items():
            print(f"{nom}: {scores}")
