"""empty message

Revision ID: 6215d4278ee1
Revises: 
Create Date: 2019-07-21 13:49:52.365867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6215d4278ee1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_title', sa.String(length=100), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('time', sa.TIME(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('information', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('security_answer1', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('event')
    # ### end Alembic commands ###
