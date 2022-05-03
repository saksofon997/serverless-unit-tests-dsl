# TEST
this_folder = dirname(__file__)


def main():
    metamodel_path = join(dirname(__file__), 'tests.tx')

    entity_mm = metamodel_from_file(metamodel_path, autokwd=True)

    entity_mm.register_model_processor(model_processor)

    entity_mm.register_obj_processors(object_processors())

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Build Test Suite model from serverless.sts file
    test_suite = entity_mm.model_from_file(join(this_folder, 'serverless.sts'))

    if test_suite.type == "JS":
        tests_folder = join(this_folder, 'tests_js')
        if not os.path.exists(tests_folder):
            os.mkdir(tests_folder)

        jinja_template = jinja_env.get_template("templates/nodejs.template")

        for function in test_suite.functions:

            with open(join(f"tests_js", f"{function.name}.test.js"), 'w') as f:
                f.write(jinja_template.render(
                    function=function, type=test_suite.type))
    else:
        tests_folder = join(this_folder, 'tests_py')
        if not os.path.exists(tests_folder):
            os.mkdir(tests_folder)

        jinja_template = jinja_env.get_template("templates/python.template")

        for function in test_suite.functions:

            with open(join(f"tests_py", f"test_{function.name}.py"), 'w') as f:
                f.write(jinja_template.render(
                    function=function, type=test_suite.type))


if __name__ == "__main__":
    main()
