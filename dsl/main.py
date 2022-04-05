import os
import jinja2

from os.path import dirname, join
from textx import metamodel_from_file, language, generator
from textx.export import metamodel_export, model_export
from textx.exceptions import TextXSemanticError

from model_processors import check_env_override, duplicate_case_names_check, duplicate_function_names_check
from object_processors import environment_processor


def model_processor(model, metamodel):
    try:
        # Errors
        duplicate_function_names_check(model, metamodel)
        duplicate_case_names_check(model, metamodel)
        # Warnings
        check_env_override(model, metamodel)
    except TextXSemanticError as e:
        print(e.message)


def object_processors():
    return {
        "Environment": environment_processor
    }


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

    entity_mm = metamodel_from_file(metamodel_path, autokwd=True)

    # Register model processor on the meta-model instance
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

        jinja_template = jinja_env.get_template("nodejs.template")

        for function in test_suite.functions:

            with open(join(f"tests_js", f"{function.name}.test.js"), 'w') as f:
                f.write(jinja_template.render(
                    function=function, type=test_suite.type))
    else:
        tests_folder = join(this_folder, 'tests_py')
        if not os.path.exists(tests_folder):
            os.mkdir(tests_folder)

        jinja_template = jinja_env.get_template("python.template")

        for function in test_suite.functions:

            with open(join(f"tests_py", f"test_{function.name}.py"), 'w') as f:
                f.write(jinja_template.render(
                    function=function, type=test_suite.type))


if __name__ == "__main__":
    main()
