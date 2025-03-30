import json
import time

thèmes = "data/thème.json"
questions = "data/questions.json"

class Question:
    def __init__(self, texte, choix, reponse):
        self.texte = texte
        self.choix = choix
        self.reponse = reponse

    def poser(self, temps_limite):
        """Affiche la question et retourne si la réponse est correcte dans le temps imparti."""
        print("\n" + self.texte)
        for i, choix in enumerate(self.choix, 1):
            print(f"{i}. {choix}")

        start_time = time.time()
        while True:
            reponse_utilisateur = input("Votre réponse : ")
            elapsed_time = time.time() - start_time
            if elapsed_time > temps_limite:
                print("\nTemps écoulé ! Votre réponse est incorrecte.")
                return False 

            try:
                reponse_utilisateur = int(reponse_utilisateur)
                if 1 <= reponse_utilisateur <= len(self.choix):
                    return self.choix[reponse_utilisateur - 1] == self.reponse
                else:
                    print("Réponse hors choix.")
                    return False
            except ValueError:
                print("Entrée invalide, veuillez entrer un numéro.")
                return False

class Quiz:
    def __init__(self, questions, temps_limite=15):
        self.questions = [Question(q["question"], q["choix"], q["reponse"]) for q in questions]
        self.temps_limite = temps_limite  # limite de temps par question
        
    def jouer(self):
        """Lance le quiz et retourne le score final."""
        score = 0
        for question in self.questions:
            print(f"\nVous avez {self.temps_limite} secondes pour répondre.")
            if question.poser(self.temps_limite):
                print("Bonne réponse !")
                score += 1
            else:
                print("Mauvaise réponse.")
        
        print(f"\nScore final : {score}/{len(self.questions)}")
        return score

def charger_questions(fichier="data/questions.json"):
    """Charge les questions depuis un fichier JSON."""
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)["questions"]
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erreur : Impossible de charger les questions.")
        return []
