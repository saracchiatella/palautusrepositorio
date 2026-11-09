from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table


def main():
    season = input("Season (e.g. 2024-25): ")
    nationality = input("Nationality (e.g. FIN): ").upper()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Players from {nationality}")

    table.add_column("Name")
    table.add_column("Team")
    table.add_column("Goals", justify="right")
    table.add_column("Assists", justify="right")
    table.add_column("Points", justify="right")

    for player in players:
        points = player.goals + player.assists

        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points)
        )

    console = Console()
    console.print(table)


if __name__ == "__main__":
    main()
