"""merge the software/hardware person-link branch with the squash-reconcile branch

Two migration heads existed in this fork:

* ``2b8f88aa610f`` (reconcile_squash_schema_with_legacy) — the line that also
  carries ``a1bc96e68661`` which adds ``person.is_guest``.
* ``a2b3c4d5e6f7`` (add_person_links_for_software_and_hardware) — the fork
  feature line branched from ``a0f668430352``.

Having two heads makes ``alembic upgrade head`` fail with "Multiple head
revisions are present", so the schema (including ``person.is_guest``) is never
applied. This empty merge migration joins both branches into a single head so
the upgrade can proceed; it makes no schema changes of its own.

Revision ID: d4e5f6a7b8c9
Revises: 2b8f88aa610f, a2b3c4d5e6f7
Create Date: 2026-06-13 00:00:00.000000

"""

# revision identifiers, used by Alembic.
revision = "d4e5f6a7b8c9"
down_revision = ("2b8f88aa610f", "a2b3c4d5e6f7")
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
