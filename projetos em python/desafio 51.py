sexo = str (input('digite o seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'mMFf':
    sexo = str (input('dados invalidos por favor, informe seu sexo: [M/F] ')).stripp().upper()[0]
print ('sexo {} registrado'.format(sexo))

    
