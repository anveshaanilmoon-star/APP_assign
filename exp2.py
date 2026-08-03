# Decorator for bold formatting
def bold_text(func):
    def wrapper(title, content):
        result = func(title, content)
        return f"**{result}**"
    return wrapper


# Report Class
class Report:

    # Class variable for storing templates
    templates = {}

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add template
    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    # Class method to retrieve template
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method (__call__)
    def __call__(self, template_name):
        template = Report.get_template(template_name)
        if template:
            return template(self.title, self.content)
        else:
            return "Template not found."

    # String representation
    def __str__(self):
        return f"Report Title : {self.title}\nContent : {self.content}"


# Simple template function
def simple_template(title, content):
    return f"Title : {title}\nContent : {content}"


# Fancy template with bold formatting
@bold_text
def fancy_template(title, content):
    return f"Title : {title}\nContent : {content}"


# Main Function
def main():

    # Add templates
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create report instance
    report = Report(
        "Monthly Sales Report",
        "Sales increased by 20% compared to last month."
    )

    # Display report object
    print("----- Original Report -----")
    print(report)

    # Generate reports
    print("\n----- Simple Template -----")
    print(report("simple"))

    print("\n----- Fancy Template -----")
    print(report("fancy"))


# Run the program
if __name__ == "__main__":
    main()