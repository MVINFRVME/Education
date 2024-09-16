from datetime import datetime
from collections import OrderedDict

start_time_str = input()
start_time = datetime.strptime(start_time_str, '%H:%M:%S')

req = int(input())


def print_stats(ordered_results: OrderedDict):
    place = 1
    skipped_place = 0
    previous_res = None
    for name, res in ordered_results.items():
        if not previous_res:
            previous_res = res
            skipped_place = -1
        if previous_res[:2] != res[:2]:
            place += 1 + skipped_place
            skipped_place = 0
        else:
            skipped_place += 1
        print(f"{place} {name} {res[0]} {res[1]}")


def calculate_fine(time, result, server, start_time):
    if result == 'FORBIDEN' or result == 'DENIED':
        return 20, None
    elif result == 'ACCESSED':
        return (time - start_time).seconds // 60, server


d = {}
previous = None
for _ in range(req):
    line = input()
    team, time_str, server, result = line.split()
    if team not in d:
        d[team] = [set(), 0, None]

    time = datetime.strptime(time_str, '%H:%M:%S')

    if d[team][2] is None:
        d[team][2] = (time - start_time).seconds // 3600
    else:
        diff = (time - start_time).seconds // 3600
        if diff < 0:
            diff += 24
        if diff < d[team][2]:
            continue

    fine, server = calculate_fine(time, result, server, start_time)
    d[team][1] += fine
    if server:
        d[team][0].add(server)

for val in d.values():
    val[0] = len(val[0])

od = OrderedDict(sorted(d.items(), key=lambda item: (item[1][0], item[1][1])))
print_stats(od)
