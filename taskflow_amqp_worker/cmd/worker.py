import sys
import urlparse

from oslo.config import cfg

from taskflow.engines.worker_based import worker as w

from taskflow_amqp_worker.common import log
from taskflow_amqp_worker import version



opts = [
    cfg.StrOpt('amqp_url', required=True,
               help='MQ URL like amqp://192.168.122.1:5672/'),
    cfg.StrOpt('exchange', required=True, default='taskflow',
               help='MQ exchange name'),
    cfg.StrOpt('topic', required=True, default='workers',
               help='MQ topic'),
    cfg.ListOpt('tasks', required=True,
                help='List of tasks like mytasks:CallJoe,mytasks:CallJim')
    ]


CONF = cfg.CONF
CONF.register_cli_opts(opts, 'taskflow')


def parse(args):
    cfg.CONF(args=args, project='universal-worker',
             version='%%prog %s' % version.VERSION)
    return cfg.CONF.config_file


def parse_sys_args():
    return parse(sys.argv[1:])


def check_amqp_url():
    parsed = urlparse.urlparse(CONF.taskflow.amqp_url)
    if parsed.scheme != 'amqp':
        logging.getLogger(__name__).error(
            'Configuration error: Bad AMQP URL scheme in "%s". '
            'Expected "amqp".\n' % CONF.taskflow.amqp_url)
        exit(1)


def main():
    parse_sys_args()

    log.configure_logging()

    check_amqp_url()

    worker_config = {
        'url': CONF.taskflow.amqp_url,
        'exchange': CONF.taskflow.exchange,
        'topic': CONF.taskflow.topic,
        'tasks': CONF.taskflow.tasks
        }

    worker = w.Worker(**worker_config)

    worker.run()
