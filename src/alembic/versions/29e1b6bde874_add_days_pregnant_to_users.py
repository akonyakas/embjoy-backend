"""Add days_pregnant to users

Revision ID: 29e1b6bde874
Revises: 751aaa8f655a
Create Date: 2024-08-25 20:59:47.343000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29e1b6bde874'
down_revision: Union[str, None] = '751aaa8f655a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('days_pregnant', sa.INT, nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'days_pregnant')
    # ### end Alembic commands ###
