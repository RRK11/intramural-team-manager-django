from django.contrib import admin
from .models import Player, Team, TeamPlayer, Game


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "skill_level", "created_at")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("skill_level",)
    ordering = ("last_name", "first_name")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_name", "sport", "captain_name", "created_at")
    search_fields = ("team_name", "sport", "captain_name")
    list_filter = ("sport",)
    ordering = ("team_name",)


@admin.register(TeamPlayer)
class TeamPlayerAdmin(admin.ModelAdmin):
    list_display = ("team", "player", "jersey_number", "date_joined")
    search_fields = ("team__team_name", "player__first_name", "player__last_name")
    list_filter = ("team", "date_joined")
    ordering = ("team__team_name", "player__last_name")


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("team", "opponent_name", "game_date", "location", "result", "points_scored", "points_allowed")
    search_fields = ("team__team_name", "opponent_name", "location")
    list_filter = ("team", "result", "game_date")
    ordering = ("-game_date",)