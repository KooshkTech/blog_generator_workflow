# src/blog_generator/graph/nodes/deployment.py
def deployment(state):
    state.update({"deployment_status": "Deployed"})
    return state