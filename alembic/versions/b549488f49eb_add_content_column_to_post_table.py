"""add content column to post table

Revision ID: b549488f49eb
Revises: 74c32766179e
Create Date: 2024-08-30 11:17:34.115310

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b549488f49eb'
down_revision: Union[str, None] = '74c32766179e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
