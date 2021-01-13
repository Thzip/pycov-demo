import argparse
import xml.etree.ElementTree as ET

cov_file = "coverage.xml"


def check_rate(package, rate_threshold):
    tree = ET.parse(cov_file)
    root = tree.getroot()
    # package = root.find(f"packages/package[@name='{package}']") # when using --cov=source.apps.app1
    package = root.find(f"packages/package[@name='.']")  # when using --cov=source/apps/app1
    cov_rate = float(package.attrib['line-rate'])
    assert cov_rate >= rate_threshold, f'code coverage not enough, expect: >= {rate_threshold}, actual:{cov_rate}'


def __parse_args():
    arg_parser = argparse.ArgumentParser('Parse code coverage result and check against threshold')
    arg_parser.add_argument('-P', '--package', dest='package', action='store', required=True, help='package under test')
    arg_parser.add_argument('-R', '--rate-threshold', dest='rate_threshold', type=float, action='store', default=0.8,
                            help='unittest code coverage threshold')
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = __parse_args()
    check_rate(args.package, args.rate_threshold)
