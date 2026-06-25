"""merge the upstream sync head with the salary-scale cascade head

Merging ``upstream/main`` into this fork left two Alembic heads:

* ``c5e8b2a4f1d3`` (add_revision_padding) — the tip of the upstream migration
  line pulled in during the sync.
* ``d1e2f3a4b5c6`` (cascade_delete_salary_scale_on_department) — the fork's
  custom line that cascade-deletes salary scale entries on department deletion.

Having two heads makes ``alembic upgrade head`` fail with "Multiple head
revisions are present". This empty merge migration joins both branches into a
single head so the upgrade can proceed; it makes no schema changes of its own.

Revision ID: e7f8a9b0c1d2
Revises: c5e8b2a4f1d3, d1e2f3a4b5c6
Create Date: 2026-06-25 00:00:00.000000

"""

# revision identifiers, used by Alembic.
revision = "e7f8a9b0c1d2"
down_revision = ("c5e8b2a4f1d3", "d1e2f3a4b5c6")
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
