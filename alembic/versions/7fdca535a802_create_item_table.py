"""create item table

Revision ID: 7fdca535a802
Revises: 
Create Date: 2024-01-18 16:01:08.604410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from advanced_alchemy.types import GUID, DateTimeUTC

# revision identifiers, used by Alembic.
revision: str = '7fdca535a802'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('done', sa.Boolean(), nullable=False),
                    sa.Column('id', GUID(length=16), nullable=False),
                    sa.Column('sa_orm_sentinel', sa.Integer(), nullable=True),
                    sa.Column('created_at', DateTimeUTC(timezone=True), nullable=False),
                    sa.Column('updated_at', DateTimeUTC(timezone=True), nullable=False),
                    sa.PrimaryKeyConstraint('id', name=op.f('pk_item'))
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
