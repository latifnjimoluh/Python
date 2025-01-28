import csv
from src.tournament import Tournament

class TournamentManager:
    def __init__(self, players):
        self.tournament = Tournament(players)

    def start_tournament(self):
        """Lance le tournoi et permet à l'utilisateur de choisir de continuer ou d'arrêter après chaque tour."""
        while True:
            self.tournament.start_round()
            self.tournament.display_ranking()

            # Demande à l'utilisateur s'il veut continuer ou arrêter le tournoi
            user_choice = input("\nSouhaitez-vous continuer (C) ou arrêter (A) le tournoi ? : ").lower()
            if user_choice == "a":
                self.end_tournament()
                break

    def end_tournament(self):
        """Arrête le tournoi et sauvegarde les résultats dans un fichier CSV."""
        print("\nLe tournoi est terminé.")
        self.save_results()
        self.tournament.display_ranking()

    def save_results(self):
        """Sauvegarde les résultats du tournoi dans un fichier CSV."""
        with open('data/participants.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nom', 'Score'])
            for player in self.tournament.players:
                writer.writerow([player.name, player.score])
        print("Les résultats ont été sauvegardés dans participants.csv.")
