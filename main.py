"""TAR Extract Win — Extract tar and tar.gz archives on Windows into a folder, with a file list first."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='tar_extract_win',
        description='Extract tar and tar.gz archives on Windows into a folder, with a file list first.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('TAR Extract Win')
    print('A tarball without a Unix box.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
