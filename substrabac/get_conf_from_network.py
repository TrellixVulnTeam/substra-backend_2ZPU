'''
Get data generated by substra-network
'''

import os
import grp
import getpass
from subprocess import call
from substrapp.conf import conf

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

dir_path = os.path.dirname(os.path.realpath(__file__))

SUBSTRA_NETWORK_PATH = os.environ.get('SUBSTRA_NETWORK_PATH', os.path.join(dir_path, '../../substra-network/'))
ORGS = ('owkin', 'chu-nantes')
ORDERERS = ('orderer',)
current_user = getpass.getuser()
current_group = grp.getgrgid(os.getgid()).gr_name


def create_core_peer_config():
    for org_name in conf['orgs'].keys():
        org = conf['orgs'][org_name]
        for peer in org['peers']:
            stream = open(os.path.join(dir_path, './core.yaml'), 'r')
            yaml_data = load(stream, Loader=Loader)

            # override template here

            yaml_data['peer']['id'] = peer['host']
            yaml_data['peer']['address'] = '%(host)s:%(port)s' % {'host': peer['host'], 'port': peer['external_port']}
            yaml_data['peer']['localMspId'] = org['org_msp_id']
            yaml_data['peer']['mspConfigPath'] = '../user/msp'

            # yaml_data['peer']['tls']['cert']['file'] = '../tls/' + peer['name'] + '/cli-client.crt'
            # yaml_data['peer']['tls']['key']['file'] = '../tls/' + peer['name'] + '/cli-client.key'
            yaml_data['peer']['tls']['clientCert']['file'] = '../tls/' + peer['name'] + '/cli-client.crt'
            yaml_data['peer']['tls']['clientKey']['file'] = '../tls/' + peer['name'] + '/cli-client.key'
            yaml_data['peer']['tls']['enabled'] = 'true'
            yaml_data['peer']['tls']['rootcert']['file'] = '../ca-cert.pem'
            yaml_data['peer']['tls']['clientAuthRequired'] = 'true'
            yaml_data['peer']['tls']['clientRootCAs'] = ['../ca-cert.pem']

            yaml_data['logging']['level'] = 'debug'

            peer_dir = os.path.join(dir_path, 'substrapp/conf/%(org_name)s/%(peer_name)s' % {
                'org_name': org_name,
                'peer_name': peer['name']})
            if not os.path.exists(peer_dir):
                os.makedirs(peer_dir)
            filename = os.path.join(peer_dir, 'core.yaml')
            with open(filename, 'w+') as f:
                f.write(dump(yaml_data, default_flow_style=False))


def get_conf_from_network():
    for org in ORGS:
        # copy user msp
        call(['sudo', 'cp', '-R',
              os.path.join(SUBSTRA_NETWORK_PATH, 'data/orgs/' + org + '/user'),
              os.path.join(dir_path, './substrapp/conf/' + org)])

        # copy user msp
        call(['sudo', 'cp', '-R',
              os.path.join(SUBSTRA_NETWORK_PATH, 'data/orgs/' + org + '/admin'),
              os.path.join(dir_path, './substrapp/conf/' + org)])

        # copy ca-cert.pem
        call(['sudo', 'cp',
              os.path.join(SUBSTRA_NETWORK_PATH, 'data/orgs/' + org + '/ca-cert.pem'),
              os.path.join(dir_path, './substrapp/conf/' + org)])

        # copy tls cli-client
        call(['sudo', 'cp', '-R',
              os.path.join(SUBSTRA_NETWORK_PATH, 'data/orgs/' + org + '/tls'),
              os.path.join(dir_path, './substrapp/conf/' + org)])

    for org in ORDERERS:
        # copy ca-cert.pem
        org_dir = os.path.join(dir_path, 'substrapp/conf/' + org)
        if not os.path.exists(org_dir):
            os.makedirs(org_dir)
        call(['sudo', 'cp', '-R',
              os.path.join(SUBSTRA_NETWORK_PATH, 'data/orgs/' + org),
              os.path.join(dir_path, 'substrapp/conf/')])

    # modify rights
    call(['sudo', 'chown', '-R', current_user + ':' + current_group,
          os.path.join(dir_path, 'substrapp/conf/')])


if __name__ == "__main__":
    call(['sudo', 'rm', '-Rf', os.path.join(dir_path, 'substrapp/conf')])
    create_core_peer_config()
    get_conf_from_network()
