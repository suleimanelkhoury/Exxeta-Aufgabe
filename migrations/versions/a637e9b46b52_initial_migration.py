"""Initial migration

Revision ID: a637e9b46b52
Revises: 
Create Date: 2024-12-13 16:20:59.250206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a637e9b46b52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exxellent_nights',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('room_size', sa.Enum('SINGLE', 'DOUBLE', 'SUITE', name='roomsize'), nullable=False),
    sa.Column('has_minibar', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exxellent_nights')
    # ### end Alembic commands ###