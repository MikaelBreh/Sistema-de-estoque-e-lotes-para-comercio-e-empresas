# arquivo contente nome dos fornecedores, produtos
# e outras informacoes que podem mudar

categorias = ['Caixa', 'Frasco', 'Rótulo', 'Tampa', 'Todos']

valores = ['Caixa 01', 'Caixa 02', 'Caixa 03', 'Caixa 04', 'Caixa 05',
           'Caixa 07', 'Caixa 08', 'Caixa 09', 'Caixa 10', 'Caixa 11',
           'Caixa 12', 'Caixa 22', 'Caixa 42', 'Caixa 43', 'Caixa 910',
           'Caixa 910 Reforçada', 'Caixa Muffato', 'Frasco 100ml Automotivo',
           'Frasco 100ml Colônias', 'Frasco 100ml Logo',
           'Frasco 60ml Spray Cilíndrico', 'Frasco 60ml Spray Quadrado',
           'Frasco Bisnauto 200ml', 'Frasco Bisnauto 400ml',
           'Frasco Botijão 100ml', 'Frasco Casa Clean 500ml Branco',
           'Frasco Casa Clean 500ml Cristal', 'Frasco Casa Clean 910ml Branco',
           'Frasco Casa Clean 910ml Cristal',
           'Frasco Casa Clean 910ml Vermelho', 'Frasco Coala 210',
           'Frasco Coala 260',
           'Frasco Detergente',
           'Frasco Lata Automotiva',
           'Frasco Orma 1L Branco', 'Frasco Orma 1L Cristal',
           'Frasco Pote Cilíndrico 1Kg', 'Frasco Pote Cilíndrico 250g',
           'Frasco Pote Fit 60g Branco', 'Frasco Pote Fit 60g Transparente',
           'Frasco Pote MM 60g', 'Frasco Saboneteira',
           'Frasco Shampoo Pet', 'Frasco Superauto 500ml Cristal',
           'Frasco Superauto 500ml Laranja', 'Frasco Superauto 500ml Preto',
           'Frasco Superauto 500ml Verde', 'Frasco Virgem 1L',
           'Rótulo Aditivo', 'Rótulo Antiembaçante Spray',
           'Rótulo Aromatizante Gel Carro Novo',
           'Rótulo Aromatizante Gel Carro Novo Recorte',
           'Rótulo Aromatizante Gel Citrus',
           'Rótulo Aromatizante Gel Citrus Recorte',
           'Rótulo Aromatizante Gel Lavanda',
           'Rótulo Aromatizante Gel Lavanda Recorte',
           'Rótulo Aromatizante Gel Morango',
           'Rótulo Aromatizante Gel Morango Recorte',
           'Rótulo Aromatizante Gel Talco',
           'Rótulo Aromatizante Gel Talco Recorte',
           'Rótulo Aromatizante Gel Tutti Frutti',
           'Rótulo Aromatizante Gel Tutti Frutti Recorte',
           'Rótulo Aromatizante Spray Carro Novo',
           'Rótulo Aromatizante Spray Morango',
           'Rotulo Aromatizante Spray Talco',
           'Rótulo Brilha Pneu Gel', 'Rótulo Brilha Pneu Líquido 1L',
           'Rótulo Brilha Pneu Líquido 500ml', 'Rótulo Cera Color',
           'Rótulo Desengraxante Bike',
           'Rótulo Detergente',
           'Rótulo Eliminador de Odores Tradicional',
           'Rótulo Eliminador de Odores Floral',
           'Rótulo Eliminador de Odores Lavanda',
           'Rótulo Esponja Automotiva', 'Rótulo Estopa',
           'Rótulo Jet Cera', 'Rótulo Jet Cera Bike',
           'Rótulo Lava Autos com Cera 1L',
           'Rótulo Lava Autos com Cera 500ml',
           'Rótulo Lava Autos Concentrado 1L',
           'Rótulo Lava Autos Concentrado 500ml',
           'Rótulo Lava Bike', 'Rótulo Lava Bike Concentrado',
           'Rótulo Limpa Estofados', 'Rótulo Limpa Parabrisas',
           'Rótulo Limpa Vidros Automotivo',
           'Rótulo Limpa Vidros Casa Clean 500ml',
           'Rótulo Limpa Vidros Casa Clean 910ml', 'Rótulo (Refil) Limpa Vidros Casa Clean 910ml',
           'Rótulo Limpador Banheiro Cemdi Clean 500ml',
           'Rótulo Limpador Banheiro Total 500ml',
           'Rótulo Limpador Banheiro Total SLEEV', 'Rótulo (Refil) Limpador Banheiro Total SLEEV',
           'Rótulo Limpador com Álcool Bambu 910ml', 'Rótulo (Refil) Limpador com Álcool Bambu 910ml',
           'Rótulo Limpador com Álcool Floral 500ml',
           'Rótulo Limpador com Álcool Floral 910ml', 'Rótulo (Refil) Limpador com Álcool Floral 910ml',
           'Rótulo Limpador com Álcool Fresh 500ml',
           'Rótulo Limpador com Álcool Fresh 910ml', 'Rótulo (Refil) Limpador com Álcool Fresh 910ml',
           'Rótulo Limpador com Álcool Lavanda 500ml',
           'Rótulo Limpador com Álcool Lavanda 910ml', 'Rótulo (Refil) Limpador com Álcool Lavanda 910ml',
           'Rótulo Limpador Cozinha Cemdi Clean 500ml',
           'Rótulo Limpador Cozinha Limpeza Pesada SLEEV', 'Rótulo (Refil) Limpador Cozinha Limpeza Pesada SLEEV',
           'Rótulo Limpador Cozinha Total 500ml',
           'Rótulo Limpador Cozinha Total SLEEV', 'Rótulo (Refil) Limpador Cozinha Total SLEEV',
           'Rótulo Limpador Multiuso 910ml', 'Rótulo (Refil) Limpador Multiuso 910ml',
           'Rótulo Renovador de Parachoques',
           'Rótulo Silicone Gel 100g', 'Rótulo Silicone Gel 1Kg', 'Rótulo Silicone Gel 250g',
           'Rótulo Silicone Líquido 100ml', 'Rótulo Silicone Líquido 200ml',
           'Tampa Aditivo',
           'Tampa Aromatizante Gel Fit Amarela', 'Tampa Aromatizante Gel Fit Azul',
           'Tampa Aromatizante Gel Fit Preta', 'Tampa Aromatizante Gel Fit Rosa',
           'Tampa Aromatizante Gel Fit Roxa', 'Tampa Aromatizante Gel Fit Transaparente',
           'Tampa Aromatizante Gel Fit Verde', 'Tampa Aromatizante Gel Fit Vermelha',
           'Tampa Aromatizante Gel MM Amarela', 'Tampa Aromatizante Gel MM Azul',
           'Tampa Aromatizante Gel MM Preta', 'Tampa Aromatizante Gel MM Rosa',
           'Tampa Aromatizante Gel MM Roxa', 'Tampa Aromatizante Gel MM Transparente',
           'Tampa Aromatizante Gel MM Verde', 'Tampa Aromatizante Gel MM Vermelha',
           'Tampa Batoque Aromatizante Gel MM', 'Tampa Cilíndrica 1Kg Vermnelha',
           'Tampa Cilíndrica 250g Azul', 'Tampa Cilíndrica 250g Preta',
           'Tampa Cilíndrica 250g Vermelha', 'Tampa Encaixe Lata Automotiva',
           'Tampa Flip Top Bater Preta Aberta', 'Tampa Flip Top Bater Preta Fechada',
           'Tampa Flip Top Rosca Branca', 'Tampa Flip Top Rosca Preta',
           'Tampa Lacre Branca', 'Tampa Limpa Parabrisas', 'Tampa Lubrifiador Bike ',
           'Tampa Rosca Azul', 'Tampa Rosca Branca', 'Tampa Rosca Preta', 'Tampa Rosca Verde',
           'Tampa Rosca Vermelha', 'Válvula Mini Trigger Lisa Preta', 'Válvula Pump',
           'Válvula Spray Branca', 'Válvula Spray Preta ', 'Válvula Trigger Estriada Branca']

estoque_minimo = {
    'Caixa 01': 0, 'Caixa 02': 0, 'Caixa 03': 0, 'Caixa 04': 0, 'Caixa 05': 0,
    'Caixa 07': 0, 'Caixa 08': 0, 'Caixa 09': 0, 'Caixa 10': 0, 'Caixa 11': 0,
    'Caixa 12': 0, 'Caixa 22': 0, 'Caixa 42': 0, 'Caixa 43': 0, 'Caixa 910': 0,
    'Caixa 910 Reforçada': 0, 'Caixa Muffato': 0, 'Frasco 100ml Automotivo': 0,
    'Frasco 100ml Colônias': 0, 'Frasco 100ml Logo': 0, 'Frasco 60ml Spray Cilíndrico': 0,
    'Frasco 60ml Spray Quadrado': 0, 'Frasco Bisnauto 200ml': 0, 'Frasco Bisnauto 400ml': 0,
    'Frasco Botijão 100ml': 0, 'Frasco Casa Clean 500ml Branco': 0,
    'Frasco Casa Clean 500ml Cristal': 0, 'Frasco Casa Clean 910ml Branco': 0,
    'Frasco Casa Clean 910ml Cristal': 0, 'Frasco Casa Clean 910ml Vermelho': 0,
    'Frasco Coala 210': 0, 'Frasco Coala 260': 0, 'Frasco Detergente': 0,
    'Frasco Lata Automotiva': 0, 'Frasco Orma 1L Branco': 0, 'Frasco Orma 1L Cristal': 0,
    'Frasco Pote Cilíndrico 1Kg': 0, 'Frasco Pote Cilíndrico 250g': 0,
    'Frasco Pote Fit 60g Branco': 0, 'Frasco Pote Fit 60g Transparente': 0,
    'Frasco Pote MM 60g': 0, 'Frasco Saboneteira': 0, 'Frasco Shampoo Pet': 0,
    'Frasco Superauto 500ml Cristal': 0, 'Frasco Superauto 500ml Laranja': 0,
    'Frasco Superauto 500ml Preto': 0, 'Frasco Superauto 500ml Verde': 0,
    'Frasco Virgem 1L': 0, 'Rótulo Aditivo': 0, 'Rótulo Antiembaçante Spray': 0,
    'Rótulo Aromatizante Gel Carro Novo': 4000, 'Rótulo Aromatizante Gel Carro Novo Recorte': 0,
    'Rótulo Aromatizante Gel Citrus': 4000, 'Rótulo Aromatizante Gel Citrus Recorte': 0,
    'Rótulo Aromatizante Gel Lavanda': 4000, 'Rótulo Aromatizante Gel Lavanda Recorte': 0,
    'Rótulo Aromatizante Gel Morango': 4000, 'Rótulo Aromatizante Gel Morango Recorte': 0,
    'Rótulo Aromatizante Gel Talco': 4000, 'Rótulo Aromatizante Gel Talco Recorte': 0,
    'Rótulo Aromatizante Gel Tutti Frutti': 4000, 'Rótulo Aromatizante Gel Tutti Frutti Recorte': 0,
    'Rótulo Aromatizante Spray Carro Novo': 2800, 'Rótulo Aromatizante Spray Morango': 1000,
    'Rotulo Aromatizante Spray Talco': 2000, 'Rótulo Brilha Pneu Gel': 2000,
    'Rótulo Brilha Pneu Líquido 1L': 2000, 'Rótulo Brilha Pneu Líquido 500ml': 14000,
    'Rótulo Cera Color': 2000, 'Rótulo Desengraxante Bike': 300, 'Rótulo Detergente': 0,
    'Rótulo Eliminador de Odores Tradicional': 0, 'Rótulo Eliminador de Odores Floral': 0,
    'Rótulo Eliminador de Odores Lavanda': 0, 'Rótulo Esponja Automotiva': 7000,
    'Rótulo Estopa': 2000, 'Rótulo Jet Cera': 2500, 'Rótulo Jet Cera Bike': 0,
    'Rótulo Lava Autos com Cera 1L': 2200, 'Rótulo Lava Autos com Cera 500ml': 5200,
    'Rótulo Lava Autos Concentrado 1L': 1300, 'Rótulo Lava Autos Concentrado 500ml': 10000,
    'Rótulo Lava Bike': 0, 'Rótulo Lava Bike Concentrado': 0, 'Rótulo Limpa Estofados': 2000,
    'Rótulo Limpa Parabrisas': 2000, 'Rótulo Limpa Vidros Automotivo': 2000,
    'Rótulo Limpa Vidros Casa Clean 500ml': 0, 'Rótulo Limpa Vidros Casa Clean 910ml': 5000,
    'Rótulo (Refil) Limpa Vidros Casa Clean 910ml': 0,
    'Rótulo Limpador Banheiro Cemdi Clean 500ml': 0,
    'Rótulo Limpador Banheiro Total 500ml': 0, 'Rótulo Limpador Banheiro Total SLEEV': 7000,
    'Rótulo (Refil) Limpador Banheiro Total SLEEV': 0,
    'Rótulo Limpador com Álcool Bambu 910ml': 2200,
    'Rótulo (Refil) Limpador com Álcool Bambu 910ml': 0,
    'Rótulo Limpador com Álcool Floral 500ml': 0,
    'Rótulo Limpador com Álcool Floral 910ml': 3700,
    'Rótulo (Refil) Limpador com Álcool Floral 910ml': 0,
    'Rótulo Limpador com Álcool Fresh 500ml': 0,
    'Rótulo Limpador com Álcool Fresh 910ml': 1000,
    'Rótulo (Refil) Limpador com Álcool Fresh 910ml': 0,
    'Rótulo Limpador com Álcool Lavanda 500ml': 0,
    'Rótulo Limpador com Álcool Lavanda 910ml': 4400,
    'Rótulo (Refil) Limpador com Álcool Lavanda 910ml': 0,
    'Rótulo Limpador Cozinha Cemdi Clean 500ml': 0,
    'Rótulo Limpador Cozinha Limpeza Pesada SLEEV': 4500,
    'Rótulo (Refil) Limpador Cozinha Limpeza Pesada SLEEV': 0,
    'Rótulo Limpador Cozinha Total 500ml': 0, 'Rótulo Limpador Cozinha Total SLEEV': 5000,
    'Rótulo (Refil) Limpador Cozinha Total SLEEV': 0, 'Rótulo Limpador Multiuso 910ml': 4000,
    'Rótulo (Refil) Limpador Multiuso 910ml': 0, 'Rótulo Renovador de Parachoques': 1200,
    'Rotulo Shampoo Branqueador PET': 0, 'Rótulo Silicone Gel 100g': 6000,
    'Rótulo Silicone Gel 1Kg': 0, 'Rótulo Silicone Gel 250g': 8000,
    'Rótulo Silicone Líquido 100ml': 5000, 'Rótulo Silicone Líquido 200ml': 1000,
    'Tampa Aditivo': 0, 'Tampa Aromatizante Gel Fit Amarela': 0,
    'Tampa Aromatizante Gel Fit Azul': 0, 'Tampa Aromatizante Gel Fit Preta': 0,
    'Tampa Aromatizante Gel Fit Rosa': 0, 'Tampa Aromatizante Gel Fit Roxa': 0,
    'Tampa Aromatizante Gel Fit Transaparente': 0, 'Tampa Aromatizante Gel Fit Verde': 0,
    'Tampa Aromatizante Gel Fit Vermelha': 0, 'Tampa Aromatizante Gel MM Amarela': 0,
    'Tampa Aromatizante Gel MM Azul': 0, 'Tampa Aromatizante Gel MM Preta': 0,
    'Tampa Aromatizante Gel MM Rosa': 0, 'Tampa Aromatizante Gel MM Roxa': 0,
    'Tampa Aromatizante Gel MM Transparente': 0, 'Tampa Aromatizante Gel MM Verde': 0,
    'Tampa Aromatizante Gel MM Vermelha': 0, 'Tampa Batoque Aromatizante Gel MM': 0,
    'Tampa Cilíndrica 1Kg Vermnelha': 0,
   'Tampa Cilíndrica 250g Azul': 0, 'Tampa Cilíndrica 250g Preta': 0,
   'Tampa Cilíndrica 250g Vermelha': 0, 'Tampa Encaixe Lata Automotiva': 0,
   'Tampa Flip Top Bater Preta Aberta': 0, 'Tampa Flip Top Bater Preta Fechada': 0,
   'Tampa Flip Top Rosca Branca': 0, 'Tampa Flip Top Rosca Preta': 0,
   'Tampa Lacre Branca': 0, 'Tampa Limpa Parabrisas': 0, 'Tampa Lubrifiador Bike ': 0,
   'Tampa Rosca Azul': 0, 'Tampa Rosca Branca': 0, 'Tampa Rosca Preta': 0, 'Tampa Rosca Verde': 0,
   'Tampa Rosca Vermelha': 0, 'Válvula Mini Trigger Lisa Preta': 0, 'Válvula Pump': 0,
   'Válvula Spray Branca': 0, 'Válvula Spray Preta ': 0, 'Válvula Trigger Estriada Branca': 0
}


forncedores = ['Talula - AlphaPack', 'Aultamp', 'EMDC', 'Fraemb', 'Ganesh', 'Grup SH', 'MacPet',
'Mamute', 'Master pumps', 'Masterkraft', 'Masterprint', 'Monte Sião', 'MR grafica',
'Oliver Print', 'Ondulapack', 'PDG', 'PRADA', 'Rotular Print', 'SIEM', 'PlasNox', 'UEFA',
'Frasco Sul']


produtos_acabados = ['Lava Autos Concentrado Mil Milhas 500ml',
'Lava Autos com Cera Mil Milhas 500ml',
'Brilha Pneu Liquido Mil Milhas 475ml',
'Brilha Pneu Gel Mil Milhas 500gr',
'Aromatizante Gel Carro Novo Mil Milhas 65gr',
'Aromatizante Gel Morango Mil Milhas 65gr',
'Aromatizante Gel Talco Mil Milhas 65gr',
'Aromatizante Gel Tutti-Frutti Mil Milhas 65gr',
'Aromatizante Gel Lavanda Mil Milhas 65gr',
'Aromatizante Gel Citrus Mil Milhas 65gr',
'Aromatizante Spray Morango',
'Aromatizante Spray Carro Novo',
'Aromatizante Spray Talco',
'Antiembaçante Spray',
'CERA LATA 200 GRS',
'Cera Color Mil Milhas BRANCA',
'Cera Color Mil Milhas VERMELHA',
'Cera Color Mil Milhas PRETA',
'Cera Color Mil Milhas PRATA',
'Cera Color Mil Milhas CINZA',
'Silicone Líquido Mil Milhas 100ml',
'Silicone Líquido Mil Milhas 200ml',
'Silicone Gel 100g Mil Milhas',
'Silicone Gel Carro Novo Mil Milhas 250gr',
'Jet Cera com Gatilho Mil Milhas 500ml',
'JET CERA 500 ML TAMPA',
'Limpa Vidros Gatilho Mil Milhas 500 ML',
'LIMPA VIDROS 500 ML AUTOMOTIVO TAMPA',
'Limpa Estofados com Gatilho Mil Milhas 500ml',
'LIMPA ESTOFADOS 500 ML TAMPA',
'LIMPA PARABRISA 100 ML',
'Renovador de Parachoques Preto Mil Milhas 200ml',
'Aditivo Radiador Mil Milhas ROSA',
'Lava Autos Concentrado Mil Milhas 1000ml',
'Lava Autos com Cera Mil Milhas 1000 ml',
'Brilha Pneu Liquido Mil Milhas 1000ml',
'Limpa Vidros 910ML',
'Limpador Com Alcool Bambu 910ML',
'Limpador Com Alcool Fresh 910ML',
'Limpador Com Alcool Lavanda 910ML',
'Limpador Com Alcool Floral 910ML',
'Cozinha Total 910ML',
'Cozinha Limpeza Pesada 910ML',
'Banheiro Total 910ML',
'Multisuo 910ML',
'Detergente CC pump'
'Limpa Vidros 910ML Refil',
'Limpador Com Alcool Bambu 910ML Refil',
'Limpador Com Alcool Fresh 910ML Refil',
'Limpador Com Alcool Lavanda 910ML Refil',
'Limpador Com Alcool Floral 910ML Refil',
'Cozinha Total 910ML Refil',
'Cozinha Limpeza Pesada 910ML Refil',
'Banheiro Total 910ML Refil',
'Multisuo 910ML Refil',
'Detergente CC Refil'
'Lubrificante Com Cera PTFE Para Correntes 90G',
'Desingraxante e Limpador Para Bike 400ML',
'Lava Bikes Pronto Para Uso 40ML',
'Cera Liquida Para Bikes 400ML (jet cera)',
'Lava Bikes Concentrado 400ML']


