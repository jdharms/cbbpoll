"""Initialize Consumption Tags

Revision ID: 1a5977b16f8
Revises: 1fda3b446166
Create Date: 2014-10-20 02:20:10.006133

"""

# revision identifiers, used by Alembic.
revision = '1a5977b16f8'
down_revision = '1fda3b446166'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy.sql import table

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('voter_application', 'will_participate',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    ### end Alembic commands ###

    tags_table = table('consumption_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=160), nullable=True),    )
    op.bulk_insert(tags_table,
        [
 {'id': 1 ,'text': "I rarely go to games, and instead focus on TV broadcasts and streams."},
 {'id': 2 ,'text': "I try to go to a few games each year."},
 {'id': 3 ,'text': "I go to either my team's game or some other game most or all weeks."},
 {'id': 4 ,'text': "I pick a few games each week to watch intently."},
 {'id': 5 ,'text': "I try to follow everything going on using multiple TVs and/or monitors."},
 {'id': 6 ,'text': "I tend to focus on watching my team and/or games that could effect their standing."},
 {'id': 7 ,'text': "I tend to focus on watching match-ups between highly ranked teams."},
 {'id': 8 ,'text': "I tend to focus on watching match-ups in my team's conference."},
 {'id': 9 ,'text': "I tend to focus on watching match-ups between closely matched teams regardless of ranking."},
 {'id': 10, 'text': "I watch the weeknight games regardless of the teams playing."},
 {'id': 11, 'text': "I gamble or participate in contests trying to predict the outcome of games and follow my progress as games go on."},
 {'id': 12, 'text': "My experience as a basketball player, coach, or referee tends to guide my focus."}
        ])



def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('voter_application', 'will_participate',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    ### end Alembic commands ###
