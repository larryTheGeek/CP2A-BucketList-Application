"""empty message

Revision ID: 37e9b391fc68
Revises: fd748cffbbb1
Create Date: 2017-07-07 21:44:36.930668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37e9b391fc68'
down_revision = 'fd748cffbbb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('profile_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'items', 'profiles', ['profile_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'items', type_='foreignkey')
    op.drop_column('items', 'profile_id')
    # ### end Alembic commands ###