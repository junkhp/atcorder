# -*- coding: utf-8 -*-
def main():
    n, C = map(int, input().split())
    abc_list = [list(map(int, input().split())) for i in range(n)]
    keikaku_dict = {}
    day_set = set()
    for i, abc in enumerate(abc_list):
        a = abc[0]
        b = abc[1] + 1
        if a in day_set:
            keikaku_dict[a].append([i, True])
        else:
            keikaku_dict[a] = [[i, True]]
            day_set.add(a)

        if b in day_set:
            keikaku_dict[b].append([i, False])
        else:
            keikaku_dict[b] = [[i, False]]
            day_set.add(b)
    day_set = sorted(day_set)

    day_cost = 0
    day_cost_dict = {}
    for day in day_set:
        for xxx in keikaku_dict[day]:
            service = xxx[0]
            is_in = xxx[1]
            if is_in:
                day_cost += abc_list[service][2]
            else:
                day_cost -= abc_list[service][2]
        day_cost_dict[day] = day_cost

    ans = 0
    for i in range(len(day_set) - 1):
        ans += min(C, day_cost_dict[day_set[i]]) * (day_set[i + 1] - day_set[i])

    print(ans)


if __name__ == '__main__':
    main()
