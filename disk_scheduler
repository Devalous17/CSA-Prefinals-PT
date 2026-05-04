def fcfs(head, requests):
    return [head] + requests

def stf(head, requests):
    seq = [head]
    reqs = requests.copy()
    current = head
    while reqs:
        # Find the closest track
        closest = min(reqs, key=lambda x: abs(x - current))
        seq.append(closest)
        current = closest
        reqs.remove(closest)
    return seq

def scan(head, requests, max_track=300):
    # Handout moves toward 0 first for SCAN
    reqs = sorted(requests)
    left = [r for r in reqs if r <= head]
    right = [r for r in reqs if r > head]
    
    # Move down to 0, then up
    left.sort(reverse=True)
    right.sort()
    
    if 0 not in left:
        left.append(0)
        
    return [head] + left + right

def c_scan(head, requests, max_track=300):
    reqs = sorted(requests)
    left = [r for r in reqs if r <= head]
    right = [r for r in reqs if r > head]
    
    # Handout moves down to 0, jumps to 300, then moves down again
    left.sort(reverse=True)
    right.sort(reverse=True)
    
    if 0 not in left:
        left.append(0)
    if max_track not in right:
        right.insert(0, max_track)
        
    return [head] + left + right

def c_look(head, requests):
    reqs = sorted(requests)
    left = [r for r in reqs if r <= head]
    right = [r for r in reqs if r > head]
    
    # Similar to C-SCAN but no jumping to physical ends (0 or 300)
    left.sort(reverse=True)
    right.sort(reverse=True)
    
    return [head] + left + right

# --- Execution and Output ---
# Using the exact data from the handout
sample_requests = [25, 290, 215, 50, 75, 120, 85, 245, 98]
start_head = 75 # The first request in the queue

print("--- Storage Access Algorithms ---")
print(f"FCFS:   {fcfs(start_head, sample_requests)}")
print(f"STF:    {stf(start_head, sample_requests)}")
print(f"SCAN:   {scan(start_head, sample_requests)}")
print(f"C-SCAN: {c_scan(start_head, sample_requests)}")
print(f"C-LOOK: {c_look(start_head, sample_requests)}")