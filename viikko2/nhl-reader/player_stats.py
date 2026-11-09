class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        nationality_players = []

        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)

        nationality_players.sort(
            key=lambda player: player.goals + player.assists,
            reverse=True
        )

        return nationality_players