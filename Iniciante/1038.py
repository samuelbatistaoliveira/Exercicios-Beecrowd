tabela_preco = {
    1 : 4.00,
    2 : 4.50,
    3 : 5.00,
    4 : 2.00,
    5 : 1.50
}

codigo,quantidade = map(int, input().split())

preco = tabela_preco[codigo]
total = preco * quantidade
print(f"Total: R$ {total:.2f}")