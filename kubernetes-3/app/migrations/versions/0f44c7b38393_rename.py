"""rename

Revision ID: 0f44c7b38393
Revises: e1c1c4333361
Create Date: 2021-10-31 09:45:51.048876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0f44c7b38393"
down_revision = "e1c1c4333361"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("firstName", sa.String(length=60), nullable=True))
    op.add_column("users", sa.Column("lastName", sa.String(length=60), nullable=True))
    op.drop_column("users", "last_name")
    op.drop_column("users", "first_name")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "first_name", sa.VARCHAR(length=60), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "users",
        sa.Column(
            "last_name", sa.VARCHAR(length=60), autoincrement=False, nullable=True
        ),
    )
    op.drop_column("users", "lastName")
    op.drop_column("users", "firstName")
    # ### end Alembic commands ###
