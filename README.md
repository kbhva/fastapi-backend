## Setting up the project

If you're running the project for the first time, make a Virtual Environment by running this command:

```bash
python -m venv chatbot_env
```

On UNIX based systems, run the following command to activate the virual environment

```bash
source chatbot_env/bin/activate
```

On Windows, run the following command to activate the virtual environment

```bash
chatbot_env\Scripts\activate
```

Install the required libraries in the Virtual Environment by running this command

```bash
pip install -r requirements.txt
```

## Making API Calls

The API is built on FastAPI in Python.

The API accepts only `POST` requests, so you need to make a request by the following set of commands.

```bash
python main.py
uvicorn main:app --reload
```

This will run the API, most probably on the `localhost` or `http://127.0.0.1` on port `8080`. Now to make a request, you need to add a request body. To simply do it, you can go to `http://127.0.0.1/docs`, this will open the Swagger UI interactive window, and click `Try it out` to try with different `input_text` parameters, and then Execute the API call.
