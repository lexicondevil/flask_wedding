"""empty message

Revision ID: 45e30b5f016c
Revises: None
Create Date: 2016-04-23 17:52:48.358324

"""

# revision identifiers, used by Alembic.
revision = '45e30b5f016c'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rsvps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('guests', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rsvps_email'), 'rsvps', ['email'], unique=True)
    op.create_index(op.f('ix_rsvps_guests'), 'rsvps', ['guests'], unique=False)
    op.create_index(op.f('ix_rsvps_name'), 'rsvps', ['name'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rsvps_name'), table_name='rsvps')
    op.drop_index(op.f('ix_rsvps_guests'), table_name='rsvps')
    op.drop_index(op.f('ix_rsvps_email'), table_name='rsvps')
    op.drop_table('rsvps')
    ### end Alembic commands ###
