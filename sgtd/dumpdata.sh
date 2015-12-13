TIMESTAMP=`date +%s`

mv db.sqlite3 ~/db.$TIMESTAMP.sqlite3

./manage.py dumpdata --indent=2 things todo auth.User | \
	tee ~/dump.$TIMESTAMP.json

./manage.py syncdb --noinput --no-initial-data

./manage.py loaddata ~/dump.$TIMESTAMP.json
