import json
from urllib.request import Request, urlopen

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'}


def count_zeroes(astring):
    return max([len(i) for i in astring.replace('1', ' ').split()])


def count_ones(astring):
    return max([len(i) for i in astring.replace('0', ' ').split()])


def get_request2dict(url):
    req = Request(url, headers=HEADERS)
    data = urlopen(req).read()
    data_dict = json.loads(data)
    return data_dict


def get_data(last: int):
    data_dict = get_request2dict('https://drand.cloudflare.com/public/latest')
    last_round = data_dict['round']
    results = []
    for round in range(last_round-last+1, last_round+1):
        data_dict = get_request2dict(
            f'https://drand.cloudflare.com/public/{round}')
        results.append(data_dict['randomness'])
    print(results)
    binary_results = [bin(int(i, 16)) for i in results]
    print(binary_results)
    return binary_results


def get_max_zeroes_ones(last):
    data = get_data(last)
    data_ones = [count_ones(i) for i in data]
    data_zero = [count_zeroes(i) for i in data]
    max_ones = max(data_ones)
    max_zero = max(data_zero)
    index_ones = data_ones.index(max_ones)
    index_zeros = data_zero.index(max_zero)
    print(f"Maximum ones in a row   : {max_ones}")
    print(f"Randomness : {data[index_ones]}")
    print(f"Maximum zeroes in a row : {max_zero}")
    print(f"Randomness : {data[index_zeros]}")


if __name__ == '__main__':
    get_max_zeroes_ones(10)
