"""Added FK

Revision ID: b723324684ce
Revises: da7e038e7070
Create Date: 2020-02-29 22:29:35.845404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b723324684ce'
down_revision = 'da7e038e7070'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('seat_reservation', sa.Column('user_reservation_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'seat_reservation', 'user_reservation', ['user_reservation_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'seat_reservation', type_='foreignkey')
    op.drop_column('seat_reservation', 'user_reservation_id')
    # ### end Alembic commands ###
