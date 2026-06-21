"""cascade delete salary scale entries when a department is deleted

Salary scale rows are auto-generated for every department/position/seniority
combination and have no meaning without their department, so they should be
removed together with it. The foreign key is recreated with ON DELETE CASCADE
to replace the default RESTRICT behaviour that blocked department deletion.

Revision ID: d1e2f3a4b5c6
Revises: d4e5f6a7b8c9
Create Date: 2026-06-21 10:00:00.000000

"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "d1e2f3a4b5c6"
down_revision = "d4e5f6a7b8c9"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint(
        "salary_scale_department_id_fkey",
        "salary_scale",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "salary_scale_department_id_fkey",
        "salary_scale",
        "department",
        ["department_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        "salary_scale_department_id_fkey",
        "salary_scale",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "salary_scale_department_id_fkey",
        "salary_scale",
        "department",
        ["department_id"],
        ["id"],
    )
