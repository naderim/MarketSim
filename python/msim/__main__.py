#!/usr/bin/env python3

"""
@author: Mohsen Naderi (mohsen@mnaderi.com)
"""

import itertools
import logging
import os
import random
import re
import string
import sys
import traceback


#from .experiment_config import experiment_config_cli
#from .experiment_runner import experiment_runner_java_cli
#from .experiment_results import get_equilibrium


__version = 0.1
__svn_date = '$Date$'
__updated_date = __svn_date[7:17]


def main(argv=None):
    """
    Command line options.
    """
    logging.basicConfig(format='%(asctime)s.%(msecs)d - %(name)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
    logging.info("Starting ...")

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version
    program_build_date = "%s" % __updated_date
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = ('%s\n' + \
                       'Created by Mohsen Naderi on %s.\n' + \
                       'Copyright 2014-2020 Mohsen Naderi (mohsen@mnaderi.com). All rights reserved.\n') \
                       % (program_shortdesc, str(__updated_date))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", default=0,
                            help="set verbosity level [default: %(default)s]")

        cmd_parsers = parser.add_subparsers(dest='command', help='sub-command to run')
        cmd_parsers.required = True

        #experiment_config_cli(cmd_parsers)
        #experiment_runner_java_cli(cmd_parsers)

        #parser_gen_config = cmd_parsers.add_parser('get_equilibrium', help='get equilibrium')
        #parser_gen_config.add_argument("-c", "--config", dest="config_file", required=True, help="config file")
        #parser_gen_config.set_defaults(func=get_equilibrium)

        # process options
        opts = parser.parse_args(argv)

        if opts.verbose > 0:
            logging.getLogger().setLevel(level=logging.DEBUG)
            logging.debug('enabled DEBUG level logging')

        logging.debug( "argv: %s" % argv )
        logging.debug( "opts: %s" % opts )
        opts.func(opts)

    except KeyboardInterrupt as e:
        logging.error( 'Got Interrupted : "%s"' % e)
        return 0
    except Exception as e:
        logging.error( 'Got Exception : "%s"' % e)
        traceback.print_exc(file=sys.stdout)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        traceback.print_exc()
        return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
