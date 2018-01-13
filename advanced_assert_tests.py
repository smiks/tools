def assert_dict_contains(dict_a, dict_b):
    if dict_a == dict_b:
        return True

    def check(d_a, d_b):
        if type(d_a) != type(d_b):
            return False

        if d_a == d_b:
            return True

        keys_b = d_b.keys()
        for k, v in d_a.items():
            # Key does not exist in d_b, return False
            if k not in keys_b:
                return False

            # Key exists in d_b, check deeper
            type_v = type(v)
            type_b = type(d_b[k])

            # Matching keys don't have matching values
            if type_v != type_b:
                return False

            if type_v is list or type_v is set:
                # iterate through d_a[k]
                res = []
                for x in v:
                    if type(x) is dict:
                        for y in d_b[k]:
                            if type(y) is dict:
                                tmp = check(x, y)
                                res.append(tmp)
                return any(res)
            return k == d_b.get(k)

    return check(dict_a, dict_b)


if __name__ == "__main__":
    a = {'scores': [{'user': 'BugHunter', 'score': 31084}]}
    b = {'scores': [{'user': 'BugHunter', 'score': 39349}, {'user': 'BugHunter', 'score': 36945}, {'user': 'BugHunter', 'score': 36704}, {'user': 'BugHunter', 'score': 34252}, {'user': 'BugHunter', 'score': 32584}, {'user': 'BugHunter', 'score': 31084}, {'user': 'BugHunter', 'score': 30619}, {'user': 'BugHunter', 'score': 30069}, {'user': 'Ax', 'score': 12440}, {'user': 'BugHunter', 'score': 10316}], 'response_code': 201, 'response_message': 'Created'}
    c = {'scores': [{'score': 39349, 'user': 'BugHunter'}, {'user': 'BugHunter', 'score': 36945}, {'user': 'BugHunter', 'score': 36704}, {'user': 'BugHunter', 'score': 34252}, {'user': 'BugHunter', 'score': 32584}, {'user': 'BugHunter', 'score': 31084}, {'user': 'BugHunter', 'score': 30619}, {'user': 'BugHunter', 'score': 30069}, {'user': 'Ax', 'score': 12440}, {'user': 'BugHunter', 'score': 10316}], 'response_code': 201, 'response_message': 'Created'}
    d = {'scores': [{'scores': [{'user': 'BugHunter', 'score': 31084}]}]}
    ret = assert_dict_contains(b, c)
    print("Compare B and C")
    assert ret == True

    ret = assert_dict_contains(a, b)
    print("Compare A and B ")
    assert ret == True

    ret = assert_dict_contains(a, d)
    print("Compare A and D ")
    assert ret == False

