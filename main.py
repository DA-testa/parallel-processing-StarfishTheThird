# python3

def parallel_processing(n, m, data):
    processors = [(0, i) for i in range(n)]
    results = []
    for processing_time in data:
        earliest_end_time, processor_idx = min(processors)
        results.append((processor_idx, earliest_end_time))
        processors[processor_idx] = (earliest_end_time + processing_time, processor_idx)
    return results

def main():
    n, m = map(int, input("Enter elements: ").split())
    data = list(map(int, input("Enter element values: ").split()))
    results = parallel_processing(n, m, data)
    print("Results:")
    for processor_idx, end_time in results:
        print(processor_idx, end_time)

if __name__ == "__main__":
    main()
