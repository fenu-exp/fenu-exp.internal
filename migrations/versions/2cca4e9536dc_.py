"""empty message

Revision ID: 2cca4e9536dc
Revises: b7153f487b78
Create Date: 2020-01-31 14:55:27.256609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cca4e9536dc'
down_revision = 'b7153f487b78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('tags', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('document', 'tags')
    # ### end Alembic commands ###