"""initial

Revision ID: 2e2854bfd4a5
Revises: 
Create Date: 2023-03-02 20:46:10.386448

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2e2854bfd4a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delivery',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('added_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('comment', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('operation_category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_table('product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('count', sa.Float(), nullable=True),
                    sa.Column('cost', sa.Float(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('permissions', sa.JSON(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('number', sa.String(), nullable=False),
                    sa.Column('hashed_password', sa.String(), nullable=False),
                    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('client',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('number', sa.String(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('order',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('added_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('completed', sa.Boolean(), nullable=False),
                    sa.Column('client_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('operation',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('added_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('amount', sa.Float(), nullable=True),
                    sa.Column('order_id', sa.Integer(), nullable=True),
                    sa.Column('operation_category_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['operation_category_id'], ['operation_category.id'], ),
                    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('order_product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('added_at', sa.TIMESTAMP(), nullable=True),
                    sa.Column('completed', sa.Boolean(), nullable=False),
                    sa.Column('count', sa.Float(), nullable=True),
                    sa.Column('order_id', sa.Integer(), nullable=True),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.Column('delivery_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['delivery_id'], ['delivery.id'], ),
                    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('operation')
    op.drop_table('operation_category')
    op.drop_table('delivery')
    op.drop_table('order_product')
    op.drop_table('order')
    op.drop_table('client')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###