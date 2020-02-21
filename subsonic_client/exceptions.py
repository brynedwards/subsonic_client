class ErrorResponse(Exception):
    def __init__(self, status, code, response_message):
        self.status = status
        self.code = code
        self.response_message = response_message
        self.message = f"Subsonic responded with {status}: '{response_message}'"
