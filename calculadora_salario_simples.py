
salario = float(input('Digite o seu salário: '))
dependentes = int(input("Digite o número de dependentes: "))
outras_deducoes = float(input('Informe outras deduções, se houver: '))

parcela_dedutivel_dependentes = 189.59
deducao_dependentes = dependentes * parcela_dedutivel_dependentes

inss_faixa_1 = 0.075
inss_faixa_2 = 0.09
inss_faixa_3 = 0.12
inss_faixa_4 = 0.14

deducao_faixa_1 = 0.00
deducao_faixa_2 = 18.18
deducao_faixa_3 = 91.00
deducao_faixa_4 = 163.82

if salario <= 1212.00:
    inss_mes = salario * inss_faixa_1
elif (salario > 1212.00) and (salario < 2427.36):
    inss_mes = salario * inss_faixa_2 - deducao_faixa_2
elif (salario >= 2427.36) and (salario < 3641.04): 
    inss_mes = salario * inss_faixa_3 - deducao_faixa_3
elif (salario >= 3641.04) and (salario <= 7087.22): 
    inss_mes = salario * inss_faixa_4 - deducao_faixa_4
elif (salario > 7087.22): 
    inss_mes = 828.38


base_de_calculo = salario - inss_mes - deducao_dependentes - outras_deducoes

irpf_faixa_1 = 0.075            
irpf_faixa_2 = 0.15
irpf_faixa_3 = 0.225
irpf_faixa_4 = 0.275

deducao_faixa_1 = 142.80
deducao_faixa_2 = 354.80
deducao_faixa_3 = 636.13
deducao_faixa_4 = 869.36

if base_de_calculo <= 1903.98:
    imposto_de_renda = 0.00
elif (base_de_calculo >= 1903.99) and (base_de_calculo < 2826.66):
    imposto_de_renda = base_de_calculo * irpf_faixa_1 - deducao_faixa_1
elif (base_de_calculo >= 2826.66) and (base_de_calculo < 3751.06): 
    imposto_de_renda = base_de_calculo * irpf_faixa_2 - deducao_faixa_2
elif (base_de_calculo >= 3751.06) and (base_de_calculo < 4664.68): 
    imposto_de_renda = base_de_calculo * irpf_faixa_3 - deducao_faixa_3
elif (base_de_calculo >= 4664.68): 
    imposto_de_renda = base_de_calculo * irpf_faixa_4 - deducao_faixa_4

salario_liquido = salario - inss_mes - imposto_de_renda

print(f'O salário líquido do mês é de {salario_liquido:,.2f}, tendo havido um desconto de R$ {inss_mes:,.2f} relativos ao INSS e R$ {imposto_de_renda:,.2f} relativos ao IRPF.')  
