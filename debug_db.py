from zou.app import app
import flask_migrate

with app.app_context():
    from sqlalchemy import text
    from zou.app import db
    try:
        with db.engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM alembic_version"))
            print("Current Database alembic_version:")
            for row in result:
                print(row)

            # Check if the tables exist
            tables = ["software_person_link", "hardware_item_person_link"]
            for table in tables:
                res = conn.execute(text(f"SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_schema = 'public' AND table_name = '{table}')"))
                exists = res.scalar()
                print(f"Table '{table}' exists: {exists}")
    except Exception as e:
        print("Error checking database:", e)
