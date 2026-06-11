# LearnLoop

LearnLoop is a Django-based web application that includes features for accounts, careers, mentorship, and chat.

## Prerequisites
- Python 3.9+
- pip (Python package installer)

## Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd LearnLoop
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirement.txt
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory (alongside `manage.py`) and add your API keys:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional, for admin panel access):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

## Deployment (Vercel)

If you plan to deploy this application to Vercel, please note that Vercel is a serverless environment. You will need to make the following architectural changes before deploying:

1. **Migrate to PostgreSQL**: You cannot use the local `db.sqlite3` file on Vercel because the serverless filesystem is ephemeral. You must provision a cloud PostgreSQL database (e.g., Neon, Supabase) and connect to it using `dj-database-url`.
2. **Static Files Management**: Configure `whitenoise` to serve static files correctly in production.
3. **Vercel Configuration**: Add a `vercel.json` file to define routing and specify the `@vercel/python` builder.
4. **Environment Variables**: Add your `DATABASE_URL`, `GROQ_API_KEY`, and `SECRET_KEY` directly in the Vercel project settings dashboard.

