# -*- coding: utf-8 -*-
 
    
def decision_root(tree):
    node_dict = {}
    tree_dict = {}
    for edge in tree:
        for i in range(2):
            try:
                node_dict[edge[i]] += 1
            except KeyError:
                node_dict[edge[i]] = 1
            
        try:
            tree_dict[edge[0]].add(edge[1])
        except:
            tree_dict[edge[0]] = set([edge[1]])
        try:
            tree_dict[edge[1]].add(edge[0])
        except:
            tree_dict[edge[1]] = set([edge[0]])
    max_value = 0
    for key, value in node_dict.items():
        if value > max_value:
            max_value = value
            max_key = key
    print(node_dict)
    return max_key, tree_dict


def main():
    n = int(input())
    tree = [list(map(int, input().split())) for i in range(n - 1)]
    num_query = int(input())
    query_list = [list(map(int, input().split())) for i in range(num_query)]
    print(tree)
    print(query_list)
    print(decision_root(tree))


if __name__ == '__main__':
    main()
