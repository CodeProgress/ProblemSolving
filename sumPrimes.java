
//Find the sum of all primes under 2000000

public class sumPrimes {
	
	public static void main(String[] args){
		
		System.out.println(sumPrimesUnderN(2000000));
	
	}
	
	public static double sumPrimesUnderN(int limit){
		double count = 0;

		int[] nums = new int[limit + 1];
		for (int i = 2; i <= limit; i++){
			if (nums[i] == 0){
				count += i;
				
				for (int j = i*2; j <= limit; j+=i){
					nums[j] = 1;
				}
			}
		}

		return count;
	}
}


