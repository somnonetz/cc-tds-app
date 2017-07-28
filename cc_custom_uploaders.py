import os
import requests

from cc_container_worker.commons import helper


def xnat_http(connector_access, local_result_file, meta_data):
    local_file_dir = local_result_file['dir']
    local_file_name = local_result_file['name']
    local_file_path = os.path.join(local_file_dir, local_file_name)

    xnat_url = connector_access['xnat_url']
    project = connector_access['project']
    subject = connector_access['subject']
    session = connector_access['session']
    container_type = connector_access['container_type']
    container = connector_access['container']
    resource = connector_access.get('resource', 'OTHER')
    xsi_type = connector_access['xsi_type']
    file = connector_access['file']
    auth = helper.auth(connector_access.get('auth'))
    ssl_verify = connector_access.get('ssl_verify', True)

    container_types = ['scans', 'reconstructions', 'assessors']
    if container_type not in container_types:
        raise Exception('container_type must be one of {}. Given container_type is: {}'.format(
            ', '.join(container_types), container_type)
        )

    base_url = '{}/REST/projects/{}/subjects/{}/experiments/{}/{}/{}'.format(
        xnat_url.rstrip('/'), project, subject, session, container_type, container
    )

    r = requests.put(
        '{}?xsiType={}'.format(base_url, xsi_type),
        auth=auth,
        verify=ssl_verify
    )
    r.raise_for_status()

    cookies = r.cookies

    with open(local_file_path, 'rb') as f:
        r = requests.put(
            '{}/resources/{}/files/{}?format=OTHER&content=T1_RAW&inbody=true'.format(base_url, resource, file),
            data=f,
            cookies=cookies,
            verify=ssl_verify
        )
        r.raise_for_status()

    r = requests.delete(
        '{}/data/JSESSION'.format(xnat_url),
        cookies=cookies,
        verify=ssl_verify
    )
    r.raise_for_status()
