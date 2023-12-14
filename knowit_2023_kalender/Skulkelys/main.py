def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []
    
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
                
    return primes

def find_elves(input_files):
    with open(input_files['alver_på_jobb.txt'], 'r') as f:
        elves_on_duty = [int(line) for line in f.read().split('\n') if line]
    
    with open(input_files['alver_ikke_på_jobb.txt'], 'r') as f:
        elves_off_duty = [int(line) for line in f.read().split('\n') if line]
    
    with open(input_files['grinchen.txt'], 'r') as f:
        grinch_lights_off = [int(line) for line in f.read().split('\n') if line]
    
    num_windows = 400009
    primes = sieve_of_eratosthenes(num_windows)
    punished_elves = set()
    
    for elf in elves_on_duty:
        for i in range(2):
            window_1 = (elf * 2) % num_windows
            window_2 = (elf + primes[elf % len(primes)]) % num_windows
            
            if window_1 in grinch_lights_off or window_2 in grinch_lights_off:
                punished_elves.add(elf)
                break
    
    for elf in elves_off_duty:
        for i in range(2):
            window_1 = (elf * 2) % num_windows
            window_2 = (elf + primes[elf % len(primes)]) % num_windows
            
            if window_1 not in grinch_lights_off and window_2 not in grinch_lights_off:
                punished_elves.add(elf)
                break
    
    return len(punished_elves)

input_files = {
    'alver_på_jobb.txt': 'knowit_2023_kalender/Skulkelys/alver_på_jobb.txt',
    'alver_ikke_på_jobb.txt': 'knowit_2023_kalender/Skulkelys/alver_ikke_på_jobb.txt',
    'grinchen.txt': 'knowit_2023_kalender/Skulkelys/grinchen.txt'
}

result = find_elves(input_files)
print(f"Antall alver som blir straffet: {result}")
