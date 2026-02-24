# End-to-end-Machine-Learning-Wine-Quality-Analysis-Project-with-MLflow

### Workflows
Update config.yaml            (config/config.yaml)
Update schema.yaml             
Update params.yaml            
Update the entity             (entity/__init__.py)
Update the configuration manager in src config    (src/winequality/config/configuration.py)
Update the components    (src/winequality/components)
Update the pipeline      (src/winequality/pipeline) 
Update the main.py  
Update the app.py



# How to run?
### STEPS:
Clone the repository

```bash
https://github.com/desaiprasad1989/End-to-end-Machine-Learning-Wine-Quality-Analysis-Project-with-MLflow
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlprojects python=3.8 -y
```

```bash
conda activate mlprojects
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)


import dagshub
dagshub.init(repo_owner='desaiprasad1989', repo_name='End-to-end-Machine-Learning-Wine-Quality-Analysis-Project-with-MLflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


MLFLOW_TRACKING_URI=https://dagshub.com/desaiprasad1989/End-to-end-Machine-Learning-Wine-Quality-Analysis-Project-with-MLflow.mlflow
MLFLOW_TRACKING_USERNAME=desaiprasad1989
MLFLOW_TRACKING_PASSWORD=5bb761db3566d027396855e19669995db3293aee
python script.py

Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/desaiprasad1989/End-to-end-Machine-Learning-Wine-Quality-Analysis-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=desaiprasad1989

export MLFLOW_TRACKING_PASSWORD=5bb761db3566d027396855e19669995db3293aee
```

