"""empty message

Revision ID: e5de38abd2c4
Revises: 45e30b5f016c
Create Date: 2016-05-04 12:40:59.158613

"""

# revision identifiers, used by Alembic.
revision = 'e5de38abd2c4'
down_revision = '45e30b5f016c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_rsvps_email', table_name='rsvps')
    op.create_index(op.f('ix_rsvps_email'), 'rsvps', ['email'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rsvps_email'), table_name='rsvps')
    op.create_index('ix_rsvps_email', 'rsvps', ['email'], unique=True)
    ### end Alembic commands ###