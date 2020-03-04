"""column name

Revision ID: e82f3b6189c0
Revises: e121f4497519
Create Date: 2020-02-29 23:17:22.608567

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e82f3b6189c0'
down_revision = 'e121f4497519'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layout', sa.Column('y_cordinate', sa.Integer(), nullable=False))
    op.drop_column('layout', 'y_cordinates')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layout', sa.Column('y_cordinates', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('layout', 'y_cordinate')
    # ### end Alembic commands ###
