from langgraph.graph import StateGraph, END
from src.blog_generator.graph.nodes import generate_user_stories, design_documents, generate_code, write_test_cases, deployment, monitoring, maintenance
from src.blog_generator.graph.state.state import WorkflowState

def create_graph():
    workflow = StateGraph(WorkflowState)

    # Add nodes
    workflow.add_node("generate_user_stories", generate_user_stories.generate_user_stories)
    workflow.add_node("design_documents", design_documents.generate_design_documents)
    workflow.add_node("generate_code", generate_code.generate_code)
    workflow.add_node("write_test_cases", write_test_cases.write_test_cases)
    workflow.add_node("deployment", deployment.deployment)
    workflow.add_node("monitoring", monitoring.monitoring)
    workflow.add_node("maintenance", maintenance.maintenance)

    # Add edges
    workflow.add_edge("generate_user_stories", "design_documents")
    workflow.add_edge("design_documents", "generate_code")
    workflow.add_edge("generate_code", "write_test_cases")
    workflow.add_edge("write_test_cases", "deployment")
    workflow.add_edge("deployment", "monitoring")
    workflow.add_edge("monitoring", "maintenance")
    workflow.add_edge("maintenance", END)

    # Set the entry point
    workflow.set_entry_point("generate_user_stories")

    # Compile the graph
    return workflow.compile()