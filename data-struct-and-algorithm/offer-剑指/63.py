# -*- coding: utf-8 -*-

'''63、股票的最大利润'''


__author__ = 'happyin3 (happyinx3@gmail.com)'


def get_max_diff(prices):
    if len(prices) < 2:
        return 0

    min_num = prices[0]
    max_diff = prices[1] - min_num

    for i in range(2, len(prices)):
        min_num = prices[i-1] if prices[i-1] < min_num else min_num

        cur_diff = prices[i] - min_num
        max_diff = cur_diff if cur_diff > max_diff else max_diff

    return max_diff


if __name__ == '__main__':
    prices = [9, 11, 8, 5, 7, 12, 16, 14]
    max_diff = get_max_diff(prices)
    print(max_diff)
