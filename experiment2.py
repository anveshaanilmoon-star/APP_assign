
def bold_text(func):
    def wrapper(report):
        return "=="*20 + "\n" + func(report) +"\n"+ "=="*20
    return wrapper



class Report:

    templates = {}

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @classmethod
    def get_template(cls, name):
        return cls.templates[name]

    def __call__(self, template_name):
        template = Report.get_template(template_name)
        return template(self)

    def __str__(self):
        return self.title + "\n" + self.content


def simple_template(report):
    return str(report)


@bold_text
def fancy_template(report):
    return str(report)


def main():

    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    report = Report("Monthly Report", "Sales increased by 20%")

    print("Simple Report")
    print(report("simple"))

    print("\nFancy Report")
    print(report("fancy"))


if __name__ == "__main__":
    main()