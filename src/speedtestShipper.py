import os
import json
import datetime as dt
from sys import exit, argv
import sys
import subprocess


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config

from termcolor import colored

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import requests

class speedtestShipper(object):


    def __init__(self, verbose):

        print("[1] Authenticating with AWS.")
        self.auth_with_aws()
        print("[2] Running SpeedtestCLI.")
        self.get_data()
        print(self.data)
        print("[3] Connection to ES.")
        self.connect_to_es()
        #self.test_this()
        print("[4] Pushing data to index.")
        self.push_data_to_index()
        print()
        print()
    
    def auth_with_aws(self):
        self.awsAuth = AWS4Auth(
            config.AWS_ES_ENDPOINT['aws_access_key_id'],
            config.AWS_ES_ENDPOINT['aws_secret_access_key'],
            config.AWS_ES_ENDPOINT['region'], 
            config.AWS_ES_ENDPOINT['service'])

    def connect_to_es(self):

        self.esClient = Elasticsearch(
            hosts = [{'host': config.AWS_ES_ENDPOINT['host'], 'port': 443}],
            #http_auth = self.awsAuth,
            use_ssl = True,
            verify_certs = True,
            connection_class = RequestsHttpConnection
        )

    def parse_data(self):
        return None

    def get_data(self):
        #self.data = os.system("speedtest -f json")  
        self.data = subprocess.run(['speedtest', '-f', 'json'], stdout=subprocess.PIPE).stdout.decode('utf-8')

    def push_data_to_index(self):
        self.esClient.index(
            index=config.ES_INDEX['index'],
            doc_type=config.ES_INDEX['doc_type'],
            body=self.data
            )