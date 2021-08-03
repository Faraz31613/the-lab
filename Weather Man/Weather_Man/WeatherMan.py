import argparse
from ReportCreator import ReportCreator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help="input file", metavar="FILE")
    parser.add_argument("-e", "--year", type=str, action='append')
    parser.add_argument("-a", "--month", type=str, action='append')
    parser.add_argument("-c", "--graph", type=str, action='append')
    args = parser.parse_args()
    file_path = args.path
    years_for_reporting = args.year
    months_for_reporting = args.month
    months_for_graph_report = args.graph
    months_list = ["Jan", "Feb", "Mar", "Apr", "May",
                   "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if not years_for_reporting:
        pass
    else:
        for x in range(len(years_for_reporting)):
            yearly_report_creator = ReportCreator()
            yearly_report_creator.year_report(
                file_path, years_for_reporting[x], months_list)

    if not months_for_reporting:
        pass
    else:
        for x in range(len(months_for_reporting)):
            year, month = months_for_reporting[x].split("/")
            month = months_list[int(month)-1]
            monthly_report_creator = ReportCreator()
            monthly_report_creator.monthly_report(file_path, year, month)

    if not months_for_graph_report:
        pass
    else:
        for x in range(len(months_for_graph_report)):
            year, month = months_for_reporting[x].split("/")
            month = months_list[int(month)-1]
            monthly_graph_creator = ReportCreator()
            monthly_graph_creator.monthly_graph(file_path, year, month)


main()
