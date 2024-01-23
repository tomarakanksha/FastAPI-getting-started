# Deploy FastAPI on Render

This repository is for getting started with [FastAPI](https://fastapi.tiangolo.com) service and deploying it on Render.

Below are the steps followed for render deployment:

## Deployment to Render:

1. Create a new Web Service on Render.
2. Specify the URL to your git repository.
3. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
4. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

## For more infomation on render deployment

Check out this: https://render.com/docs/deploy-fastapi