import os
# import pandas as pd

project_dir = os.getenv("PROJECT_DIR")
env = os.getenv("DEFAULT_ENV")
# iris_csv = os.getenv("IRIS")

# flowers = pd.read_csv(iris_csv)

# print(flowers)
print("My project directory is {} and my conda environment is {}".format(project_dir, env))

print('Hello World')
