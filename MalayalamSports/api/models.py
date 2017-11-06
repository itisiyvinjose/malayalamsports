import bcrypt
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from api.localisation.constants import *

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Admin(BaseModel):
    """
    admin model
    """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=400)

    def save(self, *args, **kwargs):
        # validate params
        if not self.email:
            raise ValidationError('email field is required')

        if not self.password:
            raise ValidationError('password field is required')

        # validate email format
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError('invalid email ')

        if self.pk is None:
            self.set_password(self.password)

        elif self.pk is not None:

            record = Admin.objects.get(pk=self.pk)
            if record.password != self.password:
                self.set_password(self.password)

        super(Admin, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        hashed = bcrypt.hashpw(raw_password.encode('utf8'), bcrypt.gensalt(5))
        self.password = hashed
        print(str(hashed))

    def check_password(self, raw_password):
        if bcrypt.checkpw(raw_password.encode('utf8'), self.password.encode('utf8')):
            return True
        else:
            return False


class News(BaseModel):
    """
    sport news model
    have many to many field for accessing related news
    """
    news_date = models.DateField(db_index=True)
    content = models.TextField()
    source = models.CharField(max_length=200)
    title = models.TextField()
    # TODO: add images
    # TODO: generate thumbnail images
    tags = models.TextField(default="[]")
    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200)
    is_trending = models.BooleanField(default=False)
    trend_scale = models.IntegerField(null=True, blank=True)
    related_news = models.ManyToManyField("self", blank=True, through='NewsRelationsShip', symmetrical=False, related_name='+')
    number_of_likes = models.IntegerField(default=0)
    number_of_dislikes = models.IntegerField(default=0)
    number_of_views = models.IntegerField(default=0)


class NewsRelationsShip(models.Model):
    news = models.ForeignKey("News", on_delete=models.CASCADE, related_name='+')
    related_news = models.ForeignKey("News", on_delete=models.CASCADE, related_name='+')
    relation_index = models.IntegerField(default=0)
    common_tags = models.TextField(default='[]')


class NewsTags(BaseModel):
    name = models.CharField(max_length=200, unique=True)


class SportsMatch(BaseModel):
    match_starting_date = models.DateField(db_index=True)
    match_starting_time = models.TimeField()
    match_finishing_date = models.DateField()
    match_finishing_time = models.TimeField()

    status = models.CharField(choices=MATCH_STATUS, max_length=200, db_index=True)
    match_facts = models.TextField(null=True)
    match_description = models.TextField()
    venue = models.TextField()
    postponed_date = models.DateField()
    postponed_time = models.TimeField()
    concise_summary_text = models.TextField()

    team_one = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='+')
    team_two = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='+')
    team_won = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='+', null=True,
                                 blank=True)
    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200, db_index=True)


class Players(BaseModel):
    name = models.CharField(max_length=200)
    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200, db_index=True)
    biography = models.TextField()
    # TODO: image


class FootBallMatchDetails(BaseModel):
    match_starting_date = models.DateField(null=True, blank=True, db_index=True)
    match_finishing_date = models.DateField(null=True, blank=True)

    match_starting_time = models.TimeField(null=True, blank=True)
    match_finishing_time = models.TimeField(null=True, blank=True)

    status = models.CharField(choices=MATCH_STATUS, max_length=200, db_index=True)
    current_status_text = models.CharField(max_length=200, null=True, blank=True)
    match_facts = models.TextField(null=True, blank=True)
    match_description = models.TextField(null=True, blank=True)
    venue = models.TextField()
    postponed_date = models.DateField(null=True, blank=True)
    postponed_time = models.TimeField(null=True, blank=True)
    concise_summary_text = models.TextField(null=True, blank=True)
    current_play_time_status = models.CharField(choices=CURRENT_PLAY_TIME, max_length=200, null=True)

    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200)

    team_one = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='+',)
    team_two = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='+',)
    team_won = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='+', null=True,
                                 blank=True)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)


class FootballMatchCommentary(BaseModel):
    current_play_time_status = models.CharField(choices=CURRENT_PLAY_TIME, max_length=200, null=True)
    added_time = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField()
    football_match = models.ForeignKey("FootBallMatchDetails", on_delete=models.CASCADE, related_name='commentaries')
    is_key_event = models.BooleanField(default=False)



class SportTeam(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200, db_index=True)
    # TODO: logo
