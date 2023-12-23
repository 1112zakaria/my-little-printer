# my-little-printer

## Dependencies for Windows Native environment
Requires Anaconda environment, Python version < 3.11; I use Python 3.10

Install Anaconda: https://www.anaconda.com/download

In the Anaconda prompt:
```
conda create --name <env-name> python=3.10
conda activate <env-name>
```
Requires Tensorflow 2.10
```
pip install tensorflow==2.10
```
Requires cudatoolkit and cudnn
```
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
```

## Requirements
- Setup .env file with PERSONAL_ACCESS_TOKEN variable