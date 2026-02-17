python3 -m pip install -r requirements.txt --break-system-packages
mkdir -p staticfiles_build/static
python3 manage.py collectstatic --noinput --clear
