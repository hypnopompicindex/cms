from django.core.management.base import BaseCommand, CommandError
import subprocess
from cms.settings import MEDIA_ROOT, BACKUP_MEDIA


class Command(BaseCommand):
    '''
    Backup Media Files
    '''
    help = 'Backup media files'

    def handle(self, *args, **options):
        rsync_cmd = 'rsync -a ' + MEDIA_ROOT + ' ' + BACKUP_MEDIA
        subprocess.call(rsync_cmd, shell=True)
