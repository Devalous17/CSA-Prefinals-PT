def calculate_fcfs(processes):
    # processes is a list of lists: [[Process_ID, Arrival_Time, Burst_Time], ...]
    
    n = len(processes)
    
    # Sort processes by Arrival Time just in case they are out of order
    processes.sort(key=lambda x: x[1])
    
    # Arrays to store our calculated times
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n
    
    current_time = 0
    
    for i in range(n):
        pid = processes[i][0]
        arrival = processes[i][1]
        burst = processes[i][2]
        
        # If the CPU is idle (current time is less than arrival time), fast forward
        if current_time < arrival:
            current_time = arrival
            
        # Process executes
        completion_time[i] = current_time + burst
        current_time = completion_time[i] # Update the clock
        
        # Calculate Turnaround and Waiting times
        turnaround_time[i] = completion_time[i] - arrival
        waiting_time[i] = turnaround_time[i] - burst
        
    # Print the Results nicely
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    print("-" * 65)
    for i in range(n):
        print(f"{processes[i][0]}\t{processes[i][1]}\t{processes[i][2]}\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

# --- Testing the Algorithm ---
# Data format: [Process ID, Arrival Time, Burst Time]
process_data = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 8],
    ["P4", 4, 6]
]

calculate_fcfs(process_data)