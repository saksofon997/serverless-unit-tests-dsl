from __future__ import unicode_literals
import json
import os
from os.path import dirname, join
from textx import metamodel_from_file, language, generator
from textx.export import metamodel_export, model_export
import jinja2


def dot_model_export(model, output_path):
    metamodel_path = join(dirname(__file__), 'tests.tx')

    entity_mm = metamodel_from_file(metamodel_path)

    # Export to .dot file for visualization
    dot_folder = join(output_path)
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)

    print("Exporting metamodel and model to folder: " + dot_folder)

    metamodel_export(entity_mm, join(dot_folder, 'metamodel.dot'))

    entity_model = model

    model_export(entity_model, join(dot_folder, 'model.dot'))

    print("Done exporting Dot")


@language("serverless_unit_test_dsl", "*.sts")
def serverless_unit_test_dsl():
    '''A language for specification of serverless apps unit tests'''
    metamodel_path = join(dirname(__file__), 'tests.tx')

    return metamodel_from_file(metamodel_path)


@generator("serverless_unit_test_dsl", "Dot")
def dot_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generating dot visualizations from sTs grammars'''
    try:
        dot_model_export(model, output_path)
    except Exception as e:
        print("Dot generator failed due to: \n\n" + e.__str__())


# TEST
this_folder = dirname(__file__)


def main():
    metamodel_path = join(dirname(__file__), 'tests.tx')

    entity_mm = metamodel_from_file(metamodel_path)

    # Export to .dot file for visualization
    tests_folder = join(this_folder, 'tests')
    if not os.path.exists(tests_folder):
        os.mkdir(tests_folder)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Build Test Suite model from serverless.sts file
    test_suite = entity_mm.model_from_file(join(this_folder, 'serverless.sts'))

    if test_suite.type == "JS":
        jinja_template = jinja_env.get_template("nodejs.template")

        for function in test_suite.functions:

            with open(join(f"tests", f"{function.name}.test.js"), 'w') as f:
                f.write(jinja_template.render(
                    function=function, type=test_suite.type))
    else:
        jinja_template = jinja_env.get_template("python.template")

        for function in test_suite.functions:

            with open(join(f"tests", f"test_{function.name}.py"), 'w') as f:
                f.write(jinja_template.render(
                    function=function, type=test_suite.type))


if __name__ == "__main__":
    main()
