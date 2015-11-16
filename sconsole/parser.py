# Import python libs
import logging
import optparse
import os

# Import salt libs
import salt.config


logger = logging.getLogger()


def parse():
    '''
    Parse the command line input
    '''
    parser = optparse.OptionParser()
    parser.add_option(
            '--theme',
            dest='theme',
            default='std',
            help='Set the color theme to use from std or bright')
    parser.add_option(
            '-c',
            '--config-dir',
            dest='config_dir',
            default='/etc/salt',
            help='The config dir')
    options, args = parser.parse_args()
    opts = options.__dict__
    master_config = os.path.join(opts['config_dir'], 'master.conf')
    logger.debug('Reading config file: {0}'.format(master_config))
    opts.update(salt.config.master_config(master_config))
    opts['color'] = False
    return opts
