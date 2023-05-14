### sagemaker ###
pip install --upgrade sagemaker

### boto3 ###
pip install --upgrade boto3

### tree ###
sudo yum -y install tree

### AWS CLI ###
# pip install --upgrade awscli
# aws configure
# aws s3 ls s3://s3bucket-kita/

### jupyterlab_s3_browser ###
# (https://github.com/IBM/jupyterlab-s3-browser/blob/master/docs/SAGEMAKER.md)
pip install jupyterlab-s3-browser
jupyter serverextension enable --py jupyterlab_s3_browser
# restart-jupyter-server

### jupyterlab-lsp ###
# (https://github.com/jupyter-lsp/jupyterlab-lsp?sc_channel=sm&sc_campaign=YouTube_Videos&sc_publisher=YOUTUBE&sc_country=japan&sc_geo=JAPAN&sc_outcome=awareness&trk=YouTubeJapan) ###
pip install jupyterlab-lsp
pip install 'python-lsp-server[all]'
# Shift + Tab