import random
import math

def sphere_function(x):
    return sum(xi ** 2 for xi in x)

def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_eval = func(current)
    step_size = 0.1

    for _ in range(iterations):
        best_neighbor = None
        best_eval = current_eval
        
        for i in range(n):
            for direction in [-1, 1]:
                neighbor = list(current)
                neighbor[i] += direction * step_size
                
                neighbor[i] = max(bounds[i][0], min(neighbor[i], bounds[i][1]))
                
                neighbor_eval = func(neighbor)
                if neighbor_eval < best_eval:
                    best_neighbor = neighbor
                    best_eval = neighbor_eval
        
        if best_neighbor is None:
            step_size /= 2
            if step_size < epsilon:
                break
            continue
            
        if abs(current_eval - best_eval) < epsilon or math.dist(current, best_neighbor) < epsilon:
            current, current_eval = best_neighbor, best_eval
            break
            
        current, current_eval = best_neighbor, best_eval

    return current, current_eval

def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_eval = func(current)
    step_size = 0.5 
    
    for _ in range(iterations):
        neighbor = [
            current[i] + random.uniform(-step_size, step_size)
            for i in range(n)
        ]
        neighbor = [max(bounds[i][0], min(neighbor[i], bounds[i][1])) for i in range(n)]
        neighbor_eval = func(neighbor)

        if neighbor_eval < current_eval:
            if abs(current_eval - neighbor_eval) < epsilon or math.dist(current, neighbor) < epsilon:
                current, current_eval = neighbor, neighbor_eval
                break
            current, current_eval = neighbor, neighbor_eval

    return current, current_eval

def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    n = len(bounds)
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_eval = func(current)
   
    best_pos = list(current)
    best_eval = current_eval
    step_size = 0.5
    
    for _ in range(iterations):
        if temp < epsilon:
            break
            
        neighbor = [
            current[i] + random.uniform(-step_size, step_size)
            for i in range(n)
        ]
        neighbor = [max(bounds[i][0], min(neighbor[i], bounds[i][1])) for i in range(n)]
        neighbor_eval = func(neighbor)
        
        delta = neighbor_eval - current_eval
        
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_eval = neighbor, neighbor_eval
           
            if current_eval < best_eval:
                best_pos = list(current)
                best_eval = current_eval
                
        temp *= cooling_rate

    return best_pos, best_eval

if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)