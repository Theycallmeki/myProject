
set -o errexit

pip install -r requirements.txt

python myProject/manage.py collectstatic --no-input
python myProject/manage.py migrate
