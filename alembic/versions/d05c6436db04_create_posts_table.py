"""create posts table

Revision ID: d05c6436db04
Revises: 
Create Date: 2025-08-31 14:29:53.753985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd05c6436db04'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String(), nullable=False), 
                    sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'), 
                    sa.UniqueConstraint('title'))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
