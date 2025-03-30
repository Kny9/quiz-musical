def valider_choix(choix, options):
    """Valide une entrée utilisateur."""
    try:
        choix = int(choix)
        if 1 <= choix <= options:
            return choix
    except ValueError:
        pass
    print("Entrée invalide.")
    return None
