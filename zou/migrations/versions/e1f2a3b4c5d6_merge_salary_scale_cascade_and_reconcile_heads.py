"""merge the salary-scale-cascade and squash-reconcile heads

The fork carried two parallel Alembic heads:

  * 2b8f88aa610f - reconcile squash schema with legacy
  * d1e2f3a4b5c6 - cascade delete salary scale on department (via the
                   import-workflow / person-links line)

Both descend from a0f668430352, so ``alembic upgrade head`` could not pick a
single target and aborted with "Multiple head revisions are present", which
made ``zou upgrade-db`` a no-op on deploy. This empty merge revision unites
them into one head so upgrades resolve again.

Revision ID: e1f2a3b4c5d6
Revises: 2b8f88aa610f, d1e2f3a4b5c6
Create Date: 2026-06-21 10:30:00.000000

"""


# revision identifiers, used by Alembic.
revision = "e1f2a3b4c5d6"
down_revision = ("2b8f88aa610f", "d1e2f3a4b5c6")
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
