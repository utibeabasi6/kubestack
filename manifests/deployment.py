from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

NAME = ""
IMAGE = ""


def collect_data():
    global NAME, IMAGE
    name_entered = False
    while not name_entered:
        NAME = input("Enter a name for your deployment: ")
        if NAME == "":
            print("Name cannot be blank😂")
        else:
            name_entered = True

    image_entered = False
    while not image_entered:
        IMAGE = input("Enter a Docker image: ")
        if IMAGE == "":
            print("Image cannot be blank")
        else:
            image_entered = True


def generate_template():
    env = Environment(
        loader=PackageLoader("manifests", "templates"),
        autoescape=select_autoescape()
    )
    template = env.get_template("deployment.yaml")
    print("Generating deployment manifest".center(80, "-"))
    return template.render(name=NAME, image=IMAGE)
