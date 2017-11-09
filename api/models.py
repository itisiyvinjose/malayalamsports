import json

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
    news_date_time = models.DateTimeField(null=True, blank=False)
    content = models.TextField()
    source = models.CharField(max_length=200)
    title = models.TextField()
    # TODO: add images
    # TODO: generate thumbnail images
    tags = models.TextField(default="[]")
    related_tags = models.ManyToManyField("NewsTags", blank=True, related_name='+')
    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200)
    is_trending = models.BooleanField(default=False)
    trend_scale = models.IntegerField(null=True, blank=True)
    related_news = models.ManyToManyField("self", blank=True, through='NewsRelationsShip', symmetrical=False, related_name='+')
    number_of_likes = models.IntegerField(default=0)
    number_of_dislikes = models.IntegerField(default=0)
    number_of_views = models.IntegerField(default=0)
    should_display_on_home_page = models.BooleanField(default=False)
    home_page_display_order = models.IntegerField(default=0)

    def save(self, *args, **kwargs):

        def filter_new_tags(tags):
            existing_tags = NewsTags.objects.values_list('tag_name', flat=True)
            new_tags = list(set(tags) - set(existing_tags))
            return new_tags

        def save_new_tags(tags):
            for tag in tags:
                obj, created = NewsTags.objects.get_or_create(
                    tag_name=tag
                )

                if created:
                    print('Tag ' + tag + ' created')

        def update_tags():
            if self.tags:
                tags = json.loads(self.tags)
                new_tags = filter_new_tags(tags)
                save_new_tags(new_tags)

        if 'relationship_update' in kwargs:
            relationship_update = kwargs.pop('relationship_update', None)
            if relationship_update:
                pass
            else:
                update_tags()

        else:
            update_tags()

        super(News, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.id) + str(" ") + str(self.title)


class NewsRelationsShip(models.Model):
    news = models.ForeignKey("News", on_delete=models.CASCADE, related_name='+')
    related_news = models.ForeignKey("News", on_delete=models.CASCADE, related_name='+')
    relation_index = models.IntegerField(default=0)
    common_tags = models.TextField(default='[]')


class NewsTags(BaseModel):
    tag_name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('tag_name',)

    def __str__(self):
        return str(self.tag_name.capitalize())


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

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.id) + str(" ") + str(self.status)


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

    match_title = models.TextField()

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

    should_show_on_home_page = models.BooleanField(default=False)
    display_priority_scale = models.IntegerField(default=0)
    is_kerala_blasters_involved = models.BooleanField(default=False)

    series = models.ForeignKey("SportTeam", on_delete=models.CASCADE, related_name='matches', null=True, blank=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return str(self.id) + str(" ") + str(self.match_title)


class FootballMatchCommentary(BaseModel):
    current_play_time_status = models.CharField(choices=CURRENT_PLAY_TIME, max_length=200, null=True)
    added_time = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField()
    football_match = models.ForeignKey("FootBallMatchDetails", on_delete=models.CASCADE, related_name='commentaries')
    is_key_event = models.BooleanField(default=False)


class SportTeam(BaseModel):
    display_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    sport = models.CharField(choices=SPORT_CATEGORY, max_length=200, db_index=True)
    identifier = models.CharField(max_length=200)
    # TODO: logo

    class Meta:
        ordering = ('display_name',)

    def __str__(self):
        return str(self.id) + str(" ") + str(self.identifier)


class MatchSeries(BaseModel):
    display_name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200, unique=True)


    class Meta:
        ordering = ('display_name',)

    def __str__(self):
        return str(self.id) + str(" ") + str(self.identifier)
