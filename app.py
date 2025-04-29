from datetime import datetime, timedelta
import streamlit as st
from faker import Faker
import pandas as pd
import random

# Inicializa o Faker
fake = Faker('pt_BR')

# Configurações da página
st.set_page_config(
    page_title="Data Fake - Daniel Castro",
    page_icon="📊",
    layout="centered",
)

# Função para gerar dados falsos baseados na categoria selecionada
def gerar_dados_falsos(categoria, num_linhas, num_colunas):
    dados = []
    
    for _ in range(num_linhas):
        linha = {}
        
        # ID sempre será um CPF falso
        linha['CPF'] = fake.cpf()
        
        # Gera dados específicos para cada categoria
        if categoria == 'Automotivo':
            linha['Marca do Veículo'] = fake.company()
            linha['Modelo do Veículo'] = fake.word()
            linha['Ano de Fabricação'] = random.randint(1990, 2023)
            idade_veiculo = 2023 - linha['Ano de Fabricação']
            linha['Quilometragem'] = random.randint(0, 200000) + (idade_veiculo * 10000)
            linha['Tipo de Combustível'] = fake.random_element(elements=('Gasolina', 'Diesel', 'Elétrico'))
            if linha['Tipo de Combustível'] == 'Elétrico':
                linha['Valor do Veículo'] = random.randint(100000, 300000)
            else:
                linha['Valor do Veículo'] = random.randint(20000, 150000)
            linha['Tem Multas?'] = fake.random_element(elements=('Sim', 'Não'))
            if linha['Tem Multas?'] == 'Sim':
                linha['Tem Seguro?'] = 'Sim'
            else:
                linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Cor do Veículo'] = fake.color_name()
            linha['Tipo de Câmbio'] = fake.random_element(elements=('Manual', 'Automático'))
            linha['Número de Portas'] = random.randint(2, 4)
            linha['Tem Airbag?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem ABS?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data da Última Revisão'] = fake.date_between(start_date=f'-{idade_veiculo}y', end_date='today').strftime('%d/%m/%Y')
            
        elif categoria == 'Geográfica':
            linha['Latitude'] = fake.latitude()
            linha['Longitude'] = fake.longitude()
            linha['Cidade'] = fake.city()
            linha['Estado'] = fake.estado_sigla()
            linha['País'] = 'Brasil'
            linha['Altitude (m)'] = random.randint(0, 3000)
            if linha['Altitude (m)'] > 2000:
                linha['Temperatura Média (°C)'] = round(random.uniform(10.0, 20.0), 1)
            else:
                linha['Temperatura Média (°C)'] = round(random.uniform(20.0, 35.0), 1)
            linha['Precipitação (mm)'] = round(random.uniform(0.0, 300.0), 1)
            if linha['Precipitação (mm)'] > 150:
                linha['Umidade Relativa (%)'] = random.randint(70, 90)
            else:
                linha['Umidade Relativa (%)'] = random.randint(30, 70)
            linha['Velocidade do Vento (km/h)'] = round(random.uniform(0.0, 50.0), 1)
            linha['Tipo de Clima'] = fake.random_element(elements=('Tropical', 'Temperado', 'Árido'))
            linha['Risco de Desastres'] = fake.random_element(elements=('Baixo', 'Médio', 'Alto'))
            linha['Data da Coleta'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            linha['Fonte dos Dados'] = fake.random_element(elements=('Satélite', 'Estação Meteorológica'))

        elif categoria == 'Empresarial':
            linha['Nome da Empresa'] = fake.company()
            linha['CNPJ'] = fake.cnpj()
            linha['Setor'] = fake.random_element(elements=('Tecnologia', 'Varejo', 'Saúde', 'Educação'))
            if linha['Setor'] == 'Tecnologia':
                linha['Nível de Risco'] = 'Baixo'
            elif linha['Setor'] == 'Varejo':
                linha['Nível de Risco'] = 'Médio'
            else:
                linha['Nível de Risco'] = 'Alto'
            linha['Número de Funcionários'] = random.randint(10, 1000)
            linha['Faturamento Anual (R$)'] = linha['Número de Funcionários'] * random.randint(10000, 50000)
            linha['Custo com Pessoal (R$)'] = linha['Número de Funcionários'] * random.randint(5000, 20000)
            linha['Lucro Líquido (R$)'] = linha['Faturamento Anual (R$)'] - linha['Custo com Pessoal (R$)']
            linha['Dívida Total (R$)'] = random.randint(50000, 5000000)
            linha['Data de Fundação'] = fake.date_between(start_date='-30y', end_date='today').strftime('%d/%m/%Y')
            linha['Tem Filial no Exterior?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Certificação ISO?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Nível de Satisfação dos Funcionários (%)'] = random.randint(50, 100)
            linha['Fonte dos Dados'] = fake.random_element(elements=('Relatório Anual', 'Sistema ERP'))

        elif categoria == 'Mobilidade Elétrica':
            linha['Modelo do Veículo'] = fake.random_element(elements=('Tesla Model 3', 'Nissan Leaf', 'Chevrolet Bolt'))
            linha['Tipo de Bateria'] = fake.random_element(elements=('Íon-Lítio', 'Níquel-Metal'))
            if linha['Tipo de Bateria'] == 'Íon-Lítio':
                linha['Capacidade da Bateria (kWh)'] = round(random.uniform(50.0, 100.0), 1)
            else:
                linha['Capacidade da Bateria (kWh)'] = round(random.uniform(30.0, 60.0), 1)
            linha['Autonomia (km)'] = int(linha['Capacidade da Bateria (kWh)'] * random.uniform(5.0, 8.0))
            linha['Custo do Veículo (R$)'] = int(linha['Autonomia (km)'] * random.uniform(500.0, 1000.0))
            linha['Tempo de Recarga (horas)'] = round(random.uniform(1.0, 12.0), 1)
            linha['Potência do Motor (kW)'] = random.randint(100, 500)
            linha['Nível de Emissões (g/km)'] = 0.0
            linha['Tem Recarga Rápida?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Número de Estações de Recarga'] = random.randint(100, 10000)
            linha['Custo Médio de Recarga (R$)'] = round(random.uniform(20.0, 100.0), 1)
            linha['Data de Fabricação'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Tem Garantia Estendida?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Fonte dos Dados'] = fake.random_element(elements=('Fabricante', 'Concessionária'))

        elif categoria == 'Imobiliário':
            linha['Endereço do Imóvel'] = fake.address()
            linha['Tipo de Imóvel'] = fake.random_element(elements=('Casa', 'Apartamento', 'Terreno'))
            linha['Área do Imóvel (m²)'] = random.randint(50, 500)
            linha['Valor do Imóvel'] = linha['Área do Imóvel (m²)'] * random.randint(2000, 5000)
            linha['Número de Quartos'] = random.randint(1, 5)
            linha['Número de Banheiros'] = linha['Número de Quartos'] + random.randint(0, 2)
            linha['Tem Piscina?'] = fake.random_element(elements=('Sim', 'Não'))
            if linha['Tem Piscina?'] == 'Sim':
                linha['Tem Garagem?'] = 'Sim'
            else:
                linha['Tem Garagem?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Elevador?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Condomínio Fechado?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor do Condomínio'] = random.randint(200, 2000)
            linha['Ano de Construção'] = random.randint(1980, 2023)
            linha['Tipo de Oferta'] = fake.random_element(elements=('Venda', 'Aluguel'))
            linha['Data da Última Reforma'] = fake.date_between(start_date='-10y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (cartão de crédito)':
            linha['Número do Cartão'] = fake.credit_card_number()
            linha['Validade do Cartão'] = fake.credit_card_expire()
            linha['Bandeira do Cartão'] = fake.credit_card_provider()
            if linha['Bandeira do Cartão'] in ['Visa', 'Mastercard']:
                linha['Tem Anuidade?'] = fake.random_element(elements=('Sim', 'Não'))
            else:
                linha['Tem Anuidade?'] = 'Sim'
            if linha['Bandeira do Cartão'] == 'Mastercard':
                linha['Tem Cashback?'] = 'Sim'
            else:
                linha['Tem Cashback?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Limite do Cartão'] = random.randint(1000, 20000)
            linha['Valor da Última Fatura'] = random.randint(500, linha['Limite do Cartão'])
            linha['Dia de Vencimento da Fatura'] = random.randint(1, 31)
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Programa de Pontos?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Número de Parcelas em Aberto'] = random.randint(0, 12)
            linha['Valor Total de Parcelas'] = random.randint(1000, 10000)
            linha['Tem Limite Internacional?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data de Emissão do Cartão'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (seguros)':
            linha['Tipo de Seguro'] = fake.random_element(elements=('Automóvel', 'Vida', 'Residencial'))
            linha['Seguradora'] = fake.company()
            if linha['Tipo de Seguro'] == 'Vida':
                linha['Valor da Cobertura'] = random.randint(500000, 1000000)
            else:
                linha['Valor da Cobertura'] = random.randint(50000, 500000)
            linha['Número de Sinistros'] = random.randint(0, 5)
            linha['Valor do Prêmio Mensal'] = random.randint(100, 1000) + (linha['Número de Sinistros'] * 100)
            linha['Tem Franquia?'] = fake.random_element(elements=('Sim', 'Não'))
            if linha['Tem Franquia?'] == 'Sim':
                linha['Valor da Franquia'] = random.randint(500, 5000)
            else:
                linha['Valor da Franquia'] = 0
            linha['Data de Início do Seguro'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término do Seguro'] = fake.date_between(start_date='today', end_date='+5y').strftime('%d/%m/%Y')
            linha['Tem Cobertura Internacional?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Assistência 24h?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tipo de Pagamento'] = fake.random_element(elements=('Mensal', 'Anual'))
            linha['Tem Desconto por Fidelidade?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data do Último Sinistro'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (empréstimos)':
            linha['Valor do Empréstimo'] = random.randint(1000, 100000)
            linha['Tipo de Empréstimo'] = fake.random_element(elements=('Pessoal', 'Consignado'))
            linha['Número de Parcelas'] = random.randint(12, 60)
            linha['Valor da Parcela'] = linha['Valor do Empréstimo'] / linha['Número de Parcelas']
            linha['Nível de Risco'] = fake.random_element(elements=('Baixo', 'Médio', 'Alto'))
            if linha['Nível de Risco'] == 'Alto':
                linha['Taxa de Juros (%)'] = round(random.uniform(5.0, 10.0), 2)
            else:
                linha['Taxa de Juros (%)'] = round(random.uniform(1.0, 5.0), 2)
            if linha['Valor do Empréstimo'] > 50000:
                linha['Tem Seguro?'] = 'Sim'
            else:
                linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Instituição Financeira'] = fake.company()
            linha['Data de Contratação'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Vencimento'] = fake.date_between(start_date='today', end_date='+5y').strftime('%d/%m/%Y')
            linha['Tem Taxa de Adiantamento?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Número de Parcelas Pagas'] = random.randint(0, linha['Número de Parcelas'])
            linha['Número de Parcelas em Atraso'] = random.randint(0, 12)
            linha['Tem Restrição no Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Motivo do Empréstimo'] = fake.random_element(elements=('Reforma', 'Viagem', 'Educação'))
        
        elif categoria == 'Serviços financeiros (consórcios)':
            linha['Tipo de Consórcio'] = fake.random_element(elements=('Automóvel', 'Imóvel'))
            if linha['Tipo de Consórcio'] == 'Imóvel':
                linha['Valor do Bem'] = random.randint(500000, 1000000)
            else:
                linha['Valor do Bem'] = random.randint(50000, 500000)
            linha['Número de Cotas'] = random.randint(12, 120)
            linha['Valor da Cota'] = linha['Valor do Bem'] / linha['Número de Cotas']
            if linha['Tipo de Consórcio'] == 'Imóvel':
                linha['Taxa Administrativa (%)'] = round(random.uniform(2.0, 5.0), 2)
            else:
                linha['Taxa Administrativa (%)'] = round(random.uniform(0.5, 2.0), 2)
            linha['Tem Lance Fixo?'] = fake.random_element(elements=('Sim', 'Não'))
            if linha['Tem Lance Fixo?'] == 'Sim':
                linha['Valor do Lance'] = random.randint(10000, 50000)
            else:
                linha['Valor do Lance'] = 0
            linha['Data de Início'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término'] = fake.date_between(start_date='today', end_date='+10y').strftime('%d/%m/%Y')
            linha['Número de Cotas Pagas'] = random.randint(0, linha['Número de Cotas'])
            linha['Número de Cotas em Atraso'] = random.randint(0, 12)
            linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Reajuste Anual?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data da Última Assembléia'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
        
        elif categoria == 'Serviços financeiros (financiamento)':
            linha['Tipo de Financiamento'] = fake.random_element(elements=('Imóvel', 'Veículo'))
            if linha['Tipo de Financiamento'] == 'Imóvel':
                linha['Valor Financiado'] = random.randint(500000, 1000000)
            else:
                linha['Valor Financiado'] = random.randint(50000, 500000)
            linha['Número de Parcelas'] = random.randint(12, 360)
            linha['Valor da Parcela'] = linha['Valor Financiado'] / linha['Número de Parcelas']
            if linha['Tipo de Financiamento'] == 'Imóvel':
                linha['Taxa de Juros (%)'] = round(random.uniform(1.0, 5.0), 2)
            else:
                linha['Taxa de Juros (%)'] = round(random.uniform(5.0, 10.0), 2)
            if linha['Valor Financiado'] > 500000:
                linha['Tem Seguro?'] = 'Sim'
            else:
                linha['Tem Seguro?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Instituição Financeira'] = fake.company()
            linha['Data de Início'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término'] = fake.date_between(start_date='today', end_date='+30y').strftime('%d/%m/%Y')
            linha['Número de Parcelas Pagas'] = random.randint(0, linha['Número de Parcelas'])
            linha['Número de Parcelas em Atraso'] = random.randint(0, 12)
            linha['Tem Reajuste Anual?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Valor da Entrada'] = random.randint(10000, 100000)
            linha['Tem Restrição no Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Motivo do Financiamento'] = fake.random_element(elements=('Casa Própria', 'Carro Novo'))
        
        elif categoria == 'Marketing':
            linha['Canal de Marketing'] = fake.random_element(elements=('Instagram', 'Google Ads', 'Facebook', 'LinkedIn'))
            if linha['Canal de Marketing'] == 'Google Ads':
                linha['Custo por Clique (CPC)'] = round(random.uniform(1.0, 5.0), 2)
            else:
                linha['Custo por Clique (CPC)'] = round(random.uniform(0.5, 2.0), 2)
            linha['Público-Alvo'] = fake.random_element(elements=('18-35 anos', '35-50 anos', '50+ anos'))
            if linha['Público-Alvo'] == '18-35 anos':
                linha['Taxa de Conversão (%)'] = round(random.uniform(5.0, 10.0), 2)
            else:
                linha['Taxa de Conversão (%)'] = round(random.uniform(2.0, 5.0), 2)
            linha['Orçamento Total'] = random.randint(1000, 100000)
            linha['Gasto Atual'] = random.randint(500, linha['Orçamento Total'])
            linha['Número de Cliques'] = random.randint(100, 10000)
            linha['Número de Conversões'] = int(linha['Número de Cliques'] * (linha['Taxa de Conversão (%)'] / 100))
            linha['Custo por Aquisição (CPA)'] = round(linha['Gasto Atual'] / linha['Número de Conversões'], 2) if linha['Número de Conversões'] > 0 else 0
            linha['Tem Campanha Ativa?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tipo de Anúncio'] = fake.random_element(elements=('Vídeo', 'Banner', 'Texto'))
            linha['Tem Retargeting?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data de Início da Campanha'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            linha['Data de Término da Campanha'] = fake.date_between(start_date='today', end_date='+1y').strftime('%d/%m/%Y')
        
        elif categoria == 'Contábil':
            linha['Renda Mensal'] = random.randint(2000, 20000)
            linha['Tipo de Contribuinte'] = fake.random_element(elements=('PF', 'PJ'))
            if linha['Tipo de Contribuinte'] == 'PF':
                linha['Valor do Imposto Pago'] = linha['Renda Mensal'] * random.uniform(0.1, 0.3)
            else:
                linha['Valor do Imposto Pago'] = linha['Renda Mensal'] * random.uniform(0.2, 0.4)
            linha['Número de Dependentes'] = random.randint(0, 5)
            if linha['Número de Dependentes'] > 2:
                linha['Tem Benefícios Fiscais?'] = 'Sim'
            else:
                linha['Tem Benefícios Fiscais?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Investimentos?'] = fake.random_element(elements=('Sim', 'Não'))
            if linha['Tem Investimentos?'] == 'Sim':
                linha['Valor dos Investimentos'] = random.randint(10000, 100000)
            else:
                linha['Valor dos Investimentos'] = 0
            linha['Tem Débitos Pendentes?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Imóvel em Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Veículo em Nome?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tem Declaração Anual?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Data da Última Declaração'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Tem Restrição na Receita?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Tipo de Regime Tributário'] = fake.random_element(elements=('Simples Nacional', 'Lucro Real'))

        elif categoria == 'E-commerce':
            linha['Nome do Cliente'] = fake.name()
            linha['Email do Cliente'] = fake.email()
            linha['Data da Compra'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            linha['Quantidade Comprada'] = random.randint(1, 5)
            linha['Valor da Compra (R$)'] = round(random.uniform(50.0, 1000.0), 2) * linha['Quantidade Comprada']
            linha['Cupom de Desconto'] = fake.random_element(elements=('SIM10', 'Nenhum'))
            if linha['Cupom de Desconto'] == 'SIM10':
                linha['Valor do Desconto (R$)'] = linha['Valor da Compra (R$)'] * 0.1
            else:
                linha['Valor do Desconto (R$)'] = 0.0
            dias_passados = (datetime.now() - datetime.strptime(linha['Data da Compra'], '%d/%m/%Y')).days
            if dias_passados > 30:
                linha['Status do Pedido'] = 'Entregue'
            elif dias_passados > 7:
                linha['Status do Pedido'] = 'Em Trânsito'
            else:
                linha['Status do Pedido'] = 'Processando'
            linha['Categoria do Produto'] = fake.random_element(elements=('Eletrônicos', 'Moda', 'Alimentos', 'Casa e Decoração'))
            if linha['Categoria do Produto'] == 'Eletrônicos':
                linha['Avaliação do Produto (1-5)'] = round(random.uniform(4.0, 5.0), 1)
            else:
                linha['Avaliação do Produto (1-5)'] = round(random.uniform(3.0, 5.0), 1)
            linha['Forma de Pagamento'] = fake.random_element(elements=('Cartão de Crédito', 'Boleto', 'Pix'))
            linha['Nome do Produto'] = fake.random_element(elements=('Smartphone XYZ', 'Camiseta Básica', 'Notebook ABC', 'Mesa de Jantar'))
            linha['Frete (R$)'] = round(random.uniform(0.0, 50.0), 2)
            linha['Método de Entrega'] = fake.random_element(elements=('Correios', 'Transportadora'))
            
        elif categoria == 'SAC-Telemarketing':
            linha['Nome do Operador'] = fake.name()
            linha['Matrícula do Operador'] = f"SAC-{random.randint(1000, 9999)}"
            linha['Tipo de Atendimento'] = fake.random_element(elements=('Reclamação', 'Dúvida', 'Elogio', 'Solicitação'))
            linha['Canal de Atendimento'] = fake.random_element(elements=('Telefone', 'Chat', 'E-mail', 'WhatsApp'))
            linha['Tempo Médio de Atendimento (TMA) em minutos'] = round(random.uniform(3.0, 15.0), 1)
            linha['Satisfação do Cliente (1-5)'] = random.randint(1, 5)
            linha['Protocolo'] = f"PROTO-{fake.date_this_year().strftime('%Y-%m')}-{random.randint(1000, 9999)}"
            linha['Data/Hora do Atendimento'] = fake.date_time_this_year().strftime('%d/%m/%Y %H:%M')
            linha['Tempo de Espera em minutos'] = round(random.uniform(0.5, 10.0), 1)
            linha['Produto/Serviço Relacionado'] = fake.random_element(elements=('Internet', 'TV por Assinatura', 'Telefonia', 'Planos'))
            linha['Resolução no Primeiro Contato?'] = fake.random_element(elements=('Sim', 'Não'))
            linha['Encaminhamento para Outro Setor'] = fake.random_element(elements=('Técnico', 'Financeiro', 'Nenhum', 'Comercial'))
            linha['Tempo de Pós-Atendimento (minutos)'] = round(random.uniform(0.5, 5.0), 1)
            linha['Status do Atendimento'] = fake.random_element(elements=('Finalizado', 'Pendente', 'Reaberto'))

        elif categoria == 'Ativos de Serviços de T.I':
            linha['Tipo de Ativo'] = fake.random_element(elements=('Servidor', 'Notebook', 'Roteador', 'Switch', 'Storage'))
            linha['Marca/Modelo'] = f"{fake.random_element(elements=('Dell', 'HP', 'Cisco'))} {fake.word().capitalize()} {random.randint(100, 999)}"
            linha['Número de Série'] = f"SN-{random.randint(100000000, 999999999)}"
            linha['Data de Aquisição'] = fake.date_between(start_date='-5y', end_date='today').strftime('%d/%m/%Y')
            linha['Valor do Ativo (R$)'] = round(random.uniform(2000.0, 50000.0), 2)
            linha['Departamento Responsável'] = fake.random_element(elements=('Infraestrutura', 'Desenvolvimento', 'Suporte', 'Redes'))
            linha['Status'] = fake.random_element(elements=('Ativo', 'Em Manutenção', 'Desativado', 'Reserva'))
            linha['Última Manutenção'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            linha['Próxima Manutenção Prevista'] = fake.date_between(start_date='today', end_date='+1y').strftime('%d/%m/%Y')
            linha['Tempo de Garantia (meses)'] = random.choice([12, 24, 36, 60])
            linha['Fornecedor'] = fake.random_element(elements=('Dell', 'HP', 'Cisco', 'Lenovo', 'IBM'))
            linha['IP/MAC Address'] = f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
            linha['Software Principal'] = fake.random_element(elements=('Windows Server', 'Linux Ubuntu', 'VMware ESXi', 'Cisco IOS'))
            linha['Criticidade'] = fake.random_element(elements=('Alta', 'Média', 'Baixa'))

        elif categoria == 'Obras e Projetos':
            linha['Nome da Obra'] = f"{fake.random_element(elements=('Residencial', 'Comercial', 'Hospitalar'))} {fake.word().capitalize()} {fake.word().capitalize()}"
            linha['Tipo de Obra'] = fake.random_element(elements=('Residencial', 'Comercial', 'Público', 'Industrial'))
            linha['Endereço da Obra'] = fake.address()
            linha['Área Total (m²)'] = round(random.uniform(100.0, 5000.0), 2)
            linha['Número de Pavimentos'] = random.randint(1, 30)
            linha['Data de Início'] = fake.date_between(start_date='-1y', end_date='today').strftime('%d/%m/%Y')
            linha['Data Prevista de Término'] = fake.date_between(start_date='today', end_date='+2y').strftime('%d/%m/%Y')
            linha['Valor Total Contratado (R$)'] = round(random.uniform(500000.0, 10000000.0), 2)
            linha['Número da Licença'] = f"LIC-{fake.date_this_year().strftime('%Y-%m')}-{random.randint(1000, 9999)}"
            linha['Status da Licença'] = fake.random_element(elements=('Vigente', 'Vencida', 'Em Análise', 'Suspensa'))
            linha['Número de Alvarás'] = random.randint(1, 5)
            linha['Responsável Técnico'] = f"Eng. {fake.name()}"
            linha['Percentual Concluído (%)'] = round(random.uniform(0.0, 100.0), 1)
            linha['Risco da Obra'] = fake.random_element(elements=('Baixo', 'Médio', 'Alto'))

        elif categoria == 'Recursos Humanos':
            linha['Nome do Funcionário'] = fake.name()
            linha['Matrícula'] = f"RH-{random.randint(1000, 9999)}"
            linha['Cargo'] = fake.random_element(elements=('Analista de TI', 'Gerente Comercial', 'Assistente Administrativo', 'Desenvolvedor'))
            linha['Data de Admissão'] = fake.date_between(start_date='-10y', end_date='today').strftime('%d/%m/%Y')
            linha['Salário (R$)'] = round(random.uniform(2000.0, 15000.0), 2)
            linha['Departamento'] = fake.random_element(elements=('TI', 'Vendas', 'Financeiro', 'Marketing', 'RH'))
            linha['Nível Hierárquico'] = fake.random_element(elements=('Júnior', 'Pleno', 'Sênior', 'Especialista'))
            linha['Tipo de Contrato'] = fake.random_element(elements=('CLT', 'PJ', 'Estágio', 'Temporário'))
            linha['Última Promoção'] = fake.date_between(start_date='-3y', end_date='today').strftime('%d/%m/%Y')
            linha['Próxima Avaliação'] = fake.date_between(start_date='today', end_date='+1y').strftime('%d/%m/%Y')
            linha['Benefícios'] = fake.random_element(elements=('VT+VR+Plano de Saúde', 'VR+Plano de Saúde', 'VT+VR', 'Plano de Saúde'))
            linha['Turno'] = fake.random_element(elements=('Manhã', 'Tarde', 'Noite', 'Flexível'))
            linha['Status'] = fake.random_element(elements=('Ativo', 'Afastado', 'Desligado', 'Férias'))
            linha['Tempo de Empresa (anos)'] = round((datetime.now() - datetime.strptime(linha['Data de Admissão'], '%d/%m/%Y')).days / 365, 1)

        # Limita o número de colunas
        if len(linha) > num_colunas:
            linha = dict(list(linha.items())[:num_colunas])
        
        dados.append(linha)
    
    return pd.DataFrame(dados)

# Interface do Streamlit
st.title('📊 Data Fake')
st.markdown("""
    **Criado por Daniel Castro**  
    [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/daniel-casthro/)
""")

st.markdown("---")


#st.image("https://via.placeholder.com/1200x400.png?text=Banner+do+Gerador+de+Dados+Falsos", use_container_width=True)


# Descrição
st.markdown("""
    Bem-vindo ao **Gerador de Dados Falsos**!  
    Aqui você pode criar dados fictícios para diversos segmentos, como automotivo, imobiliário, serviços financeiros e muito mais.  
    Selecione a categoria, o número de linhas e colunas, e clique em **Gerar Dados**.
""")

# Seleção da categoria
categoria = st.selectbox(
    '**Selecione a categoria**',
    ['Automotivo', 'Geográfica', 'Empresarial', 'Mobilidade Elétrica',
     'Imobiliário', 'Serviços financeiros (cartão de crédito)', 
     'Serviços financeiros (seguros)', 'Serviços financeiros (empréstimos)', 
     'Serviços financeiros (consórcios)', 'Serviços financeiros (financiamento)', 
     'Marketing', 'Contábil','E-commerce','SAC-Telemarketing','Ativos de Serviços de T.I',
     'Obras e Projetos','Recursos Humanos'
     ]
)

# Seleção do número de linhas e colunas
col1, col2 = st.columns(2)
with col1:
    num_linhas = st.slider('**Número de linhas**', 1, 100000, 10)
with col2:
    num_colunas = st.slider('**Número de colunas**', 1, 15, 5)

# Botão para gerar os dados
if st.button('**Gerar Dados**', type="primary"):
    st.markdown("---")
    st.subheader("Dados Gerados")
    dados = gerar_dados_falsos(categoria, num_linhas, num_colunas)
    st.dataframe(dados, use_container_width=True)
    
    # Opção para baixar os dados como CSV
    st.download_button(
        label="📥 Baixar dados como CSV",
        data=dados.to_csv(index=False).encode('utf-8'),
        file_name=f'dados_falsos_{categoria}.csv',
        mime='text/csv',
    )

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido com  por **Daniel Castro** | [LinkedIn](https://www.linkedin.com/in/daniel-casthro/)")

# Conexão com Google
# Substitua com seu próprio ID de medição GA4
GA_ID = "G-JBK37XNY60"

ga_js = f"""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
"""

# Insere o código no app Streamlit (invisível ao usuário)
st.components.v1.html(ga_js, height=0)

# Banner
st.markdown("---")
st.image("banner2.png", use_container_width=True)