import os
from pathlib import Path
import jinja2
import click

from os.path import dirname, join
from textx import metamodel_from_file, language, generator
from textx.export import metamodel_export, model_export

from sts_generator.model_processors import check_env_override, duplicate_case_names_check, duplicate_function_names_check
from sts_generator.object_processors import environment_processor


def model_processor(model, metamodel):
    # Errors
    duplicate_function_names_check(model, metamodel)
    duplicate_case_names_check(model, metamodel)
    # Warnings
    check_env_override(model, metamodel)


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

    metamodel_export(tests_mm, join(dot_folder, "metamodel.dot"))

    tests_model = model

    model_export(tests_model, join(dot_folder, "model.dot"))

    print("\nSuccessfully exported dot\n")


@language("ServerlessTestS", "*.sts")
def serverless_unit_test_dsl():
    '''A language for specification of serverless functions unit tests'''
    metamodel_path = join(dirname(__file__), "tests.tx")

    return metamodel_from_file(metamodel_path)


@generator("ServerlessTestS", "sts-dot")
def dot_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generating dot visualizations from ServerlessTestS grammars'''
    try:
        print(
            f"\nGenerating DOT...\n\nModel: ${model}\n\nOutput folder: ${output_path}")

        dot_model_export(model, output_path)
    except Exception as e:
        print("\nDot generator failed due to:\n" + e.__str__())


@generator("ServerlessTestS", "sts")
def tests_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generate Serverless unit tests'''
    try:
        print(
            f"\nGenerating tests...\n\nModel: ${model}\n\nOutput folder: ${output_path}")

        app_generation(model, output_path)
    except Exception as e:
        print("\nTest generator failed due to:\n" + e.__str__())


def sts_generate(textx):
    @textx.command()
    @click.option("--model", default="./serverless.sts", help="Path to the model directory.")
    @click.option("--output", default="./test", help="Path to the output directory.")
    def sts_generate(model, output):
        '''Generate Serverless unit tests'''
        try:
            print(
                f"\nGenerating tests...\n\nModel: ${model}\n\nOutput folder: ${output}")

            metamodel_path = join(dirname(__file__), "tests.tx")

            metamodel = metamodel_from_file(metamodel_path, autokwd=True)

            metamodel.register_model_processor(model_processor)

            metamodel.register_obj_processors(object_processors())

            model_object = metamodel.model_from_file(Path(model))

            app_generation(model_object, output)
        except Exception as e:
            print("\nTest generator failed due to:\n" + e.__str__())


def app_generation(model, output):
    this_folder = Path(__file__).parent.parent

    os.makedirs(output, exist_ok=True)

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    if model.type == "JS":
        jinja_template = jinja_env.get_template(
            "sts_generator/templates/nodejs.template")

        for function in model.functions:

            with open(join(output, f"{function.name}.test.js"), "w") as f:
                f.write(jinja_template.render(
                    function=function, type=model.type))
    else:
        jinja_template = jinja_env.get_template(
            "sts_generator/templates/python.template")

        for function in model.functions:

            with open(join(output, f"test_{function.name}.py"), "w") as f:
                f.write(jinja_template.render(
                    function=function, type=model.type))

    print("\nSuccessfully generated tests\n")
