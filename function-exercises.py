def list_benefits():
  return "More organized code", "More readable code", "Easier code reuse"," Allowing programmers to share and connect code together"


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefits in list_of_benefits:
        print(build_sentence(benefits))

name_the_benefits_of_functions()
