
set -o errexit

pip install -r requirements.txt

python myproject/manage.py collectstatic --no-input
python myproject/manage.py migrate
