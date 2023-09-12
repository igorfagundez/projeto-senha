import numpy as np
import string as st

letras = st.ascii_letters
numeros = st.digits
especial = st.punctuation
algarismos = letras+numeros+especial

senha = np.random.choice(list(algarismos),10)

print("A senha sera:",''.join(senha))
