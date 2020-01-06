"""empty message

Revision ID: b7153f487b78
Revises: 
Create Date: 2020-01-31 13:49:49.601596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7153f487b78'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('author', sa.Text(), nullable=True),
    sa.Column('reference', sa.String(length=256), nullable=True),
    sa.Column('year', sa.Float(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=128), nullable=True),
    sa.Column('path', sa.String(length=256), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_document_timestamp'), 'document', ['timestamp'], unique=False)
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('head', sa.String(length=128), nullable=True),
    sa.Column('shortcut', sa.String(length=64), nullable=True),
    sa.Column('link', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('head')
    )
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('path', sa.String(length=256), nullable=True),
    sa.Column('xsize', sa.Float(), nullable=True),
    sa.Column('ysize', sa.Float(), nullable=True),
    sa.Column('zoom', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_photo_timestamp'), 'photo', ['timestamp'], unique=False)
    op.create_table('bina',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('head', sa.String(length=128), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('abstract', sa.Text(), nullable=True),
    sa.Column('photo_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['photo_id'], ['photo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bina_timestamp'), 'bina', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('surname', sa.String(length=64), nullable=True),
    sa.Column('affiliation_id', sa.String(length=128), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('orcid', sa.String(length=128), nullable=True),
    sa.Column('rgate', sa.String(length=128), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['affiliation_id'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_timestamp'), 'user', ['timestamp'], unique=False)
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=False),
    sa.Column('localization', sa.String(length=128), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('members', sa.Text(), nullable=True),
    sa.Column('files', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_timestamp'), 'event', ['timestamp'], unique=False)
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('head', sa.Text(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_note_timestamp'), 'note', ['timestamp'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('head', sa.Text(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_note_timestamp'), table_name='note')
    op.drop_table('note')
    op.drop_index(op.f('ix_event_timestamp'), table_name='event')
    op.drop_table('event')
    op.drop_index(op.f('ix_user_timestamp'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_bina_timestamp'), table_name='bina')
    op.drop_table('bina')
    op.drop_index(op.f('ix_photo_timestamp'), table_name='photo')
    op.drop_table('photo')
    op.drop_table('organization')
    op.drop_index(op.f('ix_document_timestamp'), table_name='document')
    op.drop_table('document')
    # ### end Alembic commands ###