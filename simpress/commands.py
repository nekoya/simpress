import argparse

from simpress import builder, logger, web


def build_parser():
    parser = argparse.ArgumentParser(description='simpress bootstrap script')
    subparsers = parser.add_subparsers(help='sub-command help')

    publish_parser = subparsers.add_parser('publish',
                                           help='Publish static HTML files')
    publish_parser.set_defaults(func='publish')

    preview_parser = subparsers.add_parser('preview', help='Preview on web')
    preview_parser.add_argument('-p', '--port', type=int, default=3776)
    preview_parser.set_defaults(func='preview')
    return parser


def execute():
    logger.setup()
    parser = build_parser()
    args = parser.parse_args()
    if 'func' not in args:
        parser.error('please specify subcommand')
    globals().get(args.func)(args)


def preview(args):
    web.create_app().run(host='0.0.0.0', port=args.port)


def publish(args):
    builder.build()
