def safe_report(report: list) -> [bool, int]:
    if report[0] - report[1] > 0 and abs(report[0] - report[1]) <= 3:
        increasing = False
    elif report[0] - report[1] < 0 and abs(report[0] - report[1]) <= 3:
        increasing = True
    else:
        return False, 0

    for idx, xy in enumerate(zip(report[1:-1], report[2:])):
        x, y = xy
        if not 1 <= abs(x - y) <= 3:
            return False, idx+1
        elif x - y > 0 and increasing:
            return False, idx+1
        elif x - y < 0 and not increasing:
            return False, idx+1

    return True, -99


def parse_input(filename: str, dampener: bool = False) -> int:
    input_file = open(filename, 'r')
    lines = input_file.readlines()

    safe_reports = 0
    for this_line in lines:
        this_report = [int(x) for x in this_line.strip().split()]
        this_report_safe, idx = safe_report(this_report)

        if not this_report_safe and dampener:
            option_1 = this_report[0:idx]+this_report[idx+1:]
            option_2 = this_report[0:idx+1] + this_report[idx + 2:]
            this_report_safe_1, idx = safe_report(option_1)
            this_report_safe_2, idx = safe_report(option_2)

            if idx>0:
                option_3 = this_report[0:idx-1] + this_report[idx:]
                this_report_safe_3, idx = safe_report(option_3)
            else:
                this_report_safe_3 = False

            if idx+3 < len(this_report):
                option_4 = this_report[0:idx + 2] + this_report[idx + 3:]
                this_report_safe_4, idx = safe_report(option_4)
            else:
                this_report_safe_4=False

            this_report_safe = any([this_report_safe_1,
                                   this_report_safe_2,
                                   this_report_safe_3,
                                   this_report_safe_4])

        safe_reports += 1 if this_report_safe else 0

    return safe_reports
