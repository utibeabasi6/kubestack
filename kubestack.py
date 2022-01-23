import sys

def print_intro():
    intro = ["",
    "Welcome To",
    "",
    """  __  _  __ __  ____     ___   _____ ______   ____     __  __  _     
    |  |/ ]|  |  ||    \   /  _] / ___/|      | /    |   /  ]|  |/ ]    
    |  ' / |  |  ||  o  ) /  [_ (   \_ |      ||  o  |  /  / |  ' /     
    |    \ |  |  ||     ||    _] \__  ||_|  |_||     | /  /  |    \     
    |     ||  :  ||  O  ||   [_  /  \ |  |  |  |  _  |/   \_ |     |    
    |  .  ||     ||     ||     | \    |  |  |  |  |  |\     ||  .  |    
    |__|\_| \__,_||_____||_____|  \___|  |__|  |__|__| \____||__|\_|  """,
    "",
    ""]

    for string in intro:
        print(string.center(80, "+"))

manifests = [
    "Deployment",
    "Service",
    "Ingress",
]

def main():
    print_intro()
    print("Here are the manifests we currently support")
    for index, manifest in enumerate(manifests):
        print(f"{index + 1})", manifest, sep="  ")

    manifest_selected = False
    while not manifest_selected:
        manifest = input("Select the manifest you want to generate or enter q to quit: ").title()
        if manifest == "Q":
            sys.exit()
        if manifest in manifests:
            manifest_selected = True
        else:
            print("Sorry we do not currently support this manifest")
    
    if manifest == "Deployment":
        import manifests.deployment as deployment
        deployment.collect_data()
        manifest = deployment.generate_template()
        with open("deployment.yaml", "w") as f:
            f.write(manifest)

if __name__ == "__main__":
    main()