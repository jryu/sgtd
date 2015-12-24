set -e

TIMESTAMP=`date +%s`

./manage.py dumpdata --indent=2 \
	things todo auth.User sites sessions socialaccount | \
	tee ~/dump.$TIMESTAMP.json

mv db.sqlite3 ~/db.$TIMESTAMP.sqlite3

./manage.py migrate --noinput

./manage.py loaddata ~/dump.$TIMESTAMP.json
