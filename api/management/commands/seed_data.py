from api.data_seed import seed_isl_teams
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Seed ISL teams data'

    # def add_arguments(self, parser):
    #     parser.add_argument('file_name', nargs='+', type=int)

    def handle(self, *args, **options):
        seed_isl_teams.seed_data()
        self.stdout.write(self.style.SUCCESS('Completed ISL data seed'))