import os
import requests

from container_worker import helper


def xnat_http(connector_access, local_input_file):
    local_file_dir = local_input_file['dir']
    local_file_name = local_input_file['name']
    local_file_path = os.path.join(local_file_dir, local_file_name)

    if not os.path.exists(local_file_dir):
        os.makedirs(local_file_dir)

    xnat_url = connector_access['xnat_url']
    project = connector_access['project']
    subject = connector_access['subject']
    session = connector_access['session']
    container_type = connector_access['container_type']
    container = connector_access['container']
    resource = connector_access['resource']
    file = connector_access['file']
    auth = helper.auth(connector_access.get('auth'))
    ssl_verify = connector_access.get('ssl_verify', True)

    container_types = ['scans', 'reconstructions', 'assessors']
    if container_type not in container_types:
        raise Exception('container_type must be one of {}. Given container_type is: {}'.format(
            ', '.join(container_types), container_type)
        )

    url = '{}/REST/projects/{}/subjects/{}/experiments/{}/{}/{}/resources/{}/files/{}'.format(
        xnat_url.rstrip('/'), project, subject, session, container_type, container, resource, file
    )

    r = requests.get(
        url,
        auth=auth,
        verify=ssl_verify,
        stream=True
    )
    r.raise_for_status()

    with open(local_file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                f.write(chunk)
    r.raise_for_status()

    cookies = r.cookies

    r = requests.delete(
        '{}/data/JSESSION'.format(xnat_url),
        cookies=cookies,
        verify=ssl_verify
    )
    r.raise_for_status()
