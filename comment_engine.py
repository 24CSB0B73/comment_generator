#def generate_comment(feature): #new file instead of coment generator for better approach

 #   name = feature["name"]
  #  params = feature["parameters"]

    #comment = f"Function '{name}' "

    #if feature["operations"]:
     #   comment += f"performs {feature['operations'][0]} "

    #if feature["has_loop"]:
     #   comment += "using iteration "

    #if feature["has_condition"]:
     #   comment += "with conditional logic "

    #if params:
     #   comment += f"on parameters {', '.join(params)} "

    #if feature["return_value"]:
     #   comment += f"and returns {feature['return_value']}."
#
    #return comment
def generate_comment(ir, analysis):

    name = ir["name"]
    params = ir["parameters"]

    comment = f"The function '{name}' "

    if analysis:
        comment += ", ".join(analysis)

    if params:
        comment += f" on parameters {', '.join(params)}"

    if ir["return"]:
        comment += f" and returns {ir['return']}"

    comment += "."

    return comment