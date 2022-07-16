cd "$(dirname "$0")/.."
cd tailwind

npx tailwindcss -i ../ipmail/web/static/css/tailwind_base.css -o ../ipmail/web/static/css/production.css
npx cleancss ../ipmail/web/static/css/production.css -o ../ipmail/web/static/css/production.min.css

rm ../ipmail/web/static/css/production.css
