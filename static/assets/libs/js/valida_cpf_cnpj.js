function TestaCPF(elemento) {
  cpf = elemento.value;
  cpf = cpf.replace(/[^\d]+/g, '');
  if (cpf == '') return regeita_cpf(elemento);
  // Elimina CPFs invalidos conhecidos    
  if (cpf.length != 11 ||
    cpf == "00000000000" ||
    cpf == "11111111111" ||
    cpf == "22222222222" ||
    cpf == "33333333333" ||
    cpf == "44444444444" ||
    cpf == "55555555555" ||
    cpf == "66666666666" ||
    cpf == "77777777777" ||
    cpf == "88888888888" ||
    cpf == "99999999999")
    return regeita_cpf(elemento);
  // Valida 1o digito 
  add = 0;
  for (i = 0; i < 9; i++)
    add += parseInt(cpf.charAt(i)) * (10 - i);
  rev = 11 - (add % 11);
  if (rev == 10 || rev == 11)
    rev = 0;
  if (rev != parseInt(cpf.charAt(9)))
    return regeita_cpf(elemento);
  // Valida 2o digito 
  add = 0;
  for (i = 0; i < 10; i++)
    add += parseInt(cpf.charAt(i)) * (11 - i);
  rev = 11 - (add % 11);
  if (rev == 10 || rev == 11)
    rev = 0;
  if (rev != parseInt(cpf.charAt(10)))
   return regeita_cpf(elemento);
  return aceita_cpf(elemento);
}

function validarCNPJ(cnpj) {
    elemento = cnpj
    cnpj = cnpj.value;
 
    cnpj = cnpj.replace(/[^\d]+/g,'');
 
    if(cnpj == '') return regeita_cnpj()
     
    if (cnpj.length != 14) return regeita_cnpj()

 
    // Elimina CNPJs invalidos conhecidos
    if (cnpj == "00000000000000" || 
        cnpj == "11111111111111" || 
        cnpj == "22222222222222" || 
        cnpj == "33333333333333" || 
        cnpj == "44444444444444" || 
        cnpj == "55555555555555" || 
        cnpj == "66666666666666" || 
        cnpj == "77777777777777" || 
        cnpj == "88888888888888" || 
        cnpj == "99999999999999")
        return regeita_cnpj()
         
    // Valida DVs
    tamanho = cnpj.length - 2
    numeros = cnpj.substring(0,tamanho);
    digitos = cnpj.substring(tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
      soma += numeros.charAt(tamanho - i) * pos--;
      if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(0))
        return regeita_cnpj()
         
    tamanho = tamanho + 1;
    numeros = cnpj.substring(0,tamanho);
    soma = 0;
    pos = tamanho - 7;
    for (i = tamanho; i >= 1; i--) {
      soma += numeros.charAt(tamanho - i) * pos--;
      if (pos < 2)
            pos = 9;
    }
    resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
    if (resultado != digitos.charAt(1))
          return regeita_cnpj()
           

    return aceita_cnpj()
    
}

function aceita_cnpj() {
    document.getElementById("cnpj_label").innerHTML = 'CNPJ - <i class="fas fa-check"></i>';
    document.getElementById("cnpj_cliente").className = 'form-control is-valid';
}
function regeita_cnpj() {
    document.getElementById("cnpj_label").innerHTML = 'CNPJ - <i class="fas fa-exclamation-triangle"></i>';
    document.getElementById("cnpj_cliente").className = 'form-control is-invalid';
}
function aceita_cpf(elemento) {
    document.getElementById("cpf_label").innerHTML = 'CPF - <i class="fas fa-check"></i>';
    document.getElementById("cpf_cliente").className = 'form-control is-valid';
}
function regeita_cpf(elemento) {
    document.getElementById("cpf_label").innerHTML = 'CPF - <i class="fas fa-exclamation-triangle"></i>';
    document.getElementById("cpf_cliente").className = 'form-control is-invalid';
}

