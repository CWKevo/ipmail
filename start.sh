cd "$(dirname "$0")"

export FLASK_ENV="development"
export FLASK_APP="ipmail.web:WEB"

flask run --host 0.0.0.0 --port 5000
