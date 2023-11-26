"""Add ChatId model

Revision ID: 9e5aa4e19647
Revises: 3dd3bacefcb6
Create Date: 2023-11-26 22:29:30.097838

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9e5aa4e19647"
down_revision: Union[str, None] = "3dd3bacefcb6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "chat_ids",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("chat_ids")
    # ### end Alembic commands ###