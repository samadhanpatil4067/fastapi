"""add colum to post table

Revision ID: 182f4137c87b
Revises: d05c6436db04
Create Date: 2025-08-31 14:42:52.421552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '182f4137c87b'
down_revision: Union[str, Sequence[str], None] = 'd05c6436db04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
