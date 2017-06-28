import os
import requests
import tempfile
import zipfile

from container_worker import helper


def xnat_http(connector_access, local_input_file):
    local_file_dir = local_input_file['dir']
    local_file_name = local_input_file['name']
    local_file_path = os.path.join(local_file_dir, local_file_name)

    if not os.path.exists(local_file_dir):
        os.makedirs(local_file_dir)

    download_path = tempfile.mkdtemp()
    zip_file_path = os.path.join(download_path, 'file.zip')
    zip_content_path = os.path.join(download_path, 'zip_content')
    os.mkdir(zip_content_path)

    rest_url = connector_access['rest_url']
    project = connector_access['project']
    subject = connector_access['subject']
    session = connector_access['session']
    scan = connector_access['scan']
    resource = connector_access['resource']

    url = '{}/projects/{}/subjects/{}/experiments/{}/scans/{}/resources/{}/files?format=zip'.format(
        rest_url, project, subject, session, scan, resource
    )

    r = requests.get(
        url,
        auth=helper.auth(connector_access.get('auth')),
        verify=connector_access.get('ssl_verify', True),
        stream=True
    )
    r.raise_for_status()

    with open(zip_file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                f.write(chunk)
    r.raise_for_status()

    z = zipfile.ZipFile(zip_file_path, 'r')
    z.extractall(zip_content_path)
    z.close()

    extracted_file_path = None
    for dirpath, _, files in os.walk(zip_content_path):
        for file in files:
            if extracted_file_path:
                raise Exception('Zip downloaded from XNAT contains more than one file.')
            extracted_file_path = os.path.join(dirpath, file)

    if not extracted_file_path:
        raise Exception('Zip downloaded from XNAT does not contain any file.')

    os.symlink(extracted_file_path, local_file_path)
