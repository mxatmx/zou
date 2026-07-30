"""merge upstream v1.0.55 and fork migration heads

The fork's salary-scale cascade migration was merged with the upstream head
available at the time. Upstream later introduced its own cascade migration and
subsequent revisions from the same ancestor. This no-op revision joins the two
valid histories so deployments have one Alembic head.

Revision ID: b4c5d6e7f8a
Revises: e7f8a9b0c1d2, 4159fed814b5
Create Date: 2026-07-30 00:00:00.000000

"""


# revision identifiers, used by Alembic.
revision = "b4c5d6e7f8a"
down_revision = ("e7f8a9b0c1d2", "4159fed814b5")
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
