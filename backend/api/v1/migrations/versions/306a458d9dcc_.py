"""empty message

Revision ID: 306a458d9dcc
Revises: 5f1c584f5a0
Create Date: 2015-11-20 16:04:56.416932

"""

# revision identifiers, used by Alembic.
revision = '306a458d9dcc'
down_revision = '5f1c584f5a0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('credit_card', sa.Column('stripe_customer_id', sa.String(length=120), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('credit_card', 'stripe_customer_id')
    ### end Alembic commands ###