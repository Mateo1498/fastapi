"""add content column to posts table

Revision ID: c9b8c3747c42
Revises: dc41d8a9ee27
Create Date: 2022-10-13 16:38:58.410435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9b8c3747c42'
down_revision = 'dc41d8a9ee27'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
