# exec-dash

Set-up new Anaconda environment from which to run dashboard:
```sh    
conda create -n dashboard-env python=3.7 # (first time only)
conda activate dashboard-env
```

From inside the virtual environment, use pip to install package dependencies:
```sh
    pip install -r requirements.txt
```