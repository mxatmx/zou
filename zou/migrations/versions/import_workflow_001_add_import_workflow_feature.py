"""add_import_workflow_feature

Revision ID: import_workflow_001
Revises: 
Create Date: 2024-12-16

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "import_workflow_001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create the task_type_asset_type_import_link table
    op.create_table(
        "task_type_asset_type_import_link",
        sa.Column(
            "asset_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("entity_type.id"),
            primary_key=True,
            index=True,
        ),
        sa.Column(
            "task_type_id",
            UUID(as_uuid=True),
            sa.ForeignKey("task_type.id"),
            primary_key=True,
            index=True,
        ),
        sa.UniqueConstraint(
            "asset_type_id",
            "task_type_id",
            name="task_type_asset_type_import_link_uc",
        ),
    )

    # Add uses_import_workflow column to entity table
    op.add_column(
        "entity",
        sa.Column(
            "uses_import_workflow",
            sa.Boolean(),
            nullable=True,
            default=False,
        ),
    )
    op.create_index(
        "ix_entity_uses_import_workflow",
        "entity",
        ["uses_import_workflow"],
    )

    # Set default value for existing rows
    op.execute("UPDATE entity SET uses_import_workflow = false")

    # Make column non-nullable after setting defaults
    op.alter_column(
        "entity",
        "uses_import_workflow",
        nullable=False,
        server_default=sa.text("false"),
    )


def downgrade():
    # Remove index and column from entity
    op.drop_index("ix_entity_uses_import_workflow", table_name="entity")
    op.drop_column("entity", "uses_import_workflow")

    # Drop the import link table
    op.drop_table("task_type_asset_type_import_link")
