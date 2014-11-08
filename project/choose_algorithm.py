
class RelationNode:
    """
    class that describes relationship between men and women in voting
    id - id of participant
    preferable_ids - ids person would like to ask out
    """
    def __init__(self, id, preferable_ids):
        self.__id = id
        self.__preferable_ids = preferable_ids

    def set_range(self, likes_amount):
        self.__likes_amount = likes_amount

    @property
    def get_id(self):
        return self.__id

    @property
    def preferences(self):
        return self.__preferable_ids[:]

    def rate(self, judges):
        return len(filter((lambda x: self.get_id in x.preferences), judges))

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        prefs = ', '.join(map(str, self.preferences))
        return 'id = {0}, preferences = [{1}]'.format(self.__id, prefs)


def check_list_arg(arg):
    for item in arg:
        if not isinstance(item, RelationNode):
            raise TypeError('items of lists must be RelationNode')


def choose_algo(men, women):
    """ algorithm of picking dating pairs after voting"""
    if not isinstance(men, list) or not isinstance(women, list):
        raise TypeError('args should be lists of RelationNode')
    check_list_arg(men)
    check_list_arg(women)
    men_sorted = sort_by_rating(men, women)
    women_sorted = sort_by_rating(women, men)
    men_sorted.reverse()
    women_sorted.reverse()
    result = []
    for man in men_sorted:
        try:
            chosen_woman = \
                filter(lambda x: x.get_id in man.preferences, women_sorted)[0]
            women_sorted = filter(lambda x: x != chosen_woman, women_sorted)
        except:
            pass
        else:
            result.append((man, chosen_woman))
    return result


def sort_by_rating(list_to_sort, list_sorted_by):
    return sorted(list_to_sort, key=lambda x: x.rate(list_sorted_by))


if __name__ == "__main__":
    men = [RelationNode(1, [2, 4, 5]),
           RelationNode(2, [2, 3, 1]),
           RelationNode(3, [1, 2, 4]),
           RelationNode(4, [2, 4, 5]),
           RelationNode(5, [1, 2, 3]),
           ]
    women = [RelationNode(1, [2, 4, 5]),
             RelationNode(2, [2, 3, 1]),
             RelationNode(3, [1, 2, 4]),
             RelationNode(4, [2, 4, 5]),
             RelationNode(5, [1, 2, 3]),
    ]

    result = choose_algo(men, women)

    for x in result:
        print(str(x[0]) + " dates " + str(x[1]))
