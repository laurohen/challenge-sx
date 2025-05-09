### 1) Explique a diferença entre programação síncrona e assíncrona em Python. Quando você usaria cada uma?

Na programação **síncrona**, é como se tudo acontecesse numa fila indiana: uma tarefa termina, aí a próxima começa. Em Python, isso é o padrão — você chama uma função, ela roda, e o programa fica esperando ela acabar. Já na **assíncrona**, é tipo mandar várias tarefas ao mesmo tempo e deixar elas se virarem. Não é exatamente em paralelo por causa do GIL , mas o programa não fica parado esperando. Pra isso, você usa `async` e `await`.

**Quando usar?**
- **Síncrona**: Pra coisas simples, como scripts que vão direto ao ponto ou cálculos pesados onde a ordem importa. Exemplo: somar um monte de números ou processar um arquivo linha por linha.
- **Assíncrona**: Perfeita pra quando tem espera envolvida, tipo chamar APIs, baixar arquivos ou fazer requisições na web. Exemplo: um programa que pega dados de vários sites ao mesmo tempo com `asyncio` ou `aiohttp`.

### 2) O que são metaclasses em Python e como elas podem ser úteis?

Metaclasses são como "classes das classes". Em Python, tudo é objeto, inclusive as classes, e uma metaclass é o que define como uma classe é criada. A metaclass padrão é `type`, mas você pode criar a sua própria pra customizar o comportamento de uma classe.

**Úteis pra quê?**
- Adicionar métodos ou atributos automaticamente a classes.
- Validar regras na criação de classes (ex.: garantir que toda classe tenha um método específico).
- Frameworks como Django usam metaclasses pra coisas como ORM, onde a metaclass transforma definições de modelos em queries SQL.

Exemplo: você pode criar uma metaclass que adiciona um método `saudacao` a toda classe que a usa, sem precisar escrever o método em cada uma.

### 3) Como funciona o garbage collector do Python e como podemos gerenciar manualmente a memória?

O **garbage collector** (GC) do Python é como um faxineiro que limpa objetos que não são mais usados. Ele usa **contagem de referências**: cada objeto tem um contador de quantas vezes é referenciado. Se o contador chega a zero (ninguém aponta pra ele), o GC libera a memória. Além disso, o GC também lida com **ciclos de referência** (quando objetos se referenciam mutuamente) usando um algoritmo chamado "coleta cíclica".

**Gerenciar manualmente?**
- Use o módulo `gc` pra forçar a coleta com `gc.collect()`.
- Delete referências com `del` pra zerar o contador de um objeto.
- Evite ciclos de referência em objetos com `__del__` ou use `weakref` pra referências fracas.

Mas, na real, o GC do Python é bem automático, e você só mexe nisso em casos extremos, tipo otimizar uso de memória em apps grandes.

### 4) Qual a diferença entre deepcopy e copy em Python?

O módulo `copy` tem dois métodos: `copy.copy()` (cópia rasa) e `copy.deepcopy()` (cópia profunda).

- **Copy (cópia rasa)**: Copia só o objeto "de cima". Se ele contém outros objetos (como listas dentro de listas), as referências pros objetos internos são mantidas. Ou seja, se você alterar um objeto interno na cópia, a original também muda.
- **Deepcopy (cópia profunda)**: Copia tudo, incluindo os objetos internos, recursivamente. A cópia é completamente independente da original.

**Exemplo:**
```python
import copy
lista = [[1, 2], [3, 4]]
copia_rasa = copy.copy(lista)
copia_profunda = copy.deepcopy(lista)
copia_rasa[0][0] = 99  # Altera a original também
print(lista)  # [[99, 2], [3, 4]]
print(copia_profunda)  # [[1, 2], [3, 4]]  # Intacta
```

Use `copy` pra estruturas simples, `deepcopy` pra objetos complexos com camadas.

### 5) O que são decorators e como eles funcionam?

Decorators são como um "envelopinho" que você coloca em funções ou métodos pra adicionar comportamento extra sem mudar o código original. É uma função que recebe outra função, faz algo com ela (antes, depois, ou até modifica o resultado) e devolve uma nova função.

**Como funciona?**
Você usa `@nome_do_decorator` em cima da função. O decorator "embrulha" a função com outra função (geralmente usando uma função interna chamada `wrapper`).

**Exemplo:**
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__} com {args}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def soma(a, b):
    return a + b

print(soma(2, 3))  # Imprime: Chamando soma com (2, 3) \n 5
```

**Útil pra**: logging, autenticação, medir tempo de execução, ou cache de resultados.

### 6) Explique o conceito de GIL (Global Interpreter Lock) e como ele afeta o multi-threading em Python?

O **GIL** (Global Interpreter Lock) é uma trava no interpretador CPython que garante que só uma thread execute bytecode Python de cada vez, mesmo em processadores com múltiplos núcleos. Isso existe pra simplificar a gestão de memória e evitar problemas com objetos Python em C.

**Como afeta multi-threading?**
- Em tarefas que usam muito CPU (como cálculos pesados), threads não aproveitam múltiplos núcleos por causa do GIL. Uma thread tem que esperar a outra liberar o GIL.
- Em tarefas de I/O (como requisições de rede ou leitura de arquivos), o GIL não atrapalha tanto, porque as threads liberam o GIL enquanto esperam.

**Soluções?**
- Use `multiprocessing` pra tarefas CPU-bound, já que cada processo tem seu próprio interpretador e GIL.
- Use bibliotecas como `numba` ou `Cython` pra pular o GIL em código crítico.
- Pra I/O-bound, threads ou `asyncio` funcionam bem.

### 7) Como funciona a tipagem dinâmica e forte do Python? Dê um exemplo prático.

Python tem **tipagem dinâmica**, ou seja, você não precisa declarar o tipo de uma variável — o interpretador descobre na hora da execução. E é **forte**, porque não faz conversões automáticas entre tipos incompatíveis (como em JavaScript, que junta "5" + 3 e vira "53").

**Exemplo prático:**
```python
# Tipagem dinâmica: não preciso dizer que x é int
x = 5
x = "texto"  # Agora x é str, sem problema

# Tipagem forte: Python não mistura tipos incompatíveis
a = "5"
b = 3
# print(a + b)  # Erro! TypeError: não pode somar str com int
print(int(a) + b)  # Funciona: 8, porque converti explicitamente
```

**Resumo**: Dinâmica = flexibilidade pra mudar tipos. Forte = segurança pra evitar operações malucas sem conversão explícita.

---