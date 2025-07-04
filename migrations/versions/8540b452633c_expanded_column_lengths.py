"""Expanded column lengths

Revision ID: 8540b452633c
Revises: 
Create Date: 2025-06-11 04:22:46.178546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8540b452633c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seo_request', schema=None) as batch_op:
        batch_op.alter_column('url',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=1000),
               existing_nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=2000),
               existing_nullable=True)
        batch_op.alter_column('h1',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('canonical',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seo_request', schema=None) as batch_op:
        batch_op.alter_column('canonical',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('h1',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.String(length=2000),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=255),
               existing_nullable=True)
        batch_op.alter_column('url',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###
