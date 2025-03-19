"""Initial migration

Revision ID: 03a1420e0536
Revises:
Create Date: 2025-03-19 15:44:16.868687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = '03a1420e0536'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: Create `profile` table."""
    op.create_table(
        'profile',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('context', sa.String, nullable=False),
        sa.Column('full_name', sa.String, nullable=False),
        sa.Column('phone', sa.String, nullable=False, unique=True),
        sa.Column('email', sa.String, nullable=True),
        sa.Column('age_range', sa.String, nullable=True),
        sa.Column('gender', sa.String, nullable=True),
        sa.Column('marital_status', sa.String, nullable=True),
        sa.Column('approximate_location', sa.String, nullable=True),
        sa.Column('profession', sa.String, nullable=True),
        sa.Column('current_company', sa.String, nullable=True),
        sa.Column('social_media', JSONB, nullable=True),
        sa.Column('societary_status', JSONB, nullable=True),
        sa.Column('interests', JSONB, nullable=True),
        sa.Column('mentions', JSONB, nullable=True),
        sa.Column('legal_verification', JSONB, nullable=True),
        sa.Column('social_media_images', JSONB, nullable=True),
        sa.Column('observations_and_data_reconciliation', JSONB, nullable=True),
    )



def downgrade() -> None:
    """Downgrade schema: Drop `profile` table."""
    op.drop_table('profile')
