import sklearn
import numpy as np
from utils.LogHelper import Logs
from utils.DateUtil import get_microseconds
from utils.Anomaly import Anomaly
from sklearn import preprocessing


class Dataset:

    def __init__(self):

        self.logs = Logs().read()
        self.client_ip_label_encoder = preprocessing.LabelEncoder()
        self.request_method_label_encoder = preprocessing.LabelEncoder()
        self.request_status_label_encoder = preprocessing.LabelEncoder()
        self.request_size_label_encoder = preprocessing.LabelEncoder()
        self.time_taken_to_serve_label_encoder =preprocessing.LabelEncoder()
        self.user_agent_label_encoder =preprocessing.LabelEncoder()
        self.request_header_label_encoder = preprocessing.LabelEncoder()

        self.scores = []
        self.client_ips = []
        self.request_methods = []
        self.request_status = []
        self.request_size = []
        self.times_taken_to_serve = []
        self.user_agents = []
        self.request_headers = []

        self.dataset = []

    def preprocess_time(self):
        timestamp_clusters = {}
        for row in self.logs:
            timestamp = get_microseconds(row[0])
            if timestamp not in timestamp_clusters:
                timestamp_clusters[timestamp]=0
            timestamp_clusters[timestamp] = timestamp_clusters[timestamp] + 1
        anomaly_scores = Anomaly().detect(timestamp_clusters)
        for row in self.logs:
            self.scores.append(anomaly_scores[row[0]])

    def preprocess_client_ip(self):
        self.client_ip_label_encoder.fit([row[1] for row in self.logs])
        inst = [row[1] for row in self.logs]
        self.client_ips = self.client_ip_label_encoder.transform(inst)

    def preprocess_request_method(self):
        self.request_method_label_encoder.fit([row[2] for row in self.logs])
        inst = [row[2] for row in self.logs]
        self.request_methods = self.request_method_label_encoder.transform(inst)

    def preprocess_request_status(self):
        self.request_status_label_encoder.fit([row[3] for row in self.logs])
        inst = [row[3] for row in self.logs]
        self.request_status = self.request_status_label_encoder.transform(inst)

    def preprocess_request_size(self):
        self.request_size_label_encoder.fit([row[4] for row in self.logs])
        inst = [row[4] for row in self.logs]
        self.request_size = self.request_size_label_encoder.transform(inst)

    def preprocess_time_taken_to_serve(self):
        self.time_taken_to_serve_label_encoder.fit([row[5] for row in self.logs])
        inst = [row[5] for row in self.logs]
        self.times_taken_to_serve = self.time_taken_to_serve_label_encoder.transform(inst)

    def proprocess_user_agent(self):
        self.user_agent_label_encoder.fit([row[6] for row in self.logs])
        inst = [row[6] for row in self.logs]
        self.user_agents = self.user_agent_label_encoder.transform(inst)

    def preprocess_request_header(self):
        self.request_header_label_encoder.fit([row[7] for row in self.logs])
        inst = [row[7] for row in self.logs]
        self.request_headers = self.request_header_label_encoder.transform(inst)

    def detransform_client_ip(self, client_ip_list):
        return self.client_ip_label_encoder.inverse_transform(client_ip_list)

    def preprocess(self):

        self.preprocess_time()
        self.preprocess_client_ip()
        self.preprocess_request_method()
        self.preprocess_request_status()
        self.preprocess_request_size()
        self.preprocess_time_taken_to_serve()
        self.proprocess_user_agent()
        self.preprocess_request_header()

        dataset_size = len(self.logs)
        for i in range(dataset_size):
            obj = [
                self.logs[i][0],
                self.scores[i],
                self.client_ips[i],
                self.request_methods[i],
                self.request_status[i],
                self.request_size[i],
                self.times_taken_to_serve[i],
                self.user_agents[i],
                self.request_headers[i]
            ]
            self.dataset.append(obj)

    def read_dataset(self):
        self.preprocess()
        return self.dataset


if __name__=='__main__':
    dataset_obj = Dataset()
    dataset_obj.preprocess()