"""Add the per-user asset creation permission.

Revision ID: d5a6b7c8e9f0
Revises: b4c5d6e7f8a
Create Date: 2026-08-09

"""

from alembic import op
import sqlalchemy as sa


revision = "d5a6b7c8e9f0"
down_revision = "b4c5d6e7f8a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "person",
        sa.Column(
            "can_create_assets",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )
    op.alter_column("person", "can_create_assets", server_default=None)


def downgrade():
    op.drop_column("person", "can_create_assets")
