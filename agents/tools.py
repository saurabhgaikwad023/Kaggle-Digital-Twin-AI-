import tempfile, subprocess, sys

class Tool:
    def call(self, payload:dict) -> dict:
        raise NotImplementedError

class EchoTool(Tool):
    def call(self, payload:dict) -> dict:
        return {'echo': payload}

class SafePythonExecTool(Tool):
    def call(self, payload:dict) -> dict:
        code = payload.get('code','')
        if not code: return {'error':'no code provided'}
        with tempfile.NamedTemporaryFile(suffix='.py', delete=False) as f:
            f.write(code.encode()); path = f.name
        try:
            out = subprocess.check_output([sys.executable, path], stderr=subprocess.STDOUT, timeout=5)
            return {'output': out.decode()}
        except Exception as e:
            return {'error': str(e)}
