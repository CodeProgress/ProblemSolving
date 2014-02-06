
public class NthPrime {
		
	public static void main(String[] args){

		System.out.println(nthPrime(10001));
		
	}
		
	public static int nthPrime(int n){
		int    count = 0;
		double log2  = Math.log(2);
		int    limit = (int) Math.ceil(n/(1/(Math.log(n)/log2)));
		int[]  nums  = new int[limit + 1];
		
		for (int i = 2; i <= limit; i++){
			if (nums[i] == 0){
				count += 1;
				if (count == n){
					return i;
				}
				for (int j = i*2; j <= limit; j+=i){
					nums[j] = 1;
				}
			}
		}
		
		return -1;
	}
	
}

	
