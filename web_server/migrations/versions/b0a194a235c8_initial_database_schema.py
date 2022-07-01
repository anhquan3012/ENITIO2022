"""Initial Database Schema

Revision ID: b0a194a235c8
Revises: 
Create Date: 2022-06-29 23:22:53.749405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0a194a235c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('OG', sa.Integer(), nullable=False),
    sa.Column('participant_id', sa.Integer(), nullable=True),
    sa.Column('mac_address', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('treasure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('collected_by_id', sa.Integer(), nullable=True),
    sa.Column('is_treasure', sa.Boolean(), nullable=False),
    sa.Column('is_virus', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['collected_by_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id', 'level')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('treasure')
    op.drop_table('player')
    op.drop_table('game_status')
    # ### end Alembic commands ###