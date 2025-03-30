import json

class Thème:
    @staticmethod
    def charger_themes(fichier="data/themes.json"):
        """Charge les thèmes disponibles depuis themes.json."""
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("themes", [])  # Retourne les thèmes disponibles
        except (FileNotFoundError, json.JSONDecodeError):
            print("Erreur : Impossible de charger les thèmes.")
            return []  # Retourne une liste vide en cas d'erreur
