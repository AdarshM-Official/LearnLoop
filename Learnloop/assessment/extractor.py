import ast
import complexity

# NOTE ON SAFETY: This module analyzes the code's structure (AST) but DOES NOT
# execute arbitrary user code (using eval() or exec()), which is essential for security.
# Actual sandboxed execution would require Docker/containerization external to Python.

def calculate_ast_metrics(code_snippet):
    """
    Calculates structural features from the Python code's Abstract Syntax Tree (AST).
    
    Features help assess code structure and verbosity.
    """
    try:
        # Parse the code into an AST node
        tree = ast.parse(code_snippet)
    except SyntaxError:
        return None, "SyntaxError: The provided code is not valid Python."

    # 1. Total AST Nodes Count (Proxy for code length/detail)
    node_count = sum(1 for node in ast.walk(tree))

    # 2. Maximum AST Depth (Proxy for nesting/complexity)
    def get_max_depth(node):
        max_depth = 0
        for child in ast.iter_child_nodes(node):
            max_depth = max(max_depth, get_max_depth(child))
        return 1 + max_depth

    max_depth = get_max_depth(tree)

    return {
        "ast_nodes_count": node_count,
        "max_ast_depth": max_depth,
    }, None

def calculate_complexity(code_snippet):
    """
    Calculates Cyclomatic Complexity (a standard metric for code complexity).
    Requires 'radon' or similar library (using a simplified approach here for portability).
    """
    # Using a simplified, common method: counting control flow keywords (if, while, for, and, or)
    complexity_score = 1 # Start with 1 (function entry)
    keywords = ['if', 'while', 'for', 'and', 'or', 'elif']
    
    for line in code_snippet.splitlines():
        for keyword in keywords:
            if keyword in line:
                # Simple count - a robust solution would use a dedicated library like 'radon'
                complexity_score += line.count(keyword)
    
    return complexity_score

def extract_ml_features(code_snippet):
    """
    Master function to run all feature extraction.
    """
    ast_metrics, error = calculate_ast_metrics(code_snippet)
    if error:
        return None, error

    complexity_score = calculate_complexity(code_snippet)
    
    features = {
        **ast_metrics,
        "cyclomatic_complexity": complexity_score,
        # Add more features here (e.g., function count, docstring presence)
    }

    # Ensure the feature vector matches the training order:
    # [ast_nodes_count, max_ast_depth, cyclomatic_complexity]
    feature_vector = [
        features["ast_nodes_count"],
        features["max_ast_depth"],
        features["cyclomatic_complexity"]
    ]
    
    return features, feature_vector
