"""V0_3

Revision ID: 4e211bc2f98e
Revises: 518cb6aff9b3
Create Date: 2023-12-22 15:53:54.678837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e211bc2f98e'
down_revision: Union[str, None] = '518cb6aff9b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follow_request',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('request_user_id', sa.UUID(), nullable=False),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.Column('request_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['request_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_follow_request_request_user_id'), 'follow_request', ['request_user_id'], unique=False)
    op.create_index(op.f('ix_follow_request_user_id'), 'follow_request', ['user_id'], unique=False)
    op.add_column('Post_comment_reply', sa.Column('post_id', sa.UUID(), nullable=False))
    op.add_column('Post_comment_reply', sa.Column('reply_like_count', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_Post_comment_reply_post_id'), 'Post_comment_reply', ['post_id'], unique=False)
    op.create_foreign_key(None, 'Post_comment_reply', 'posts', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Post_comment_reply', type_='foreignkey')
    op.drop_index(op.f('ix_Post_comment_reply_post_id'), table_name='Post_comment_reply')
    op.drop_column('Post_comment_reply', 'reply_like_count')
    op.drop_column('Post_comment_reply', 'post_id')
    op.drop_index(op.f('ix_follow_request_user_id'), table_name='follow_request')
    op.drop_index(op.f('ix_follow_request_request_user_id'), table_name='follow_request')
    op.drop_table('follow_request')
    # ### end Alembic commands ###
