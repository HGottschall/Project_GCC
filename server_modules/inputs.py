import pandas as pd

df = pd.read_excel('data\Relatório.xlsx')

encerrados_preload = (df['status'] == 'encerrados').sum()
ativo_preload = (df['status'] == 'ativo').sum()
analise_preload = (df['status'] == 'analise').sum()
revisao_preload = (df['status'] == 'revisao').sum()
lgpd_preload = (df['lgpd'] == True).sum()
limresp_preload = (df['limiteResponsabilidade'] == True).sum()

target_inputs = ativo_preload + revisao_preload + analise_preload
total_inputs = ativo_preload + analise_preload

percentage_analise = round((analise_preload / target_inputs) * 100, 0)
percentage_ativo = round((ativo_preload / target_inputs) * 100, 0)

print(percentage_analise)
print(percentage_ativo)


percentage_lgpd = round((lgpd_preload / total_inputs) * 100, 0)
percentage_limresp = round((limresp_preload / total_inputs) * 100, 0)

def get_target_inputs() -> int:
    return target_inputs

def get_total_inputs() -> int:
    return total_inputs
    
def get_total_ativos() -> int:
    return ativo_preload

def get_total_analise() -> int:
    return analise_preload

def get_lgpd_true_inputs() -> int:
    return lgpd_preload

def get_resp_true_inputs() -> int:
    return limresp_preload


# RETORNAR PARA CHART - 1
def get_percentage_input_analise() -> int:
    value = percentage_analise
    return value  
    
def get_percentage_input_ativo() -> int:
    value = percentage_ativo
    return value
     

# RETORNAR PARA CHART - 3
def get_percentage_input_lgpd() -> int:
    value = percentage_lgpd
    return value

# RETORNAR PARA CHART - 4
def get_percentage_input_resp() -> int:
    value = percentage_limresp
    return value

def setChartsValues():
    
    circle_circunference = round(2*3.14*100, 0)
    
    analise = get_percentage_input_analise()
    ativo = get_percentage_input_ativo()
    lgpd = get_percentage_input_lgpd()
    resp = get_percentage_input_resp()
    
    total_ativo_pg = f"{(circle_circunference - (circle_circunference * ativo) / 100)}"
    total_analise_pg = f"{(circle_circunference - (628 * circle_circunference) / 100)}"
    
    total_lgpd_pg = f"{(circle_circunference - (circle_circunference * lgpd) / 100)}"
    total_lgpd_abs = lgpd
    total_limresp_abs = resp

    print(total_lgpd_abs)
    
setChartsValues()