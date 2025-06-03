# 🌀 Recursividade

## 📘 O que é Recursividade?

Recursividade é uma técnica de programação em que uma função **chama a si mesma** para resolver **subproblemas menores** de um problema maior. É um conceito fundamental em ciência da computação, sendo amplamente utilizado em algoritmos que lidam com estruturas hierárquicas, como árvores, grafos e decomposição de tarefas.

O funcionamento da recursividade envolve duas etapas principais:

- **Empilhamento:** A cada chamada recursiva, uma nova instância da função é adicionada à pilha de execução.
- **Desempilhamento:** Quando a função atinge o **caso base** (condição de parada), as chamadas começam a retornar, propagando os resultados parciais até a solução final.

Utilizar recursão pode simplificar a resolução de problemas complexos, tornando o código mais legível e elegante. No entanto, é essencial garantir que toda recursão tenha um caso base bem definido, evitando loops infinitos e possíveis estouros de pilha (_stack overflow_).

---

## 🧠 Estrutura Geral de uma Função Recursiva

```python
def funcao(parametro):
    if condicao_de_parada:  # Caso base
        return resultado
    else:
        return funcao(parametro_modificado)  # Chamada recursiva
```

**Explicação dos componentes:**

- `condicao_de_parada`: critério que determina quando a recursão deve parar (caso base).
- `resultado`: valor a ser retornado quando o caso base for atingido.
- `parametro_modificado`: parâmetro alterado para que cada chamada aproxime-se do caso base.

---

## 📝 Dicas para usar Recursividade

- Sempre defina claramente o **caso base**.
- Certifique-se de que cada chamada recursiva leva o problema para mais perto do caso base.
- Teste com entradas pequenas para entender o fluxo de chamadas.
- Prefira recursividade quando ela tornar o código mais simples do que a solução iterativa.

---

## 🌳 Exemplos Clássicos de Recursividade

### 1. Fatorial de um número

```python
def fatorial(n):
    if n == 0:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)
```

### 2. Sequência de Fibonacci

```python
def fibonacci(n):
    if n <= 1:  # Casos base
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

### 3. Percorrendo uma árvore

```python
def percorrer_arvore(no):
    if no is None:  # Caso base
        return
    print(no.valor)
    percorrer_arvore(no.esquerda)
    percorrer_arvore(no.direita)
```

---

Recursividade é uma poderosa ferramenta, mas deve ser usada com cuidado e responsabilidade!
