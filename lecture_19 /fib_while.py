# Solution one: without recursion:
def fib(n):
  first  = 1
  second = 1
  count  = 0

  while(count < n):
    # increment the count
    count +=1 

    # save old first 
    old_first = first  

    # Update values       
    first  = second
    second = old_first + second

  return(first)

def main():
  print(fib(n=6))


if __name__ == '__main__':
  main()