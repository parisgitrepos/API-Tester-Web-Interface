from flask import Flask, request, render_template
import json
from backend import get_request, post_request, put_request

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', ENDPOINT = '', HEADERS = '', PAYLOAD = '',
                               RESPONSE = 'No response received yet')
    elif request.method == 'POST':
        endpoint = request.form.get('endpoint')
        method = request.form.get('method')
        headers = request.form.get('headers')
        payload = request.form.get('payload')

        if headers != '':
            try:
                # Converts headers HTML input of type str (i.e. '{"key":"value"}') to type dict (i.e. {"key":"value")
                headers = json.loads(headers)

                # JSON very particular about ' vs ", only latter is acceptable
                # However, when Python converts dict objects to str objects, any str value within dict is given '
                # headers_str not only converts dict to str but within string also converts any instance of ' to "
                headers_str = str(headers).replace("'", '"')

            except json.decoder.JSONDecodeError:
                return render_template('index.html', ENDPOINT = endpoint, HEADERS = headers,
                                       PAYLOAD = payload, RESPONSE = 'Headers incorrectly formatted')
        else:
            headers = None
            headers_str = ''

        if payload != '':
            try:
                # Converts payload HTML input of type str (i.e. '{"key":"value"}') to type dict (i.e. {"key":"value")
                payload = json.loads(payload)

                # JSON very particular about ' vs ", only latter is acceptable
                # However, when Python converts dict objects to str objects, any str value within dict is given '
                # payload_str not only converts dict to str but within string also converts any instance of ' to "
                payload_str = str(payload).replace("'", '"')

            except json.decoder.JSONDecodeError:
                return render_template('index.html', ENDPOINT = endpoint, HEADERS = headers,
                                       PAYLOAD = payload, RESPONSE = 'Payload incorrectly formatted')
        else:
            payload = None
            payload_str = ''

        if method == 'GET':
            response = get_request(endpoint, headers, payload)
            return render_template('index.html', ENDPOINT = endpoint, HEADERS = headers_str, PAYLOAD = payload_str,
                                   RESPONSE = response)
        elif method == 'POST':
            response = post_request(endpoint, headers, payload)
            return render_template('index.html', ENDPOINT = endpoint, HEADERS = headers_str, PAYLOAD = payload_str,
                                   RESPONSE = response)
        elif method == 'PUT':
            response = put_request(endpoint, headers, payload)
            return render_template('index.html', ENDPOINT = endpoint, HEADERS = headers_str, PAYLOAD = payload_str,
                                   RESPONSE = response)


if __name__ == '__main__':
    app.run()
