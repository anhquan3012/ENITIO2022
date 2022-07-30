"""Store player kills and treasure counts

Revision ID: 0af3d19f7eb5
Revises: b0a194a235c8
Create Date: 2022-07-20 22:52:19.991444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af3d19f7eb5'
down_revision = 'b0a194a235c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('level1_treasure',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('location', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('level2_treasure',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('collected_by_id', sa.Integer(), nullable=True),
    sa.Column('is_treasure', sa.Boolean(), nullable=False),
    sa.Column('is_virus', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['collected_by_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('treasure')
    op.add_column('player', sa.Column('num_kills', sa.Integer(), nullable=True))
    # ### end Alembic commands ###
    op.alter_column('level1_treasure', 'id', type_=sa.INTEGER, nullable=False, autoincrement=True, existing_autoincrement=True)
    op.alter_column('level2_treasure', 'id', type_=sa.INTEGER, nullable=False, autoincrement=True,
                    existing_autoincrement=True)

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('player', 'num_kills')
    op.create_table('treasure',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('level', sa.INTEGER(), nullable=False),
    sa.Column('location', sa.TEXT(), nullable=True),
    sa.Column('collected_by_id', sa.INTEGER(), nullable=True),
    sa.Column('is_treasure', sa.BOOLEAN(), nullable=False),
    sa.Column('is_virus', sa.BOOLEAN(), nullable=False),
    sa.ForeignKeyConstraint(['collected_by_id'], ['player.id'], ),
    sa.PrimaryKeyConstraint('id', 'level')
    )
    op.drop_table('player_treasure')
    op.drop_table('level2_treasure')
    op.drop_table('level1_treasure')
    # ### end Alembic commands ###
