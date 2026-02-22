from zou.app import app
from sqlalchemy import text
from zou.app import db

with app.app_context():
    with db.engine.begin() as conn:
        # Delete the invalid/missing revision that is preventing Alembic from working
        conn.execute(text("DELETE FROM alembic_version"))
        
        # Insert the correct base revision that our new migration builds upon
        conn.execute(text("INSERT INTO alembic_version (version_num) VALUES ('c1d2e3f4a5b6')"))
        
        print("Successfully reset Alembic version to c1d2e3f4a5b6 in the database.")
