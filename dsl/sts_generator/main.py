import os
from pathlib import Path
import jinja2

from os.path import dirname, join
from textx import metamodel_from_file, language, generator
from textx.export import metamodel_export, model_export
from textx.exceptions import TextXSemanticError

from sts_generator.model_processors import check_env_override, duplicate_case_names_check, duplicate_function_names_check
from sts_generator.object_processors import environment_processor


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
    metamodel_path = join(dirname(__file__), "tests.tx")

    tests_mm = metamodel_from_file(metamodel_path)

    dot_folder = join(output_path)
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)

    print("Exporting metamodel and model to folder: " + dot_folder)

    metamodel_export(tests_mm, join(dot_folder, "metamodel.dot"))

    tests_model = model

    model_export(tests_model, join(dot_folder, "model.dot"))

    print("Done exporting Dot")


@language("serverless_unit_test_dsl", "*.sts")
def serverless_unit_test_dsl():
    '''A language for specification of serverless unit tests'''
    metamodel_path = join(dirname(__file__), "tests.tx")

    return metamodel_from_file(metamodel_path)


@generator("serverless_unit_test_dsl", "Dot")
def dot_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generating dot visualizations from STS grammars'''
    try:
        dot_model_export(model, output_path)
    except Exception as e:
        print("Dot generator failed due to: \n\n" + e.__str__())


@generator("serverless_unit_test_dsl", "Tests")
def tests_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generate Serverless unit tests'''
    try:
        app_generation(model, output_path)
    except Exception as e:
        print("Test generator failed due to: \n\n" + e.__str__())


def app_generation(model, output_path):
    this_folder = Path(__file__).parent.parent

    os.makedirs(output_path, exist_ok=True)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    print("Generating tests...\nOutput folder: " + output_path)

    metamodel_path = join(dirname(__file__), "tests.tx")

    tests_mm = metamodel_from_file(metamodel_path, autokwd=True)

    tests_mm.register_model_processor(model_processor)

    tests_mm.register_obj_processors(object_processors())

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    if model.type == "JS":
        jinja_template = jinja_env.get_template("sts_generator/templates/nodejs.template")

        for function in model.functions:

            with open(join(output_path, f"{function.name}.test.js"), "w") as f:
                f.write(jinja_template.render(
                    function=function, type=model.type))
    else:
        jinja_template = jinja_env.get_template("sts_generator/templates/python.template")

        for function in model.functions:

            with open(join(output_path, f"test_{function.name}.py"), "w") as f:
                f.write(jinja_template.render(
                    function=function, type=model.type))
    
    print("Successfully generated tests.")
