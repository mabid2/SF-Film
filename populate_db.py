import sys, os, csv
from apps.locationmovies.models import Movies
csv_filepathname = "C:\databasecsv.csv"
project_home = "C:\Users\denys\Desktop\CodingDojo\Project1(django)\films"

sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

dataReader = csv.reader(open("C:\databasecsv.csv"), delimiter=',', quotechar='"')
readerData = list(dataReader)
for row in readerData:
    if row:
        if "Actor 1" not in row:
            try:
                movies = Movies()
                movies.title = row[0]
                movies.release_year = row[1]
                movies.location = row[2]
                movies.production_company = row[4]
                movies.director = row[6]
                movies.writer = row[7]
                movies.actors = row[8] + " " + row[9] + " " + row[10]
                movies.save()
                print "Got to the end"
            except IndexError:
                pass