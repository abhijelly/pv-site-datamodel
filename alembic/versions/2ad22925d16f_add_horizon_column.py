"""Add horizon column

Revision ID: 2ad22925d16f
Revises: 830bec1172a8
Create Date: 2023-03-09 02:53:18.683328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ad22925d16f'
down_revision = '830bec1172a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forecast_values', sa.Column('horizon_minutes', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_forecast_values_horizon_minutes'), 'forecast_values', ['horizon_minutes'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_forecast_values_horizon_minutes'), table_name='forecast_values')
    op.drop_column('forecast_values', 'horizon_minutes')
    # ### end Alembic commands ###