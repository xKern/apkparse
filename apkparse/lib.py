import hashlib
import subprocess
import xmltodict
from yaml import (
    load as yaml_load,
    Loader as yaml_loader
)


class APKParse:
    def __init__(self, apk_path, output_path='./apk-parse-output'):
        self.apk_path = apk_path
        self.output_path = output_path
        self.yaml = None
        self.xml = None
        self.bundle_id = None
        self.release_type = None
        self.version_id = None
        self.version_code = None
        self.version_name = None
        self.version = None
        self.checksum = None

    def read_yaml(self):
        path = self.output_path + '/apktool.yml'
        file = open(path)
        yaml_content = file.readlines()
        file.close()
        """
        apktool adds a line here that makes it invalid json.
        lets remove it
        """
        del yaml_content[0]
        yaml_content = '\n'.join(yaml_content)
        loaded = yaml_load(yaml_content, yaml_loader)
        self.yaml = loaded

    def read_xml(self):
        path = self.output_path + '/AndroidManifest.xml'
        file = open(path)
        xml_content = file.read()
        file.close()
        self.xml = xmltodict.parse(xml_content)

    def extract_information(self):
        self.version_code = self.yaml.get('versionInfo').get('versionCode')
        self.version_name = self.yaml.get('versionInfo').get('versionName')
        self.version = self.yaml.get('version')

        self.version_id = self.xml['manifest']['application']['meta-data'][0]['@android:value']
        self.release_type = int(self.xml['manifest']['application']['meta-data'][1]['@android:value'])
        self.bundle_id = self.xml['manifest']['@package']

    def generate_checksum(self):
        checksum = hashlib.sha1()
        with open(self.apk_path, 'rb') as f:
            while True:
                data = f.read(63536)
                if not data:
                    break
                checksum.update(data)
        self.checksum = checksum.hexdigest()

    def work(self):
        runs = ['apktool', 'decode', self.apk_path, '-o', self.output_path]
        subprocess.run(runs)
        self.read_yaml()
        self.read_xml()
        self.extract_information()
        self.generate_checksum()
