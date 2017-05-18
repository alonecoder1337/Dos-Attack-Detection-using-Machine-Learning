from Classifier import Classififer
import pandas as pd
import numpy as np
from Dataset import Dataset


class App:
    def __init__(self):
        self.classifier = Classififer().get_classifier();


    def train(self):
        df = pd.read_csv('data/train.csv', header=None)
        data = np.array(df)
        self.x_train = data[:, :-1]
        self.y_train = data[:, -1:]
        self.classifier.fit(self.x_train,self.y_train)

    def test(self):
        self.ds_obj = Dataset()
        ds = self.ds_obj.read_dataset()
        new_ds = []
        for row in ds:
            new_ds.append(row[1:])
        self.x_test = np.array(new_ds)
        self.results = self.classifier.predict(self.x_test)

    def post_test(self):
        client_ip_ids = []
        total_test,_ = self.x_test.shape

        for i in range(total_test):
            if self.results[i]==1 :
                if self.x_test[i,1] not in client_ip_ids:
                    client_ip_ids.append(self.x_test[i,1])
        dos_ips = self.ds_obj.detransform_client_ip(np.array(client_ip_ids,dtype="int64"))
        for ip in dos_ips:
            print ip

    def run(self):
        self.train()
        self.test()
        self.post_test()


if __name__ == '__main__':
    app = App()
    app.run()


