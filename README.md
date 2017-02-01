# boston_order
IVR call tree for info on travel ban for Boston residents


Uses Python 3.5

```
pip install -r requirements.txt
```

Make a copy of each `.yml` file in `/config`, removing the ".example".

Once the configs are properly completed, run:

```
python scripts/setup.py
```

You will be prompted to create an admin email and password.
Then run:

```
python test/run_dev.py
```

and go to `localhost:8899/login` to login as admin