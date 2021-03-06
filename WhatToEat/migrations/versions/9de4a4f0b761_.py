"""empty message

Revision ID: 9de4a4f0b761
Revises: 549b1474e7ee
Create Date: 2018-12-20 14:54:11.547405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9de4a4f0b761'
down_revision = '549b1474e7ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('food', sa.String(length=255), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('addtime', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_addtime'), 'record', ['addtime'], unique=False)
    op.drop_index('ix_order_addtime', table_name='order')
    op.drop_table('order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('addtime', mysql.DATETIME(), nullable=True),
    sa.Column('food', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('number', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='order_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_order_addtime', 'order', ['addtime'], unique=False)
    op.drop_index(op.f('ix_record_addtime'), table_name='record')
    op.drop_table('record')
    # ### end Alembic commands ###
