#!/usr/bin/env python
#######################################################################################################################
#  This API is to perform various docker configuration operations and visualize the graf on UI.                       #
#  Usage:                                                                                                             #
#         import docker_api											                                                  #
# 	                                                                                                                  #
#  __author__ @hkathiria                                                                                              #
#  __version__ 1.0                                                                                                    #
#                                                                                                                     #
#######################################################################################################################

try:
    import requests, json, sys, os
except ImportError:
    print("Modules request, json, sys, os are not importable. please make sure you have python installed properly")

from requests.exceptions import ConnectionError
from docker import Client
from io import BytesIO
import docker


class DockerOrchestration(object):
    """
    Class to perform operations on docker for various data source manipulations, updating configurations and handle users.
    """
    def __init__(self, headers, docker_host, docker_port, payload=None):
        """
        Initialize the grafana connection object necessary to perform any configuration or object manipulation
        :param api_key:
        :param headers:
        :param docker_host:
        :param docker_port:
        :return:
        """
        if not docker_host:
            raise ValueError("Docker hostname value is %s missing. Instance cannot be initialized" % docker_host)

        if not docker_port:
            raise ValueError("Docker hostport value is %s missing. Instance cannot be initialized" % docker_port)

        if not headers:
            raise ValueError("Docker connection header value is missing. Instance cannot be initialized")

        if not isinstance(docker_host, str):
            raise ValueError("Docker hostname must be of string type")

        if not isinstance(headers, dict):
            raise ValueError("Docker deader  must be of dict type")

        self.headers = headers
        self.docker_host = docker_host
        self.docker_port = docker_port
        self.payload = payload
        self.docker_client = Client(base_url='unix:///var/run/docker.sock')
        self.client = docker.from_env(assert_hostname=False)

    def create_docker_container(self, command=None):
        """
        To create the new container on the VM
        :return:
        """
        container = self.docker_client.create_container(image='busybox:latest', command='/bin/sleep 30')
        print("Container created : %s" % container)

    def update_docker_container(self):
        """
        To update the existing docker container
        :return:
        """
        update_container = self.docker_client.update_container()
        print (update_container)


    def create_docker_volume(self, command=None):
        """
        Create and register a named volume
        :param command:
        :return:
        """
        volume = self.docker_client.create_volume(name='foobar', driver='local', driver_opts={'foo': 'bar', 'baz': 'false'})
        print(volume)

    def create_docker_network(self, name_of_network, driver, options=None):
        """
        To create a network
        :param name_of_network:
        :param driver:
        :param options:
        :return:
        """
        network = self.docker_client.create_network(name='foobar', driver='local', driver_opts={'foo': 'bar', 'baz': 'false'})
        print(network)

    def connect_container_to_network(self, container_id_or_name=None, network_id=None):
        """
        TO connect a container to network
        :return:
        """
        network = self.docker_client.connect_container_to_network('%s', '%s') % (container_id_or_name, network_id)
        print(network)

    def disconnect_container_to_network(self, container_id_or_name=None, network_id=None):
        """
        TO connect a container to network
        :return:
        """
        network = self.docker_client.disconnect_container_from_network('%s', '%s') % (container_id_or_name, network_id)
        print(network)

    def docker_version(self):
        """
        To return the version of current running docker on the server.
        :return:
        """
        version = self.docker_client.version()
        return version

    def get_docker_volumes(self):
        """
        To get the volumes of currently registered by the docker daemon
        :return:
        """
        volumes = self.docker_client.volumes()
        print(volumes)

    def get_docker_version(self, client):
        """
        To get the docker version
        :return:
        """
        version_number = self.client.version()
        print(version_number)

    def create_container_with_mount_docker_tempfs(self, name=None, cmd=None, payload=None):
        """
        To create a container with the specified paths to be mounted with tmpfs.
        :param name:
        :param cmd:
        :param payload:
        :return:
        """
        create_container = self.docker_client.create_container()
        pass

    def build_docker(self, dockerfile=None, ):
        """
        To build the docker from the docker file.
        :return:
        """
        f = BytesIO(dockerfile.encode('utf-8'))
        response = [line for line in self.docker_client.build(fileobj = f, rm = True, tag = 'yourname/volume' )]
        print (response)

    def get_docker_images(self):
        """
        TO list the docker images
        :return:
        """
        image_list = self.docker_client.images()
        print (image_list)

    def get_docker_image(self, docker_image_name=None):
        """
        To get an image from docker daemon.
        :return:
        """
        image = self.docker_client.get_image("fedora:latest")
        image_tar = open('/tmp/fedora - latest.tar', 'w')
        image_tar.write(image.data)
        image_tar.close()

    def import_docker_image(self):
        """
        To import docker image.
        :return:
        """
        image_list = self.docker_client.import_image()
        print (image_list)

    def import_docker_image_from_data(self):
        """
        To import image from data
        :return:
        """
        image_list = self.docker_client.import_image_from_data()
        print (image_list)

    def import_docker_image_from_image(self):
        """
        To import image from data
        :return:
        """
        image_list = self.docker_client.import_image_from_image()
        print (image_list)

    def import_docker_image_from_stream(self):
        """
        To import image from data
        :return:
        """
        image_list = self.docker_client.import_image_from_stream()
        print (image_list)

    def import_docker_image_from_url(self):
        """
        To import image from data
        :return:
        """
        image_list = self.docker_client.import_image_from_url()
        print (image_list)

    def get_docker_networks(self):
        """
        Get the list of network for the dockers
        :return:
        """
        network_list = self.docker_client.networks()
        print(network_list)

    def push_docker_image_to_repository(self, dockerfile=None, ):
        """
        To build the docker from the docker file.
        :return:
        """
        f = BytesIO(dockerfile.encode('utf-8'))
        response = [line for line in self.docker_client.build(fileobj = f, rm = True, tag = 'yourname/volume' )]
        print(response)

    def pull_docker_image_to_repository(self, dockerfile=None, ):
        """
        To pull the docker image from repository
        :param dockerfile:
        :return:
        """

        for line in self.docker_client.pull('busybox', stream=True):
            print(json.dumps(json.loads(line), indent=4))

    def search_docker_image(self, docker_image_name=None):
        """
        To search and return docker image
        :param docker_image_name:
        :return:
        """
        response = self.docker_client.search('%s') % docker_image_name
        print(response[:2])

    def start_docker_container(self, docker_image_name=None, docker_command=None):
        """
        To start the docker after it has created.
        :param docker_image_name:
        :param docker_command:
        :return:
        """
        container = self.docker_client.create_container(image = 'busybox:latest', command = '/bin/sleep 30')
        response = self.docker_client.start(container=container.get('Id'))
        print(response)

    def restart_docker_container(self, container_dict=None, time_out=None):
        """
        To re-start the docker after it has created.
        :param docker_image_name:
        :param docker_command:
        :return:
        """
        response = self.docker_client.restart(container_dict, time_out)
        print(response)

    def check_status_for_docker_container(self, container_name=None):
        """
        To generate the statistics for the specific container.
        :param docker_image_name:
        :param docker_command:
        :return:
        """
        stats_obj = self.docker_client.stats('elasticsearch')
        #self.docker_client.stop('elasticsearch')
        for stat in stats_obj:
            print(stat)

    def remove_docker_image(self, dockerfile=None, ):
        """
        To remove docker image
        :param dockerfile:
        :return:
        """
        response = [line for line in self.docker_client.push('yourname/app', stream=True)]
        print(response)
