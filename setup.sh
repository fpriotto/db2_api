virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
python3 -Wignore ./src/db2-api.py
deactivate