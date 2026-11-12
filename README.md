# Ukrainian Welcome Centre website

Recovered application source for the Ukrainian Welcome Centre website. You can clone this repository and continue development independently.

The website content remains in the form in which **Stefan Dezyk** created it. The recovery and handover have not revised the published content.

## Stack

- Python 3.12 and Django 5.1.3
- PostgreSQL, Django ORM, Django authentication and django-allauth
- Django templates, Bootstrap 5.3.3, jQuery, CSS and JavaScript
- English and Ukrainian content; custom editorial dashboard and role permissions
- Local media storage for development; S3 support for deployment

Source, templates, translations and static assets are in this repository. Database copies and uploaded media are provided as release assets and are excluded from Git.

## Download the database and media

Use the named assets in the [handover release](https://github.com/vldkurov/uwc-proto-handoff/releases/tag/handoff-2026-11-12):

| File | Purpose |
| --- | --- |
| [uwc-demo.dump](https://github.com/vldkurov/uwc-proto-handoff/releases/download/handoff-2026-11-12/uwc-demo.dump) | Sanitized PostgreSQL custom-format backup; restore with PostgreSQL 18 |
| [uwc-demo.json](https://github.com/vldkurov/uwc-proto-handoff/releases/download/handoff-2026-11-12/uwc-demo.json) | Portable Django data fixture; use migrations with PostgreSQL 16+ |
| [uwc-media.zip](https://github.com/vldkurov/uwc-proto-handoff/releases/download/handoff-2026-11-12/uwc-media.zip) | All 47 recovered media files; archive root is `media/` |
| [SHA256SUMS.txt](https://github.com/vldkurov/uwc-proto-handoff/releases/download/handoff-2026-11-12/SHA256SUMS.txt) | Checksums for the separate assets and complete archive |
| [Complete handover archive](https://github.com/vldkurov/uwc-proto-handoff/releases/download/handoff-2026-11-12/uwc-handoff-2026-11-12.zip) | Existing all-in-one alternative, including source, data, media, setup guide and screenshots |

No GitHub sign-in is required. Download only one database format. The complete archive is optional when you clone this repository.

## Local setup

Install Python 3.12 and PostgreSQL, and start your local PostgreSQL service. The commands below use a macOS/Linux shell; use the equivalent virtual environment activation on Windows.

```bash
git clone https://github.com/vldkurov/uwc-proto-handoff.git
cd uwc-proto-handoff
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`. Set `DATABASE_URL` to a new local database you own. The example assumes `uwc_local` on `localhost:5432` and your OS user. If your PostgreSQL installation requires credentials, use your local username and password:

```dotenv
DATABASE_URL=postgresql://YOUR_USER:YOUR_PASSWORD@localhost:5432/uwc_local
DJANGO_DEBUG=True
USE_S3=False
```

Generate a unique local secret and copy its value into `DJANGO_SECRET_KEY` in `.env`:

```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

Keep the other local-development settings from `.env.example`. Its placeholder credentials allow ordinary pages and local media to run without the previous cloud accounts.

### Restore one database format

Download the selected database asset to the repository root using the links above.

For **PostgreSQL 18**, restore the custom backup into a new empty local database:

```bash
createdb uwc_local
pg_restore --clean --if-exists --no-owner --no-acl --exit-on-error \
  --dbname=uwc_local uwc-demo.dump
python manage.py migrate
```

Alternatively, for **PostgreSQL 16+**, use the portable JSON fixture:

```bash
createdb uwc_local
python manage.py migrate
python manage.py loaddata uwc-demo.json
```

Use one route, not both in the same database. The JSON import may print geocoding warnings with placeholder Maps keys; saved coordinates are included and no Google credentials are required for import.

### Restore media and create your administrator

Download `uwc-media.zip` to the repository root, then run:

```bash
unzip uwc-media.zip
python manage.py createsuperuser
python manage.py check
python manage.py runserver 127.0.0.1:8000
```

The resulting structure must be `media/images/...`, not `media/media/images/...`. No previous user accounts or passwords are included. Set your new administrator's project-specific Role to **Owner** in Django admin.

| Area | Local URL |
| --- | --- |
| English site | http://127.0.0.1:8000/en/ |
| Ukrainian site | http://127.0.0.1:8000/uk/ |
| Login | http://127.0.0.1:8000/en/accounts/login/ |
| Editorial dashboard | http://127.0.0.1:8000/en/dashboard/pages/ |
| Django admin | http://127.0.0.1:8000/en/admin/ |

The development toolbar can be closed using its Hide button if it covers a control on a small screen.

## Integrations and deployment

Normal pages, content editing and local media do not require AWS credentials. Email currently uses Django's console backend. Google Maps and PayPal require new credentials controlled by UWC or the receiving team before those integrations can be enabled and tested. Bootstrap, icons and jQuery load from CDNs, so full styling requires internet access.

The application previously ran on Heroku. Production hosting, DNS, email delivery, payments, Maps access and backups should be configured under organization-controlled accounts. `.env.example` contains local development settings, not production settings. Dependency versions are the recovered versions and should be reviewed before a new production deployment.

Supabase is not a dependency. The receiving team can choose its future architecture.

## Handover and verification

The source snapshot was recovered from commit `5cbe1ad47b6bb2f209386500b8c44234c452e1cc`. Application logic is unchanged. `.env.example`, this README and download exclusions have been prepared for independent local setup.

The old repository history, personal cloud credentials, production fixtures, account data, old operational logs and credential-bearing legacy import tools are excluded from this repository. The release databases exclude original user accounts, password hashes, sessions, admin audit logs, donation/payment records, draft fields and edit-history snapshots. Published content, photographs and the public directory/contact information are preserved.

Verification covered 16 pages, all 47 media files, desktop/mobile rendering and mobile navigation. Both database restoration formats were tested against the packaged application source; a newly created administrator could access the dashboard and Django admin.

Anna and her partner can take over further development and deployment. Volodymyr remains available for questions about the existing implementation and help getting started.
