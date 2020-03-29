# simple lambda expresion


var_sqr = lambda x: x * x

y = var_sqr(3)
print(y)

var_exp = lambda x, y: x + y
print(var_exp(3, 5))

# lambda & map combining

##For processing all elements in a list , listing the result and indicating which lambda expresion
## is used  and the group of variable what are being the input.
lited_var = [1, 2, 3, 4, 5]
var_sqr_list = list(map(var_sqr, lited_var))
print(var_sqr_list, lited_var)

# Combining  lambda with filter

varList_filtered = list(filter(lambda x: x % 2 == 0, lited_var))
print(varList_filtered)

# Dict and Lambdas

dictList = [{'valor1': 10},
            {'valor1': 2},
            {'valor1': 3}]
dictList = sorted(dictList, key=lambda x: x['valor1'])
print(dictList)

# Nesting Lambda exp

add_suffix = lambda suffix: (lambda myStr: myStr + ' ' + suffix)

strprefix = add_suffix('http://')
y = strprefix('URL:')
x = strprefix('rrrrr ')
print(y, x)
