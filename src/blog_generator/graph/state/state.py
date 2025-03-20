# src/blog_generator/graph/state/state.py
class WorkflowState:
    def __init__(self):
        self.user_inputs = {}
        self.user_stories = []
        self.design_documents = {}
        self.code = ""
        self.test_cases = []
        self.qa_results = ""
        self.deployment_status = ""
        self.monitoring_data = ""
        self.maintenance_updates = ""
        self.user_stories_approved = False
        self.design_approved = False
        self.code_approved = False
        self.security_approved = False
        self.test_cases_approved = False

    def update(self, data):
        self.__dict__.update(data)

    def get(self, key):
        return self.__dict__.get(key)