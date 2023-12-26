from django import template
#from censor_list import censor_list

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    return str(value) * arg

@register.filter(name='censor')
def censor(value):
    value1 = (str(value)).split()
    censor_list1 = ['дебил',
                   'дурак',
                   'придурок',
                   'козел'
                   ]
    censor_list = []
    with open('censor_list.txt', 'r') as f:
        censor_list = f.read().split(", ")

    for i, word in enumerate(censor_list):
        for j, word1 in enumerate(value1):
            if word1 == word:
                value1[j] = "*"
    value = ' '.join(value1)
    return str(value)