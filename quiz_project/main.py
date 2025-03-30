from quiz import Quiz
from user import User
from thème import Thème
import json

def charger_questions_par_theme(theme: str, fichier="data/questions.json"):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get(theme, [])  # ca retoune les quest qui correspond au theme
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erreur : Impossible de charger les questions.")
        return []

def menu():
    user = User("utilisateurs.json")
    theme_obj = Thème()  # cree l'objet pour gerer les themes
    
    while True:
        print("\n=== Menu Quiz ===")
        print("1. Jouer")
        print("2. Voir les scores")
        print("3. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            themes = theme_obj.charger_themes()
            if themes:
                print("\nSélectionnez un thème :")
                for i, theme in enumerate(themes, 1):
                    print(f"{i}. {theme}")

                try:
                    theme_choisi_index = int(input("\nVotre choix : ")) - 1
                    if 0 <= theme_choisi_index < len(themes):
                        theme_choisi = themes[theme_choisi_index]
                        print(f"\nVous avez choisi le thème : {theme_choisi}")
                        
                        questions = charger_questions_par_theme(theme_choisi)
                        if questions:
                            quiz = Quiz(questions)
                            score = quiz.jouer()
                            user.enregistrer_score(score)
                        else:
                            print("Aucune question disponible pour ce thème.")
                    else:
                        print("Choix invalide, veuillez réessayer.")
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
            else:
                print("Aucun thème disponible.")

        elif choix == "2":
            user.afficher_scores()

        elif choix == "3":
            print("À bientôt !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()