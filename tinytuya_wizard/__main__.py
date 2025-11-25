import argparse
import logging
from .wizard import wizard
from tinytuya import SCANTIME, DEVICEFILE, SNAPSHOTFILE, CONFIGFILE, RAWFILE

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('max_time', nargs='?', type=int, default=SCANTIME, help=f"Maximum time to find Tuya devices [Default: {SCANTIME}]")
  parser.add_argument('-force', '-f', action='store_true', help='Force network scan of device IP addresses')
  parser.add_argument('-nocolor', action='store_true', help='Disable color text output')
  parser.add_argument('-yes', '-y', action='store_true', help='Answer yes to all questions')
  parser.add_argument('-no-poll', '-no', action='store_true', help='Answer no to polling (overrides -yes)')
  parser.add_argument('-device-file', default=DEVICEFILE, metavar='FILE', help=f"JSON file to load/save devices [Default: {DEVICEFILE}]")
  parser.add_argument('-credentials-file', default=CONFIGFILE, metavar='FILE', help=f"JSON file to load/save cloud credentials [Default: {CONFIGFILE}]")
  args = parser.parse_args()

  logging.basicConfig(level=logging.INFO)

  wizard(
    user_code=None,
    color=not args.nocolor,
    retries=args.max_time,
    forcescan=args.force,
    assume_yes=args.yes,
    skip_poll=args.no_poll,
    DEVICEFILE=args.device_file,
    SNAPSHOTFILE=SNAPSHOTFILE,
    CREDSFILE=args.credentials_file
  )

if __name__ == "__main__":
  main()
