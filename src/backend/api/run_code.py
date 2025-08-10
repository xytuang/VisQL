from flask import Blueprint, request, jsonify
import subprocess
import tempfile
import json

run_code_bp = Blueprint('run_code', __name__)

@run_code_bp.route('/run-python', methods=['POST'])
def run_python():
    data = request.get_json()
    code = data.get('code', '')

    if not code:
        return jsonify({'error': 'No code provided'}), 400

    try:
        with tempfile.NamedTemporaryFile('w', suffix='.py', delete=True) as temp_file:
            temp_file.write(code)
            temp_file.flush()

            result = subprocess.run(
                ['python3', temp_file.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=10
            )

        output = result.stdout.decode('utf-8')
        error = result.stderr.decode('utf-8')

        if result.returncode != 0:
            print(error)
            return jsonify({'error': error}), 500

        output = json.loads(output)
        return jsonify({'output': output})

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Code execution timed out'}), 500