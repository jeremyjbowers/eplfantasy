#!/usr/bin/env python
import json

import requests

def load_players():
    try:
        all_ids = []
        with open('data/players.json', 'r') as readfile:
            for i in list(dict(json.loads(readfile.read()))['elInfo']):
                all_ids.append(i[0])

        with open('data/player_ids.json', 'w') as writefile:
            writefile.write(json.dumps(all_ids))

    except:
        print "Ooops, no players."

def scrape_players():
    with open('data/player_ids.json', 'r') as readfile:
        player_ids = list(json.loads(readfile.read()))

    for i in player_ids:
        if i:
            r = requests.get('http://fantasy.premierleague.com/web/api/elements/%s/' % i)
            if r.status_code == 200:
                player_data = json.loads(r.content)
                with open('data/players/%s.json' % i, 'w') as writefile:
                    writefile.write(json.dumps(player_data))
                print "%s %s (%s)" % (player_data['first_name'], player_data['second_name'], player_data['now_cost'])

if __name__ == "__main__":
    load_players()
    scrape_players()