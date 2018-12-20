"""empty message

Revision ID: 27694d2c80bd
Revises: 4d79791a5add
Create Date: 2018-12-01 09:33:17.756774

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '27694d2c80bd'
down_revision = '4d79791a5add'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('food', sa.String(length=255), nullable=True))
    op.add_column('order', sa.Column('number', sa.Integer(), nullable=True))
    op.drop_constraint('order_ibfk_1', 'order', type_='foreignkey')
    op.drop_column('order', 'food_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('food_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('order_ibfk_1', 'order', 'food', ['food_id'], ['id'])
    op.drop_column('order', 'number')
    op.drop_column('order', 'food')
    # ### end Alembic commands ###