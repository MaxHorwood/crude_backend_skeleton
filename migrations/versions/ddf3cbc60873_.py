"""empty message

Revision ID: ddf3cbc60873
Revises: x
Create Date: 2020-08-22 17:27:08.449495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ddf3cbc60873"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("postcode", sa.String(length=80), nullable=False),
        sa.Column("address", sa.String(length=100), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("address")
    op.drop_table("user")
    # ### end Alembic commands ###
