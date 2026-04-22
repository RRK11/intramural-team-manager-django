from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    skill_level = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "itm_players"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    sport = models.CharField(max_length=50)
    captain_name = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "itm_teams"
        ordering = ["team_name"]

    def __str__(self):
        return self.team_name


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="roster_assignments", db_column="team_id")
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="team_assignments", db_column="player_id")
    jersey_number = models.IntegerField(null=True, blank=True)
    date_joined = models.DateField()

    class Meta:
        db_table = "itm_team_players"
        ordering = ["team__team_name", "player__last_name", "player__first_name"]
        constraints = [
            models.UniqueConstraint(fields=["team", "player"], name="itm_team_players_team_id_player_id_key")
        ]

    def __str__(self):
        return f"{self.player} - {self.team}"


class Game(models.Model):
    RESULT_CHOICES = [
        ("Scheduled", "Scheduled"),
        ("Win", "Win"),
        ("Loss", "Loss"),
        ("Tie", "Tie"),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="games", db_column="team_id")
    opponent_name = models.CharField(max_length=100)
    game_date = models.DateField()
    location = models.CharField(max_length=100, blank=True)
    result = models.CharField(max_length=20, choices=RESULT_CHOICES, default="Scheduled")
    points_scored = models.IntegerField(null=True, blank=True)
    points_allowed = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "itm_games"
        ordering = ["-game_date", "team__team_name"]

    def __str__(self):
        return f"{self.team} vs {self.opponent_name} ({self.game_date})"