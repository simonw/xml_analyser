import argparse
import json
import sys
from . import ElementStats, ET


def pprint(stats):
    print(json.dumps(stats, indent=4))


def main(args=None, pprint=pprint):
    parser = argparse.ArgumentParser(
        description="Display a summary of elements in an XML file"
    )
    parser.add_argument("filepath", type=str, help="Path to the XML file")
    res = parser.parse_args(args)
    try:
        et = ET.parse(open(res.filepath))
    except Exception as e:
        print(e)
        sys.exit(1)
    pprint(ElementStats(et).stats)
