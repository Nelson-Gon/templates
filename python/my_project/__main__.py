def main():
    from my_project.hello_world import HelloWorld
    import argparse

    args_parser = argparse.ArgumentParser()

    # Add args as required

    args_parser.add_argument("-t", "hello-text", required=True, default="Hello World")

    # Make boolean
    def make_bool(in_str):
        bools_dict = {"True":True, "TRUE":True,1:True,"1":True,
                      "T":True, "False": False, "F": False, "0": False,
                      "FALSE": False, 0: False}
        if in_str:
            return bools_dict[in_str]


    use_arguments = args_parser.parse_args()
    # Create a HelloWorld object
    use_object = HelloWorld(use_arguments.hello_text)

    try:
        use_object.print_text()
    except Exception:
        # TODO: Use specific Exception
        raise
    else:
        print("Thank you for using my_project, please provide feedback at https://github.com/Nelson-Gon/my_project")


if __name__=="__main__":
    main()


