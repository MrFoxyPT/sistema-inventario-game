import json

inventario = []
limite_peso = 50

def adicionar_item():
    nome = input("Nome do item: ")

    tipos_validos = ["arma", "armadura", "consumível"]
    while True:
        tipo = input("Tipo (arma, armadura, consumível): ").lower()
        if tipo in tipos_validos:
            break
        print("❌ Tipo inválido. Escolha entre: arma, armadura, consumível.")

    raridades_validas = ["comum", "incomum", "raro", "épico"]
    while True:
        raridade = input("Raridade (comum, incomum, raro, épico): ").lower()
        if raridade in raridades_validas:
            break
        print("❌ Raridade inválida. Escolha entre: comum, incomum, raro, épico.")

    while True:
        try:
            peso = float(input("Peso: "))
            if peso >= 0:
                break
            print("❌ O peso deve ser um número positivo.")
        except ValueError:
            print("❌ Entrada inválida. Digite um número.")

    if peso_total() + peso > limite_peso:
        print("⚠️ Limite de peso excedido!")
        return

    item = {
        "nome": nome,
        "tipo": tipo,
        "raridade": raridade,
        "peso": peso
    }
    inventario.append(item)
    print("✅ Item adicionado!")


def remover_item():
    nome = input("Nome do item a remover: ")
    for item in inventario:
        if item["nome"].lower() == nome.lower():
            inventario.remove(item)
            print("🗑️ Item removido!")
            return
    print("❌ Item não encontrado.")

def mostrar_inventario():
    if not inventario:
        print("📦 Inventário vazio.")
        return
    print("\n🧾 Inventário:")
    for i, item in enumerate(inventario, start=1):
        print(f"{i}. {item['nome']} ({item['tipo']}, {item['raridade']}) - {item['peso']}kg")
    print(f"⚖️ Peso total: {peso_total()} / {limite_peso} kg\n")

def peso_total():
    return sum(item["peso"] for item in inventario)

def salvar():
    with open("inventario.json", "w") as f:
        json.dump(inventario, f)
    print("💾 Inventário salvo.")

def carregar():
    global inventario
    try:
        with open("inventario.json", "r") as f:
            inventario = json.load(f)
        print("📂 Inventário carregado.")
    except FileNotFoundError:
        print("❌ Nenhum inventário salvo encontrado.")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Mostrar inventário")
        print("4. Salvar inventário")
        print("5. Carregar inventário")
        print("0. Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            adicionar_item()
        elif escolha == "2":
            remover_item()
        elif escolha == "3":
            mostrar_inventario()
        elif escolha == "4":
            salvar()
        elif escolha == "5":
            carregar()
        elif escolha == "0":
            print("👋 Saindo...")
            break
        else:
            print("❓ Opção inválida.")

menu()
