# SLS AWS Python Hello World
A hello world python REST API, deployed as a AWS Lambda function using serverless framework.

## Deploy to AWS
```shell script
$ sls deploy
```

## Local Development
### Setup serverless offline
```shell script
$ npm init
$ npm install serverless-offline-python --save-dev
```

### Run offline
```shell script
sls offline start
```

## Additional information
### Installing package dependencies
```
(venv) $ pip install numpy
Collecting numpy
  Downloading numpy-1.13.1-cp36-cp36m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (4.5MB)
    100% |████████████████████████████████| 4.6MB 305kB/s
Installing collected packages: numpy
Successfully installed numpy-1.13.1
(venv) $ pip freeze > requirements.txt
(venv) $ cat requirements.txt
numpy==1.13.1
```

### Tail remote logs from command line
```shell script
sls logs -f <function-name-as-defined-in-serverless-yml> -t
```