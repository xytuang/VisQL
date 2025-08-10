class SemanticChecker:
    def __init__(self):
        self.constraint_manager = ConstraintManager()
        self.join_manager = JoinManager()

    def check(self, query):
        # Placeholder for semantic checks
        pass

    def report_errors(self):
        if self.errors:
            for error in self.errors:
                print(f"Error: {error}")
        else:
            print("No semantic errors found.")