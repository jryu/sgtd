mkdir -p things/fixtures

./manage.py dumpdata --indent=2 things auth.User | \
	tee things/fixtures/initial_data.json
