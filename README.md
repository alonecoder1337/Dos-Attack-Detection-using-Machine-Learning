## Welcome to GitHub




## Installation

`sudo apt-get install python-setuptools python-numpy python-scipy python-matplotlib python-pip -y`
 
`sudo pip install numpy scipy matplotlib scikit-learn luminol`




## Setting up Logs

You must give the location of log files in order to run this program. Following is the log format for any web server

"%d-%b-%Y %T::::%a::::%m::::%s::::%B::::%D::::%U::::%r"

%d is date

%b is month

%Y is Year

%T is Time (hour:min:sec in 24hour clock format)

%a is client ip address

%m is the request method

%s is status code

%B is size of response in bytes

%D is time taken to serve the request

%U is the url path




## Running Procedure

`python App.py [-h] train_filepath test_filepath`



## Contributions

Contributors are always welcome.I am ready to accept contributions.



## Dataset

Dataset can be obtained using WireShark on Ubuntu
