from riotwatcher import LolWatcher, ApiError

api = 'yourapikey'

lol_watcher = LolWatcher(api)

name = input('소환사의 이름을 입력하세요 : ')

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, name)

nick = me.get('name')
lvl = me.get('summonerLevel')

my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])

stat = my_ranked_stats[0]

tier = stat.get('tier')
rank = stat.get('rank')
queue = stat.get('queueType')

print('─────────────────────────────────────────────────────────────────────')

print(f'닉네임 : {nick}, 레벨 : {lvl}, 티어 : {tier}{rank}({queue})')

matchlist = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])

match = lol_watcher.match.by_id(my_region, matchlist[0])

info = match.get('info')
participants = info.get('participants')

row = 0

for i in participants:
    infoplayer = i.get('summonerName')
    if infoplayer == nick:
        kills = i.get('kills')
        deaths = i.get('deaths')
        assists = i.get('assists')

        champ = i.get('championName')
        pos = i.get('teamPosition')

        result = i.get('win')

        if result == True:
            result = '승리'
        if result == False:
            result = '패배'

        print(f'최근 전적 | 챔피언 : {champ}, KDA : {kills}/{deaths}/{assists}, 포지션 : {pos}, 승패여부 : {result}')

print('─────────────────────────────────────────────────────────────────────')

input()