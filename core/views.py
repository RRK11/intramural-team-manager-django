from django.shortcuts import render
from django.db.models import Count, Q
from .models import Team, Player, TeamPlayer, Game


def home(request):
    total_players = Player.objects.count()
    total_teams = Team.objects.count()
    total_roster_assignments = TeamPlayer.objects.count()
    total_games = Game.objects.count()

    recent_games = Game.objects.select_related("team").order_by("-game_date")[:5]

    teams = Team.objects.annotate(
        total_games=Count("games", filter=Q(games__result__in=["Win", "Loss", "Tie"])),
        wins=Count("games", filter=Q(games__result="Win"))
    ).order_by("team_name")

    team_stats = []
    for team in teams:
        if team.total_games > 0:
            win_percentage = round((team.wins / team.total_games) * 100, 1)
        else:
            win_percentage = 0.0

        team_stats.append({
            "team_name": team.team_name,
            "sport": team.sport,
            "wins": team.wins,
            "total_games": team.total_games,
            "win_percentage": win_percentage,
        })

    context = {
        "total_players": total_players,
        "total_teams": total_teams,
        "total_roster_assignments": total_roster_assignments,
        "total_games": total_games,
        "recent_games": recent_games,
        "team_stats": team_stats,
    }
    return render(request, "core/home.html", context)


def about(request):
    return render(request, "core/about.html")