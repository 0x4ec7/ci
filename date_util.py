
class DateUtil(object):

    @staticmethod
    def is_leap_year(year):
        if year % 100 != 0 and year % 4 == 0:
            return True
        if year % 400 == 0:
            return True
        return False

    @staticmethod
    def day_of_year(year, month, day):
        assert year > 0
        assert 1 <= month <= 12
        base = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if DateUtil.is_leap_year(year):
            base[1] = 29
        assert 1 <= day <= base[month-1]
        days = 0
        for i in range(month-1):
            days += base[i]
        days += day
        return days


def main():
    y = int(input('year: '))
    m = int(input('month: '))
    d = int(input('day: '))
    print('day of year: {}'.format(DateUtil.day_of_year(y, m, d)))


if __name__ == '__main__':
    main()
