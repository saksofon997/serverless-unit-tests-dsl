from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx import metamodel_from_file, language, generator
from textx.export import metamodel_export, model_export


def get_entity_mm():
    metamodel_path = join(dirname(__file__), 'tests.tx')

    entity_mm = metamodel_from_file(metamodel_path)

    return entity_mm


def dot_model_export(model, output_path):
    entity_mm = get_entity_mm()

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
    return get_entity_mm()

@generator("serverless_unit_test_dsl", "Dot")
def dot_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generating dot visualizations from sTs grammars'''
    try:
        dot_model_export(model, output_path)
    except Exception as e:
        print("Dot generator failed due to: \n\n" + e.__str__())

#TEST
this_folder = dirname(__file__)

def main(debug=False):

    entity_mm = get_entity_mm()

    # Export to .dot file for visualization
    dot_folder = join(this_folder, 'dotexport')
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)
    metamodel_export(entity_mm, join(dot_folder, 'sts_meta.dot'))

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'serverless.sts'))

    # Export to .dot file for visualization
    model_export(person_model, join(dot_folder, 'sts.dot'))


if __name__ == "__main__":
    main()