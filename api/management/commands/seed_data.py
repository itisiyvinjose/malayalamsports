from api.data_seed import seed_isl_teams, seed_football_match_series, seed_news, seed_match_series, seed_guest_news
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Seed ISL teams data'

    # def add_arguments(self, parser):
    #     parser.add_argument('file_name', nargs='+', type=int)

    def handle(self, *args, **options):
        seed_isl_teams.seed_data()
        self.stdout.write(self.style.SUCCESS('ISL TEAMS seed completed'))
        self.stdout.write('\n')

        seed_football_match_series.seed_data()
        self.stdout.write(self.style.SUCCESS('ISL SERIES seed completed'))
        self.stdout.write('\n')

        seed_news.seed_data()
        self.stdout.write(self.style.SUCCESS('Sports news seed completed'))

        seed_match_series.seed_data()
        self.stdout.write(self.style.SUCCESS('Sports Match series seed completed'))

        seed_guest_news.seed_data()
        self.stdout.write(self.style.SUCCESS('Guest news seed completed'))

