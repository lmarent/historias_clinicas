# Full path and name to your csv file
csv_filepathname="C:\Historias\hist\historias\Enfermedades.csv"
# Full path to your django project directory
your_djangoproject_home="C:\Historias\hist\hist"
 
import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
 
from historias.models import Diagnostico
 
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')
 
for row in dataReader:
   if row[0] != 'CODIGO': # Ignore the header row, import everything else
      diagnostico = Diagnostico()
      diagnostico.codigo_int = row[0]
      diagnostico.nombre = row[1]
      diagnostico.save()