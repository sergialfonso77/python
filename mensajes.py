# Formatea el texto en cuatro estilos
def messageFormatter(texto, tipo):
    if (tipo == 'info'):
        return '\033[44m' + ' ' + texto + ' ' + '\033[0m'
    elif (tipo == 'warning'):
        return '\033[43m\033[31m' + ' ' + texto + ' ' + '\033[0m'
    elif (tipo == 'error'):
        return '\033[41m' + ' ' + texto + ' ' + '\033[0m'
    elif (tipo == 'success'):
        return '\033[42m' + ' ' + texto + ' ' + '\033[0m'
    else:
        return '\033[0m' + ' ' + texto + ' ' + '\033[0m'
