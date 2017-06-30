import os
import requests

from container_worker import helper


def xnat_http(connector_access, local_result_file, meta_data):
    local_file_dir = local_result_file['dir']
    local_file_name = local_result_file['name']
    local_file_path = os.path.join(local_file_dir, local_file_name)

    xnat_url = connector_access['xnat_url']
    project = connector_access['project']
    subject = connector_access['subject']
    session = connector_access['session']
    resource_type = connector_access['resource_type']
    xsi_type = connector_access['xsi_type']
    file_name = connector_access['file_name']
    auth = helper.auth(connector_access.get('auth'))
    ssl_verify = connector_access.get('ssl_verify', True)

    if resource_type not in ['scans', 'reconstructions', 'assessors']:
        raise Exception('Invalid resource_type: {}'.format(resource_type))

    base_url = '{}/REST/projects/{}/subjects/{}/experiments/{}/{}'.format(
        xnat_url.rstrip('/'), project, subject, session, resource_type
    )

    r = requests.put(
        '{}?xsiType={}'.format(base_url, xsi_type),
        auth=auth,
        verify=ssl_verify
    )
    r.raise_for_status()

    with open(local_file_path, 'rb') as f:
        r = requests.put(
            '{}/resources/OTHER/files/{}?format=OTHER&content=T1_RAW&inbody=true'.format(base_url, file_name),
            data=f,
            cookies=r.cookies,
            verify=ssl_verify
        )
        r.raise_for_status()

    requests.delete(
        '{}/data/JSESSION'.format(xnat_url),
        cookies=r.cookies,
        verify=ssl_verify
    )
