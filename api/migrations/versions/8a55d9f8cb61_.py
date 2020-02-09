"""empty message

Revision ID: 8a55d9f8cb61
Revises: 87213d612eaf
Create Date: 2020-02-06 16:43:13.223557

"""

# revision identifiers, used by Alembic.
revision = '8a55d9f8cb61'
down_revision = '87213d612eaf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_user', sa.Column('policy_agreed_datetime', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('app_user', 'policy_agreed_datetime')
    # ### end Alembic commands ###