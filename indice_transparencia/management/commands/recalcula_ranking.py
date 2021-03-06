from django.core.management.base import BaseCommand, CommandError
from indice_transparencia.models import Person, update_positions_in_ranking, RankingData


class Command(BaseCommand):
    help = 'Recalcula las notas y el ranking de los candidatos'
    
    def handle(self, *args, **options):
        """ Do your work here """
        # print("Recalculando Ranking")
        # self.stdout.write("Recalculando Ranking")
        for p in Person.objects.all():
            ranking_data, is_new = RankingData.objects.get_or_create(person=p)
            if is_new:
                p.ranking_data=ranking_data
                p.save()
            p.update_mark()

        update_positions_in_ranking()