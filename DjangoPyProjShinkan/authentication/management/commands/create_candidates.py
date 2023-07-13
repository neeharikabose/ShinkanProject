from django.core.management.base import BaseCommand
from authentication.models import CandidateData

class Command(BaseCommand):
    help = 'Creates new candidates'

    def handle(self, *args, **options):
        candidates = [
            {'username': 'john', 'password': 'secret'},
            {'username': 'jane', 'password': 'pass123'},
        ]

        for candidate in candidates:
            CandidateData.objects.create(username=candidate['username'], password=candidate['password'])
