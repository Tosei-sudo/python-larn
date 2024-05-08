from multiprocessing.dummy import Pool as ThreadPool
import urllib2

ENDPOINT = "http://localhost/dummy/todos.php"

import time

responses = []

start = time.time()
# Function to send requests asynchronously
def send_request(index):
    response = urllib2.urlopen(ENDPOINT)
    responses.append(response.read())
    return "Request %d is done!" % index

def main():
    # Create a thread pool using ThreadPool
    pool = ThreadPool(3)
    
    # Send each request and get the results
    results = pool.map(send_request, range(3))
    
    # Close the thread pool
    pool.close()
    pool.join()
    
    # Display results
    for result in results:
        print(result)  # Only displaying results here
    
    print("All requests are sent!")

if __name__ == "__main__":
    main()
print responses
print "Time taken: ", time.time() - start