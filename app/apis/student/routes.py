from .resources.signin.login import StudentLogin
def initialize_routes(api):
    api.add_resource(StudentLogin, '/student-login')