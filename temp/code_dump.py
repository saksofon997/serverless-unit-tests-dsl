
print("--------")

print(test_suite.type)

print("-------- FIRST FUNCTION")

print("function: ", test_suite.functions[0].__dict__)

print("env: ", test_suite.functions[0].env.__dict__)

print("case: ", test_suite.functions[0].cases[0].__dict__)

print("input: ", test_suite.functions[0].cases[0].input.__dict__)

print("input value: ",
      test_suite.functions[0].cases[0].input.value.__dict__)

print("output: ", test_suite.functions[0].cases[0].output.__dict__)

print("output value: ",
      test_suite.functions[0].cases[0].output.value.__dict__)

print("case: ", test_suite.functions[0].cases[1].__dict__)

print("input: ", test_suite.functions[0].cases[1].input.__dict__)

print("input value: ",
      test_suite.functions[0].cases[1].input.value.__dict__)

print("output: ", test_suite.functions[0].cases[1].output.__dict__)

print("output value: ",
      test_suite.functions[0].cases[1].output.value.__dict__)

print("-------- SECOND FUNCTION")

print("function: ", test_suite.functions[1].__dict__)

# print("env: ", test_suite.functions[1].env.__dict__)

print("cases: ", test_suite.functions[1].cases[0].__dict__)

print("input: ", test_suite.functions[1].cases[0].input.__dict__)

print("output: ", test_suite.functions[1].cases[0].output.__dict__)

print("output value: ", test_suite.functions[1].cases[0].output.value)


# Export to .dot file for visualization
model_export(test_suite, join(dot_folder, 'sts.dot'))

metamodel_export(entity_mm, join(dot_folder, 'sts_meta.dot'))
