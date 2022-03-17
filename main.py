from vagas import Cache

Cache.load()

eg = Cache.getEstacionamento(1)
print('============== Edificio Garagem ==============')
print(f'||              Valor: R$ %.2f              ||' % eg.getValor())
print(f'||         Quantidade de Vagas: {eg.getQtd()}         ||')
print('==============================================')

print('')

ext = Cache.getEstacionamento(2)
print('=============== Vagas Externas ===============')
print(f'||              Valor: R$ %.2f              ||' % ext.getValor())
print(f'||         Quantidade de Vagas: {ext.getQtd()}         ||')
print('==============================================')