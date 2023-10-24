#algoritimo Hill Climbing simples para localizar e aproximar mínimo local mais proximo de x = 0
#fn -> função onde se deseja encontrar o mínimo local
#step -> distância que x se desloca, quanto menor for o step mais precisa será a aproximação
#maxIter -> número máximo de iterações antes do programa encerrar caso não encontre nenhum mínimo

def hillClimbing(fn, step, maxIter):
    current = 0
    for i in range(maxIter):
        if fn(current+step) < fn(current):
            current += step
        elif fn(current-step) < fn(current):
            current -= step
        else:
            print(f"Minimo em: x = {current}, y = {fn(current)}")
            break
    else:
        print(f"Limite de iterações atingido! Talvez o minimo tenda para -infinito?")


#função de exemplo:
a = lambda x : x*x + 5*x
hillClimbing(a, 0.5, 10000)