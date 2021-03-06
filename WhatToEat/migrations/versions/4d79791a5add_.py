"""empty message

Revision ID: 4d79791a5add
Revises: 93965b5805d9
Create Date: 2018-11-19 17:20:35.686929

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4d79791a5add'
down_revision = '93965b5805d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('order_num', sa.Integer(), nullable=True))
    op.drop_column('category', 'order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('order', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('category', 'order_num')
    # ### end Alembic commands ###
